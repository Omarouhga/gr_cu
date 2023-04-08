from odoo import models,fields,api
from odoo.exceptions import ValidationError
import re

class CUAgent(models.Model):
    _name="cu.agent"
    _rec_name="name"

    name=fields.Char(string="Nom",required=True)
    last_name=fields.Char(string="Prénom",required=True)
    phone=fields.Char(string="Phone",required=True)
    email=fields.Char(string="Email")
    

    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')
    
    def check_phone_number(self):
        for rec in self:
            if rec.phone and len(rec.phone) != 10:
                raise ValidationError("PHONE MUST HAVE 10 DIGIT !!!")
        return True

    @api.onchange("last_name","name")
    def compute_name(self):
        for rec in self:
            rec.name=""
            if  rec.name :
                rec.name=rec.name+rec.name.upper()+" "
            if rec.last_name :
                rec.name=rec.name+rec.last_name.title()+" "