from odoo import http
from odoo.http import request

class PaiementController(http.Controller):
    
    @http.route('/reservation/paiement',csrf=False, type='http', auth="public", website=True, sitemap=False)
    def paiement(self, **post):
       
        return request.render('gr_cu.payment_page')
        
    