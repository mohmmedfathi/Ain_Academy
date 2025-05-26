from odoo import models, fields, api


class OpenAcademyRoom(models.Model):
    _name = 'openacademy.room'
    _description = 'Room'

    name = fields.Char()
    price = fields.Monetary(string="Price")
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency'
    )

    state = fields.Selection(
        [
            ('available', 'Available'),
            ('reserved', 'Reserved')
        ],
        string='State',
        default='available'
    )
    available_date = fields.Datetime(default=fields.Datetime.now)

    # Room relations
    session_ids = fields.One2many(
        comodel_name='openacademy.session',
        inverse_name='room_id',
        string='Sessions'
    )

    instructor_ids = fields.Many2many(
        comodel_name='openacademy.partner',
        relation='openacademy_room_instructor_rel',
        column1='room_id',
        column2='instructor_id',
        compute='_compute_room_schedule',
        string='Instructors'
    )

    # Compute methods
    @api.depends('session_ids.start_date', 'session_ids.end_date')
    def _compute_room_schedule(self):
        """
        Updates instructor list and available date based on linked sessions.
        """
        for record in self:
            sessions = record.session_ids
            sorted_sessions = sessions.sorted(lambda s: s.end_date)

            record.instructor_ids = record._get_instructors_from_sessions(sorted_sessions)
            record.available_date = self._get_last_available_date(sorted_sessions)

    @staticmethod
    def _get_last_available_date(sorted_sessions):
        if sorted_sessions:
            return sorted_sessions[-1].end_date
        return fields.Datetime.now()

    def _get_instructors_from_sessions(self, sorted_sessions):
        return sorted_sessions.mapped('instructor_id')

    # Actions
    def action_reserve(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Reserve Room',
            'res_model': 'room.reservation.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_room_id': self.id},
        }

    def action_unreserve_specific_session(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Unreserve Specific Session',
            'res_model': 'room.unreserve.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_room_id': self.id},
        }

    def action_unreserve_all_sessions(self):
        for record in self:
            record.session_ids.write({'room_id': False})
            record.state = 'available'

    def action_open_link_sessions_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Link Existing Sessions',
            'res_model': 'room.link.sessions.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_room_id': self.id},
        }
