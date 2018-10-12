# -*- encoding: utf-8 -*-

from odoo import models, fields, api


class EventRegistration(models.Model):
	_inherit = 'event.registration'

	state = fields.Selection(selection_add=[('inactive', 'Waiting')])

	@api.one
	@api.constrains('event_id', 'state')
	def _check_seats_limit(self):
		if self.event_id.seats_availability == 'limited' \
				and self.event_id.seats_max \
				and self.event_id.seats_available < (1 if self.state == 'draft' else 0):
			self.state = 'inactive'
			if not self.event_id.warning_max_seats:
				self.event_id.warning_max_seats = 'No more seats available for this event.'
		if self.event_ticket_id.seats_availability == 'limited' \
				and self.event_ticket_id.seats_max \
				and self.event_ticket_id.seats_available < (1 if self.state == 'draft' else 0):
			self.state = 'inactive'

	@api.one
	def button_reg_cancel(self):
		if self.state == 'open':
			for waiting_attendee in self.event_id.waiting_attendee_ids:
				print(waiting_attendee.name)
				print(waiting_attendee.state)
				if waiting_attendee.event_ticket_id == self.event_ticket_id:
					self.env['mail.template'].search([('name', '=', 'Notify waiting attendees about the last place (with ticket type)')],
													 limit=1).send_mail(waiting_attendee.id, force_send=True)
				if not waiting_attendee.event_ticket_id:
					self.env['mail.template'].search([('name', '=', 'Notify waiting attendees about the last place')],
												 limit=1).send_mail(waiting_attendee.id, force_send=True)
		if self.event_id.warning_max_seats:
			self.event_id.warning_max_seats = None
		self.state = 'cancel'


class Event(models.Model):
	_inherit = 'event.event'

	warning_max_seats = fields.Char(readonly=True)
	waiting_attendee_ids = fields.One2many(
		'event.registration', 'event_id', string='Attendees',
		readonly=False, states={'done': [('readonly', True)]}, domain=[('state', '=', 'inactive')])