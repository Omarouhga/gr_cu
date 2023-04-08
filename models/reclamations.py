from odoo import models,fields,api
from odoo.exceptions import ValidationError
import re

class CUReclamation(models.Model):
    _name="cu.reclamation"
    _rec_name="nom_complet"

    nom_complet=fields.Char(string="Nom complet",required=True)
    sujet=fields.Char(string="Sujet",required=True)
    message=fields.Char(string="Message",required=True)
    email=fields.Char(string="Email")
    

    