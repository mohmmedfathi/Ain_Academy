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

    available_date = fields.Datetime(
        compute='_compute_available_date',
    )

    # Relations
    session_id = fields.One2many(
        comodel_name='openacademy.session',
        inverse_name='room_id',
        string='Sessions'
    )

    instructor_id = fields.Many2one(
        comodel_name='openacademy.partner',
        compute='_compute_instructor_id',
        string='Instructor'
    )

    # Compute Methods
    @api.depends('session_id.end_date')
    def _compute_available_date(self):

        for record in self:
            session = record.session_id
            record.available_date = session.end_date if session else fields.Datetime.now()


    @api.depends('session_id.instructor_id')
    def _compute_instructor_id(self):
        for record in self:
            session = record.session_id
            if session and session.instructor_id:
                record.instructor_id = session.instructor_id
            else:
                record.instructor_id = False

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

    
    def action_unreserve_session(self):
        
        
        self.session_id = False
        self.state = 'available'
        