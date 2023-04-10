from odoo import http
from odoo.http import request
from werkzeug.exceptions import BadRequest, Forbidden

class EspaceEtudiantController(http.Controller):
    email = None 
    @http.route('/espace_etudiant',csrf=False, type='http', auth="public", website=True, sitemap=False)
    def change_info(self, **post):
        if request.httprequest.method == 'POST':
            code_massar = post.get('code_massar')
            new_email = post.get('email')
            new_phone = post.get('phone')
            new_password = post.get('password')
            user = request.env['cu.resident'].sudo().search([('code_massar', '=', code_massar)])

            if user.sudo().password!=new_password or user.sudo().email!=new_email or user.sudo().phone!=new_phone:
                user.sudo().update({'email': new_email, 'phone': new_phone, 'password': new_password})
                return request.redirect('/welcome')
            else:
                # Handle invalid login
                pass
        