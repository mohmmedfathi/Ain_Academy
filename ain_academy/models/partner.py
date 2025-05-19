from odoo import models, fields, api


class OpenAcademyPartner(models.Model):
    _name = 'openacademy.partner'
    _description = 'partner'
    
    name = fields.Char(required=True,string = 'partner name')
    age = fields.Integer(string = 'partner age')
    is_instructor = fields.Boolean()
    attended_session_ids = fields.Many2many('openacademy.session',string = 'Attended Sessions')
    image_1920 = fields.Image(string="Profile Image")
  
    
    