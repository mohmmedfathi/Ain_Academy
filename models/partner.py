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
    is_instructor = fields.Boolean(string='Is Instructor',default=False)
    image = fields.Image(string='Profile Image')

    attended_session_ids = fields.Many2many(
        comodel_name='openacademy.session',
        relation='openacademy_student_session_rel',
        column1='student_id',
        column2='session_id',
        string='Attended Sessions',
    )
 

    instructor_id = fields.One2many(
        comodel_name = 'openacademy.session', 
        inverse_name = 'instructor_id'
    )
