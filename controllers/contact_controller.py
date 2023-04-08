from odoo import http
from odoo.http import request

class ContactController(http.Controller):
    
    @http.route('/contact',csrf=False, type='http', auth="public", website=True, sitemap=False)
    def contact(self, **post):
       
        return request.render('gr_cu.contact_us_page')
        
    