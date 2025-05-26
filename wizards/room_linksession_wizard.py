from odoo import models, fields
from odoo.exceptions import ValidationError

class RoomLinkSessionsWizard(models.TransientModel):
    _name = 'room.link.sessions.wizard'
    _description = 'Link Existing Sessions to Room'

    room_id = fields.Many2one('openacademy.room', required=True, readonly=True)
    session_ids = fields.Many2many(
        'openacademy.session',
        string='Unassigned Sessions',
        domain="[('room_id', '=', False)]"
    )

    def action_link_sessions(self):
        print("*" * 60)
        print(self)
        print("dfsnjfdjsjdknfsdfsdfs")
        for wizard in self:
            wizard.session_ids.write({'room_id': wizard.room_id.id})