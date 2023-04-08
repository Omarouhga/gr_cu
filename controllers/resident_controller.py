from odoo import http
from odoo.http import request

class Resident(http.Controller):

    @http.route('/cu_gr/resident/', auth='public',website=True)
    def etudiant_data(self, **post):
        etud_data=request.env['cu.resident'].sudo().search([])
        values={
            'records':etud_data
        }
        return request.render('gr_cu.etud_data_temp',values)