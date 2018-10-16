# -*- encoding: utf-8 -*-

from odoo import models, fields, api


class RegistrationEditor(models.TransientModel):

	_inherit = "registration.editor"

	@api.multi
	def action_make_registration(self):
		res = super(RegistrationEditor, self).action_make_registration()
		for registration_line in self.event_registration_ids:
			if registration_line.registration_id.event_id.state != 'confirm':
				registration_line.registration_id.event_id.state = 'confirm'
		return res
