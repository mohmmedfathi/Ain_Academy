from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta


class OpenAcademySession(models.Model):
    _name = 'openacademy.session'
    _description = 'Session'

    name = fields.Char(required=True)

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done')
        ],
        string='State',
        default='draft'
    )

    start_date = fields.Datetime(default=fields.Datetime.now)
    duration = fields.Float(string='Duration', help="Duration in hours")

    # Computed fields
    end_date = fields.Datetime(compute='_compute_end_date', string='End Date')
    is_active = fields.Boolean(
        compute='_compute_is_active',
        default=False,
        string='Is Active'
    )
    DisplayName = fields.Char(
        compute='_compute_Display_Name',
        string='Display Name'
    )

    # Relations
    course_id = fields.Many2one(
        comodel_name='openacademy.course',
        string='Course'
    )
    instructor_id = fields.Many2one(
        comodel_name='openacademy.partner',
        related='course_id.instructor_id',
        readonly=True,
        domain="[('is_instructor', '=', True)]",
        string='Instructor'
    )
    attended_student_ids = fields.Many2many(
        comodel_name='openacademy.partner',
        relation='openacademy_session_student_rel',
        column1='session_id',
        column2='student_id',
        string='Attended Students',
        domain="[('is_instructor', '=', False)]"
    )
    room_id = fields.Many2one(
        comodel_name='openacademy.room',
        ondelete='set null',
        string='Room'
    )

    # Compute methods
    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for rec in self:
            if rec.start_date and rec.duration:
                rec.end_date = rec.start_date + timedelta(hours=rec.duration)
            else:
                rec.end_date = None

    @api.depends('start_date', 'end_date')
    def _compute_is_active(self):
        now = fields.Datetime.now()
        for rec in self:
            rec.is_active = bool(rec.start_date and rec.end_date and rec.start_date <= now <= rec.end_date)

    @api.depends('name', 'course_id')
    def _compute_Display_Name(self):
        for rec in self:
            session_name = rec.name or "NullSession"
            course_name = rec.course_id.name or "NullCourse"
            rec.DisplayName = f"{session_name} - {course_name}"

    # Validation
    def validate_new_session(self, new_session):
        overlapping_sessions = self.env['openacademy.session'].search([
            ('room_id', '=', new_session.room_id.id),
            ('id', '!=', new_session.id),
            ('start_date', '<=', new_session.end_date),
            ('end_date', '>=', new_session.start_date),
        ])
        if overlapping_sessions:
            raise ValidationError("Room already reserved during this period.")

    # Actions
    def action_confirm(self):
        for rec in self:
            if not rec.instructor_id or not rec.course_id:
                raise ValidationError("Session must have an instructor and a course to be confirmed.")
            if rec.room_id:
                rec.validate_new_session(rec)
            rec.state = 'confirmed'
