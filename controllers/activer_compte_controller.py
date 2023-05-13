import uuid
from odoo import http
from odoo.http import request
from odoo.exceptions import UserError

class AccountConfirmationController(http.Controller):

    @http.route('/auth/activer',csrf=False, type='http', auth="public", website=True, sitemap=False)
    def confirm_account(self, **post):
        account_actived=None
        if request.httprequest.method == 'POST':
            email = post.get('email')
            user = request.env['cu.resident'].sudo().search([('email', '=', email)])
            if not user:
                raise UserError('User with email %s not found' % email) 
            else:
                account_actived=user.sudo().account_actived
           
                if account_actived==False:
                    
                   
                    token = str(uuid.uuid4())
                    user.sudo().write({'password': token,
                                    'confirmation_token':token})
                    confirmation_url = request.httprequest.host_url + 'auth/login'
                    body_html = """
                        <html>
                            
                            <body>
                                <div >
                                    <h3>Bonjour <b>{user_name}</b>,</h3>
                                    <p>Nous sommes ravis que vous ayez créé un compte chez nous. Pour assurer la sécurité de votre compte, nous vous demandons de changer votre mot de passe après la première connexion.</p>
                                    <p>Votre mot de passe temporaire est:</p>
                                    <h4>{token}</h4>
                                    <p>Veuillez utiliser le lien ci-dessous pour accéder à votre compte et changer votre mot de passe:</p>
                                    <p><a href="{confirmation_url}">{confirmation_url}</a></p>
                                    <p>Si vous avez des questions ou des préoccupations, n'hésitez pas à nous contacter. Nous sommes toujours là pour vous aider.</p>
                                    <p>Cordialement,<br>L'équipe de {company_name}</p>
                                </div>
                            </body>
                        </html>
                        """.format(
                            user_name=user.name,
                            token=token,
                            confirmation_url=confirmation_url,
                            company_name='TDI SOCITY',
                        )
                    mail_values = {
                        'subject': 'Activer votre compte Réstauration CU',
                        'body_html': body_html,
                        'email_from': 'omarouhga12@gmail.com',
                        'email_to': email,
                    }
                    request.env['mail.mail'].sudo().create(mail_values).send()
                    user.sudo().write({'account_actived': True})
                
            
        return request.render('gr_cu.activer_compte',{'message':account_actived})


    @http.route('/create_password', type='http', auth='public', website=True)
    def create_password(self, token, **post):
        user = request.env['cu.resident'].sudo().search([('confirmation_token', '=', token)])
        if not user:
            raise UserError('Invalid confirmation token')
        if user.account_actived:
            raise UserError('Email already confirmed for user %s' % user.name)
        password = post.get('password')
        user.sudo().write({
            'password': password,
            'confirmation_token': '',
            'account_actived': True,
        })
        return request.render('gr_cu.create_password_template', {'user': user})
