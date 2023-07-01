from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class CUGerant(models.Model):
    _name = "cu.gerant"
    _rec_name = "name"

    name = fields.Char(string="Nom", required=True)
    last_name = fields.Char(string="Prénom", required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    image = fields.Image(string="Image")
    @api.constrains('phone')
    def check_phone_number(self):
        for rec in self:
            if rec.phone and len(rec.phone) != 10:
                raise ValidationError("PHONE MUST HAVE 10 DIGIT !!!")
        return True

    @api.constrains('email')
    def check_unique_email(self):
        for rec in self:
            if rec.email and self.search_count([('email', '=', rec.email), ('id', '!=', rec.id)]) > 0:
                raise ValidationError("Email must be unique!")
        return True

    @api.model
    def create(self, vals):
        self.valid_email(vals.get('email'))
        existing_record = self.search([('email', '=', vals.get('email'))])
        if existing_record:
            raise ValidationError("Email must be unique!")
        return super(CUGerant, self).create(vals)

    def write(self, vals):
        if 'email' in vals:
            self.valid_email(vals.get('email'))
            existing_record = self.search([('email', '=', vals.get('email')), ('id', '!=', self.id)])
            if existing_record:
                raise ValidationError("Email must be unique!")
        return super(CUGerant, self).write(vals)

    @api.model
    def valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValidationError('Invalid email address')

    
