from odoo import http
from odoo.http import request
from werkzeug.exceptions import BadRequest, Forbidden

class AuthController(http.Controller):
    
    @http.route('/auth/login',csrf=False, type='http', auth="public", website=True, sitemap=False)
    def login(self, **post):
        if request.httprequest.method == 'POST':
            email = post.get('email')
            password = post.get('password')
            user = request.env['cu.resident'].sudo().search([('email', '=', email)])
            if user and user.sudo().password==password:
                return "connecté"
            else:
                return "mot de passe ou username incorrect"
        else:
            return request.render('gr_cu.login_template')
        
    @http.route('/auth/logout', type='http', auth="public", website=True, sitemap=False)
    def logout(self):
        request.session.logout()
        return request.redirect('/')
