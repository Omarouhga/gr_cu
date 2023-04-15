from odoo import http
from odoo.http import request
from werkzeug.exceptions import BadRequest, Forbidden



class EspaceEtudiantController(http.Controller):
    @http.route('/espace_etudiant',csrf=False, type='http', auth="public", website=True, sitemap=False)
    def change_info(self, **post):
        if request.httprequest.method == 'POST':
            code_massar = post.get('code_massar')
            new_email = post.get('email')
            new_phone = post.get('phone')
            new_password = post.get('password')
            user = request.env['cu.resident'].sudo().search([('code_massar', '=', code_massar)])

            if user.sudo().password != new_password or user.sudo().email != new_email or user.sudo().phone != new_phone:
                user.sudo().write({'email': new_email,
                                    'phone': new_phone, 
                                    'password': new_password})
                message = '1'
            else:
                message = '0'
        else:
            message = None

        etud_data = request.env['cu.resident'].sudo().search([('id', '=', user.id)])
        if etud_data:
            reservations = request.env['cu.reservation'].sudo().search([('resident_id', '=', etud_data.id)])
            values = {
                'records': etud_data,
                'reservations': reservations,
                'message': message
            }
            # Render the welcoming page template with the resident name and solde
            return request.render('gr_cu.welcome_template', values)
        else:
            # Render an error page if no resident is found for the current user
            return request.render('gr_cu.error_template', {'error_message': 'Resident not found for current user'})
    