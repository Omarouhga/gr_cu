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

    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')
    
   
