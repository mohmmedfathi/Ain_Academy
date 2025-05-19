from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta, datetime
from .helpers import validate_new_session

class OpenAcademySession(models.Model):
    _name = 'openacademy.session'
    _description = 'Session'

    name = fields.Char(required=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done')]
        , default='draft')
    start_date = fields.Datetime()
    duration = fields.Float(help="Duration in hours")

    # session computed fields
    end_date = fields.Datetime(compute='_compute_end_date', store=True)
    is_active = fields.Boolean(compute='_compute_is_active', store=True)
    display_name = fields.Char(compute='_compute_display_name', store=True) 
    # session relations
    course_id = fields.Many2one('openacademy.course', required=False)
    instructor_id = fields.Many2one('openacademy.partner',domain="[('is_instructor', '=', True)]") 
    attended_student_ids = fields.Many2many('openacademy.partner', string='Attended Students',domain="[('is_instructor', '=', False)]")
    room_id = fields.Many2one('openacademy.room')

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
            for rec in self :
                if rec.start_date and rec.duration:
                    rec.end_date = rec.start_date + timedelta(hours=rec.duration)
                else:
                    rec.end_date = None

    @api.depends('start_date', 'end_date')
    def _compute_is_active(self):
        now = fields.Datetime.now()
        for rec in self :
            if rec.start_date and rec.end_date:
                rec.is_active = rec.start_date <= now <= rec.end_date
            # else:
            #     rec.is_acive = False

    @api.depends('name' , 'course_id.name')
    def _compute_display_name(self):
            for rec in self:
                session_name = rec.name or "NullSession"
                course_name = rec.course_id.name or "NullCourse"

                rec.display_name = f"{session_name}-{course_name}"

    def action_confirm(self):
        for record in self:
            if not record.instructor_id or not record.course_id:
                raise ValidationError("Session must have an instructor and a course to be confirmed.")


            if record.room_id:
                validate_new_session(record.room_id, record)  # i pass the full room record (not just session_ids) assume in the future could be more validation (room state, available_date)
            record.state = 'confirmed'