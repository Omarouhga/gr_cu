from datetime import datetime, timedelta
from odoo import http
from odoo.http import request
from werkzeug.exceptions import BadRequest, Forbidden



class EspaceEtudiantController(http.Controller):
    @http.route('/espace_etudiant',csrf=False, type='http', auth="public", website=True, sitemap=False)
    def change_info(self, **post):
        if request.httprequest.method == 'POST':
            code_massar = post.get('code_massar')
            new_email = post.get('email')
            new_phone = post.get('phone')
            new_password = post.get('password')
            user = request.env['cu.resident'].sudo().search([('code_massar', '=', code_massar)])

            if user.sudo().password != new_password or user.sudo().email != new_email or user.sudo().phone != new_phone:
                user.sudo().write({'email': new_email,
                                    'phone': new_phone, 
                                    'password': new_password})
                message = '1'
            else:
                message = '0'
        else:
            message = None

        etud_data = request.env['cu.resident'].sudo().search([('id', '=', user.id)])
        if etud_data:
            reservations = request.env['cu.reservation'].sudo().search([('resident_id', '=', etud_data.id)])
            values = {
                'records': etud_data,
                'reservations': reservations,
                'message': message
            }
            # Render the welcoming page template with the resident name and solde
            return request.render('gr_cu.welcome_template', values)
        else:
            # Render an error page if no resident is found for the current user
            return request.render('gr_cu.error_template', {'error_message': 'Resident not found for current user'})
    
    @http.route('/reservation',csrf=False, type='http', auth="public", website=True, sitemap=False)
    def reservation(self, **post):
        if request.httprequest.method == 'POST':
            date_start = post.get('start_date')
            date_end = post.get('end_date')
            dejeuner = post.get('DJ')
            diner = post.get('D')
            code_massar = post.get('code_massar')
            resident = request.env['cu.resident'].sudo().search([('code_massar', '=', code_massar)])
            date_consommation = datetime.strptime(date_start, '%Y-%m-%d')
            print(dejeuner)
            while date_consommation <= (datetime.strptime(date_end, '%Y-%m-%d')-timedelta(days=1)):
                if date_consommation.weekday() != 6 and resident:
                    pre_DJ = request.env['cu.reservation'].sudo().search([('resident_id', '=', resident.id),('date_consommation', '=', date_consommation.date()),('type', '=', 'DJ')])
                    pre_D = request.env['cu.reservation'].sudo().search([('resident_id', '=', resident.id),('date_consommation', '=', date_consommation.date()),('type', '=', 'D')])
                    if (not pre_DJ) and dejeuner:
                        reservation = request.env['cu.reservation'].sudo().create({
                        'resident_id': resident.id,
                        'test': dejeuner,
                        'date_consommation': date_consommation.date(),
                        'type': 'DJ'
                        })

                    if not pre_D and diner and date_consommation.weekday() != 5 and resident:
                        reservation = request.env['cu.reservation'].sudo().create({
                        'resident_id': resident.id,
                        'test': diner,
                        'date_consommation': date_consommation.date(),
                        'type': 'D'
                        })
                date_consommation += timedelta(days=1)
                
            return request.redirect('/welcome')
            # price = nb_days * (int(dejeuner) + int(diner))
        else:
            return request.render('gr_cu.error_template', {'error_message': 'Invalid request method'})

