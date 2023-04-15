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
    

    @api.constrains('phone')
    def check_phone_number(self):
        for rec in self:
            if rec.phone and len(rec.phone) != 10:
                raise ValidationError("PHONE MUST HAVE 10 DIGIT !!!")
        return True

    @api.model
    def create(self, vals):
        self.valid_email(vals.get('email'))
        return super(CUAgent, self).create(vals)

    def write(self, vals):
        if 'email' in vals:
            self.valid_email(vals.get('email'))
        return super(CUAgent, self).write(vals)
    
    @api.model
    def valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValidationError('Invalid email address')

    @api.onchange("last_name","name")
    def compute_name(self):
        for rec in self:
            rec.name=""
            if  rec.name :
                rec.name=rec.name+rec.name.upper()+" "
            if rec.last_name :
                rec.name=rec.name+rec.last_name.title()+" "