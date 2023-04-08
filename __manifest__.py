{
    'name': 'restauration cité universitaire',
    'version': '1.0',
    'category':'CU',
    'sequence': '-1',
    'summary': "Gestion des réservation et vérification des repas au cité universitaire",
    'description': "",
    
    'depends': 
    [
        'base','website','web'  
    ],
    'data':[
        'security/cu_groups.xml',
        'security/ir.model.access.csv',
        'wizards/charger_solde_wiz_view.xml',
        'views/web_template.xml',
        'views/login_template.xml',
        'views/welcome_template.xml',
        # 'views/paiement_template.xml',
        'views/website_layout.xml',
        'views/city_universitaire_reservation_view.xml',
        'views/city_universitaire_reclamation_view.xml',
        'views/city_universitaire_resident_view.xml',
        'views/city_universitaire_agent_view.xml',
        'views/city_universitaire_gerant_view.xml',
        'views/city_universitaire_menu_view.xml'
    ],
    
     'installable': True,
    'application': True,
    'auto_install': False,
     'license': 'LGPL-3',
     'author': "TDI ENSA BM"
     
    
}