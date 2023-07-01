from odoo import models,fields,api
from odoo import exceptions
from odoo.http import request


class CUchargersolde(models.TransientModel):
    _name="cu.resident.solde"
    _inherit=['mail.thread','mail.activity.mixin']

    _description="Charger solde d'un resident"
   
    montant=fields.Integer("Montant")
    
    
    
    def charger_solde(self):
        resident_recent=self.env['cu.resident'].browse(self.env.context.get('active_id'))  
        email=resident_recent.email
        
        resident_recent.solde+=self.montant
        body_html = """
                        <html>
                            
                            <body>
                                <div >
                                    <h3>Bonjour <b>{user_name}</b>,</h3>
                                    <p>Nous sommes ravis pour vous informer que vous avez recharger votre compte par {montant}Dh.</p>
                                    <p>Votre solde actuel est {montant_actuel}Dh.</p>
                                    <p>Si vous avez des questions ou des préoccupations, n'hésitez pas à nous contacter. Nous sommes toujours là pour vous aider.</p>
                                    <p>Cordialement,<br>L'équipe de {company_name}</p>
                                </div>
                            </body>
                        </html>
                        """.format(
                            user_name=resident_recent.name,
                            company_name='TDI SOCITY',
                            montant=self.montant,
                            montant_actuel = resident_recent.solde,
                        )
        mail_values = {
                        'subject': 'Rechargement du compte',
                        'body_html': body_html,
                        'email_from': 'omarouhga12@gmail.com',
                        'email_to': email,
                    }
        request.env['mail.mail'].sudo().create(mail_values).send()
        
