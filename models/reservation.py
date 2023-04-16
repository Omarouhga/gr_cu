from odoo import models,fields,api
from odoo.exceptions import ValidationError
import re
from datetime import datetime



class CUReservation(models.Model):
    _name="cu.reservation"
    
    resident_id = fields.Many2one('cu.resident',string="Résident",required=True)
    date_reservation = fields.Date(string="Date de réservation",default=datetime.today(),required=True)
    date_consommation=fields.Date(string="Date de consommation",required=True)
    type = fields.Selection([('DJ','déjeuner'),('D','Diner')],required=True,string="Type")
    
    
    @api.constrains('resident_id', 'date_consommation', 'type')
    def _check_reservation_limit(self):
        for rec in self:
            domain = [
                ('resident_id', '=', rec.resident_id.id),
                ('date_consommation', '=', rec.date_consommation),
                ('type', '=', rec.type),
            ]
            count = self.search_count(domain)
            if count > 1:
                raise ValidationError("The resident can only reserve one lunch and one dinner per day.")
    
    
    @api.model
    def create(self, values):
        reservation = super(CUReservation, self).create(values)
        reservation._check_reservation_limit()
        return reservation

    def write(self, values):
        result = super(CUReservation, self).write(values)
        self._check_reservation_limit()
        return result
