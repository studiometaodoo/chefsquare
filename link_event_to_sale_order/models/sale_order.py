# -*- encoding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
	_inherit = 'sale.order'

	@api.multi
	def action_cancel_with_event(self):
		for line in self.order_line:
			if line.event_id:
				line.event_id.state = 'cancel'
				if line.event_id.registration_ids:
					for registration in line.event_id.registration_ids:
						registration.unlink()

		self.action_cancel()

	@api.multi
	def action_draft_with_event(self):
		for line in self.order_line:
			if line.event_id:
				line.event_id.state = 'draft'
		self.action_draft()
