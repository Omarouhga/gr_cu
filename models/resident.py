from odoo import models,fields,api
from odoo.exceptions import ValidationError
import re

class CUResident(models.Model):
    _name="cu.resident"
    _rec_name="name"

    name=fields.Char(string="Nom",required=True)
    last_name=fields.Char(string="Prénom",required=True)
    gender=fields.Selection([('F','Femme'),('Ma.','Homme'),('u','autre')],required=True,string="Genre")
    phone=fields.Char(string="Phone",required=True)
    email=fields.Char(string="Email")
    password=fields.Char(strng="Password",required=True)
    code_massar=fields.Char(strng="Code Appoge",required=True)
    hex_id = fields.Char(string="HEX ID")
    reservations = fields.One2many('cu.reservation','resident_id',string="reservation")
    solde = fields.Integer(string="Solde")
    apogee=fields.Integer(String="Apogee")
    

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


    def effectuer_reservation():
        
        return 0

    def annuler_reservation():
        return 0
    
    def modifier_reservation():
        return 0
    
    def transferer_solde():
        return 0
    
    
    
    

    # @api.onchange("last_name","name")
    # def compute_name(self):
    #     for rec in self:
    #         rec.name=""
    #         if  rec.name :
    #             rec.name=rec.name+rec.name.upper()+" "
    #         if rec.last_name :
    #             rec.name=rec.name+rec.last_name.title()+" "