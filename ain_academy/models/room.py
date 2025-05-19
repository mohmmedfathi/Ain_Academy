from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta
from .helpers import _get_last_available_date,_get_session_sort_key

class OpenAcademyRoom(models.Model):
    _name = 'openacademy.room'
    _description = 'Room'

    name = fields.Char()
    price = fields.Float()
    state = fields.Selection(
        [('available', 'Available'), ('reserved', 'Reserved')],
        default='available'
    )
    available_date = fields.Datetime(default=fields.Datetime.now)

    # room relations
    session_ids = fields.One2many('openacademy.session', 'room_id')

    # room computed fields
    instructor_ids = fields.Many2many(
        'openacademy.partner',
        compute='_compute_room_schedule'
    )

    def _get_instructors_from_sessions(self,sorted_sessions):
        return sorted_sessions.mapped('instructor_id')

    @api.depends('session_ids.start_date', 'session_ids.end_date')
    def _compute_room_schedule(self): 
        """
            when add session so two things happen 
            1 - Update the instructor list based on sessions.
            2 - Update the available_date to match the end_date of the latest session.
        """
        for record in self:
            sessions = record.session_ids
            sorted_sessions = sessions.sorted(_get_session_sort_key)

            record.instructor_ids = record._get_instructors_from_sessions(sorted_sessions)
            record.available_date = _get_last_available_date(sorted_sessions) # we can make it inverse
                                                                                   # when the sessions added make an inverse to update

   

    def action_reserve(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Reserve Room',
            'res_model': 'room.reservation.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_room_id': self.id}
        }

    
    def action_unreserve_specific_session(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Unreserve Specific Session',
            'res_model': 'room.unreserve.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_room_id': self.id}
        }

    def action_unreserve_all_sessions(self):
        for record in self:
            record.session_ids.write({'room_id': False})
            record.state = 'available'

