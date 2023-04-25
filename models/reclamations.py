from odoo import models,fields,api
from odoo.exceptions import ValidationError
import re

class CUReclamation(models.Model):
    _name="cu.reclamation"
    _rec_name="name"

    name=fields.Char(string="Nom complet")
    subject=fields.Char(string="Sujet")
    message=fields.Text(string="Message")
    email=fields.Char(string="Email")
    

    