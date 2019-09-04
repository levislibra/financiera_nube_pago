# -*- coding: utf-8 -*-
from openerp import http

# class FinancieraNubePago(http.Controller):
#     @http.route('/financiera_nube_pago/financiera_nube_pago/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/financiera_nube_pago/financiera_nube_pago/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('financiera_nube_pago.listing', {
#             'root': '/financiera_nube_pago/financiera_nube_pago',
#             'objects': http.request.env['financiera_nube_pago.financiera_nube_pago'].search([]),
#         })

#     @http.route('/financiera_nube_pago/financiera_nube_pago/objects/<model("financiera_nube_pago.financiera_nube_pago"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('financiera_nube_pago.object', {
#             'object': obj
#         })