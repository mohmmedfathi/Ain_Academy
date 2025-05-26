from odoo import models, fields


class OpenAcademyPartner(models.Model):
    _name = 'openacademy.partner'
    _description = 'Partner'
    _order = 'age desc'

    name = fields.Char(
        string='Partner Name',
        required=True,
        index=True
    )
    age = fields.Integer(string='Partner Age')
    is_instructor = fields.Boolean(
        string='Is Instructor',
        default=False
    )
    image = fields.Image(string='Profile Image')

    attended_session_ids = fields.Many2many(
        comodel_name='openacademy.session',
        relation='openacademy_student_session_rel',
        column1='student_id',
        column2='session_id',
        string='Attended Sessions',
        compute='_compute_attended_sessions',
        store=False
    )
    sessions_taught = fields.Many2many(
        comodel_name='openacademy.session',
        relation='openacademy_partner_session_rel',
        column1='instructor_id',
        column2='session_id',
        string='Taught Sessions',
        compute='_compute_sessions_taught',
        store=False
    )

    # Compute methods
    def _compute_attended_sessions(self):
        for partner in self:
            partner.attended_session_ids = self.env['openacademy.session'].search([('attended_student_ids', 'in', [partner.id])])

    def _compute_sessions_taught(self):
        for partner in self:
            partner.sessions_taught = self.env['openacademy.session'].search([('instructor_id', '=', partner.id)])
