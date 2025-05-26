from odoo import models, fields


class OpenAcademyCourse(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    name = fields.Char(required=True, string='Course Name')
    description = fields.Text(string='Course Description')

    difficulty_level = fields.Selection(
        [
            ('easy', 'Easy'),
            ('medium', 'Medium'),
            ('hard', 'Hard')
        ],
        default='easy'
    )

    # Course relations
    instructor_id = fields.Many2one(
        comodel_name = 'openacademy.partner',
        string = 'Instructor',
        domain="[('is_instructor', '=', True)]"
    )
    session_ids = fields.One2many(comodel_name = 'openacademy.session', inverse_name = 'course_id')
