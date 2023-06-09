from odoo import http
from odoo.http import request
# from authorizenet import apicontract, constants
# from authorizenet.apicontrollers import createTransactionController

class PaymentController(http.Controller):
    
    # @http.route('/paiement', type='http', auth='public', website=True)
    # def process_payment(self, **kw):
        # Retrieve the order information and total amount to charge
        # montant = kw.get('montant')
        
        # # Create a new transaction request using Authorize.Net API
        # transaction = apicontract.TransactionRequest()
        # transaction.transactionType = constants.TRANSACTION_TYPE_AUTH_CAPTURE
        # transaction.amount = montant
        # transaction.order = apicontract.OrderType()
        
        # # Send the transaction request to Authorize.Net
        # controller = createTransactionController(transaction)
        # controller.execute()
        # response = controller.getresponse()
        
        # # Check the response and update the order status accordingly
        # if response is not None:
        #     if response.messages.resultCode == "Ok":
        #         # Payment is successful
        #         # Update the order status to 'paid'
        #         return http.redirect_with_hash('/shop/payment/validate')
        # return request.render('gr_cu.payment_process_page')
    
    @http.route('/paiement/montant', type='http', auth='public', website=True)
    def amount_payment(self, **kw):
        
        return request.render('gr_cu.payment_process_page')