from odoo import models, fields
from odoo.exceptions import ValidationError

class RoomReservationWizard(models.TransientModel):
    _name = 'room.reservation.wizard'
    _description = 'Room Reservation Wizard'

    room_id = fields.Many2one('openacademy.room', string="Room", required=True)
    session_id = fields.Many2one('openacademy.session', string="Session", required=True,
                                 domain="[('room_id', '=', False)]")

    def action_reserve_room(self):
        """
        Reserve the selected room for the selected session.
        """
        if not self.room_id or not self.session_id:
            raise ValidationError("Both Room and Session are required.")

        self.session_id.room_id = self.room_id.id
        self.room_id.state = 'reserved'
        
        return {'type': 'ir.actions.act_window_close'}
