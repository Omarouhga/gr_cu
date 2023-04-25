from odoo import http
from odoo.http import request

class ContactController(http.Controller):
    
    @http.route('/contact',csrf=False, type='http', auth="public", website=True, sitemap=False)
    def contact(self, **post):
        message=None
        if request.httprequest.method == 'POST':
            name = post.get('name')
            email = post.get('email')
            subject = post.get('subject')
            message = post.get('message')
            request.env['cu.reclamation'].sudo().create({
                                                            'name': name,
                                                            'email': email,
                                                            'subject': subject,
                                                            'message': message,
                                                                })
            message=1
        else:
            message=None            
        return request.render('gr_cu.contact_us_page',{'message':message})
        
    