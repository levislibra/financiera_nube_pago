# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import UserError, ValidationError
# import http.client

class FinancieraNubePagoCuenta(models.Model):
	_name = 'financiera.nube.pago.cuenta'

	name = fields.Char('Nombre')
	company_id = fields.Many2one('res.company', 'Empresa', default=lambda self: self.env['res.company']._company_default_get('financiera.pagos.360.cuenta'))
	id_nube_pago = fields.Integer('Id de Usuario NubePago')
	api_key = fields.Char('API Key')
	api_secret_key = fields.Char('API Secret Key')
	available_balance = fields.Float("Saldo Disponible")
	unavailable_balance = fields.Float("Saldo Pendiente")

	expire_create_new = fields.Boolean("Crear nueva Solicitud de Pago al expirar")
	expire_days_payment = fields.Integer("Dias para pagar la nueva Solicitud de Pago")

	def button_test(self):
		conn = http.client.HTTPSConnection("api.pagos360.com")
		headers = { 'authorization': "Bearer <API Key>" }
		conn.request("GET", "/account/balances", headers=headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

# class FinancieraPagos360Solicitud(models.Model):
# 	_name = 'financiera.pagos.360.solicitud'

# 	id_solicitud = fields.Integer("ID de la solicitud")
# 	state = fields.Selection([
# 			('pendiente', 'Pendiente'), ('pagada', 'Pagada'),
# 			('expirada', 'Expirada'), ('revertida', 'Revertida')],
# 			string='Estado', readonly=True, default='pendiente')
# 	cuota_id = fields.Many2one('financiera.prestamo.cuota', 'Cuota')

# 	@api.model
# 	def create(self, values):
# 		rec = super(FinancieraPagos360Solicitud, self).create(values)
# 		conn = http.client.HTTPSConnection("api.pagos360.com")
# 		# payload = "{\"payment_request\":{\"description\":\"concepto_del_pago\",\"first_due_date\":\"25-01-2020\",\"first_total\":200.99,\"payer_name\":\"nombre_pagador\"}}"
# 		payload = {
# 			'payment_request': {
# 				'description': 'Pago de cuota',
# 				'first_due_date': self.cuota_id.fecha_vencimiento,
# 				'first_total': self.cuota_id.saldo,
# 				'payer_name': self.cuota_id.partner_id.name,
# 			}
# 		}
# 		headers = {
# 			'content-type': "application/json",
# 			'authorization': "<API Key>"
# 		}
# 		conn.request("POST", "/payment-request", payload, headers)
# 		res = conn.getresponse()
# 		data = res.read()
# 		print(data.decode("utf-8"))

# class ExtendsFinancieraPrestamoCuota(models.Model):
# 	_inherit = 'financiera.prestamo.cuota' 
# 	_name = 'financiera.prestamo.cuota'

# 	cobrar_pagos_360_voluntario = fields.Boolean('Cobrar mediante Pagos360 voluntario')
# 	pagos_360_solicitud_id = fields.Many2one('financiera.pagos.360.solicitud', 'Pagos360 - Solicitud')

# 	@api.one
# 	def pagos_360_crear_solicitud(self, fecha_vencimiento):



# class ExtendsFinancieraPrestamo(models.Model):
# 	_inherit = 'financiera.prestamo' 
# 	_name = 'financiera.prestamo'

# 	@api.one
# 	def enviar_a_acreditacion_pendiente(self):
# 		rec = super(ExtendsFinancieraPrestamo, self).enviar_a_acreditacion_pendiente()

# 		for cuota_id in self.cuota_ids:
# 			cuota_id.