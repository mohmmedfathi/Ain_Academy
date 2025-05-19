from odoo import models, fields, api

class OpenAcademyCourse(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    name = fields.Char(required=True,string='Course Name')
    description = fields.Text(string ='Course Description')
    difficulty_level = fields.Selection([
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard')
    ], default='easy')
    instructor_id = fields.Many2one('openacademy.partner',domain="[('is_instructor', '=', True)]")
    session_ids = fields.One2many('openacademy.session', 'course_id')