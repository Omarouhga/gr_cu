from odoo import http
from odoo.http import request
from werkzeug.exceptions import BadRequest, Forbidden

class AuthController(http.Controller):
    email = None 
    @http.route('/auth/login',csrf=False, type='http', auth="public", website=True, sitemap=False)
    def login(self, **post):
        error=None
        if request.httprequest.method == 'POST':
            
            global email
            email = post.get('email')
            password = post.get('password')
            user = request.env['cu.resident'].sudo().search([('email', '=', email)])

            if user and user.sudo().password==password:
                return request.redirect('/welcome')
            else:
                error="Mot de passe ou email est incorrect"
        
        return request.render('gr_cu.login_template',{'error':error})
        
    @http.route('/auth/logout', type='http', auth="public", website=True, sitemap=False)
    def logout(self):
        request.session.logout()
        return request.redirect('/')
    @http.route('/welcome', type='http', auth="public", website=True, sitemap=False)
    def welcome(self):
        if email :
            etud_data=request.env['cu.resident'].sudo().search([('email', '=', email)])
            values={
            'records':etud_data}
            # Render the welcoming page template with the resident name and solde
            return request.render('gr_cu.welcome_template',values)
        else:
            # Render an error page if no resident is found for the current user
            return request.render('gr_cu.error_template', {'error_message': 'Resident not found for current user'})