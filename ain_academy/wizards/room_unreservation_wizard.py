from odoo import models, fields, api
from odoo.exceptions import ValidationError

class RoomUnreserveWizard(models.TransientModel):
    _name = 'room.unreserve.wizard'
    _description = 'Room Unreserve Wizard'

    room_id = fields.Many2one('openacademy.room', string="Room", required=True)
    session_id = fields.Many2one('openacademy.session', string="Session to Unreserve", required=True,
                                 domain="[('room_id', '!=', False)]")

    def action_unreserve_session(self):
        if not self.session_id:
            raise ValidationError("You must select a session to unreserve.")
        self.session_id.room_id = False
        return {'type': 'ir.actions.act_window_close'}
