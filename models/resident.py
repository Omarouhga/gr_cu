from odoo import models,fields,api
from odoo.exceptions import ValidationError
import re

class CUResident(models.Model):
    _name="cu.resident"
    _inherit=['mail.thread','mail.activity.mixin']
    _rec_name="name"

    name=fields.Char(string="Nom",required=True)
    last_name=fields.Char(string="Prénom",required=True)
    gender=fields.Selection([('F','Femme'),('Ma.','Homme'),('u','autre')],required=True,string="Genre")
    phone=fields.Char(string="Phone",required=True)
    email=fields.Char(string="Email",required=True)
    date_naissance=fields.Date(string='Date de naissance')
    date_residence=fields.Date(string='Date de résidence')
    password=fields.Char(strng="Password",required=True)
    code_massar=fields.Char(strng="Code Appoge",required=True)
    hex_id = fields.Char(string="HEX ID")
    reservations = fields.One2many('cu.reservation','resident_id',string="reservation")
    solde = fields.Float(string="Solde")
    apogee=fields.Integer(String="Apogee")
    account_actived = fields.Boolean(string='compte activé',default=False) 
    confirmation_token = fields.Char(string='Confirmation token')
    image_resident = fields.Image(string="Image")
    
    
    @api.constrains('phone')
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
        return super(CUResident, self).create(vals)

    def write(self, vals):
        if 'email' in vals:
            self.valid_email(vals.get('email'))
            existing_record = self.search([('email', '=', vals.get('email')), ('id', '!=', self.id)])
            if existing_record:
                raise ValidationError("Email must be unique!")
        return super(CUResident, self).write(vals)

    @api.model
    def valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValidationError('Invalid email address')
    
    
    def effectuer_reservation():
        
        return 0

    def annuler_reservation():
        return 0
    
    def modifier_reservation():
        return 0
    
    # @api.multi
    # def write(self, values):
    #     for rec in self:
    #         if rec.password!=rec.confirmation_token:
    #             values={'account_actived':True}
    
    #     return super(CUResident, self).write(values)
        
    
    
    

    # @api.onchange("last_name","name")
    # def compute_name(self):
    #     for rec in self:
    #         rec.name=""
    #         if  rec.name :
    #             rec.name=rec.name+rec.name.upper()+" "
    #         if rec.last_name :
    #             rec.name=rec.name+rec.last_name.title()+" "