from odoo import models,fields,api
from odoo import exceptions

class CUchargersolde(models.TransientModel):
    _name="cu.resident.solde"
    _description="Charger solde d'un resident"
   
    montant=fields.Integer("Montant")
    
    
    
    def charger_solde(self):
        resident_recent=self.env['cu.resident'].browse(self.env.context.get('active_id'))    
        resident_recent.solde+=self.montant
