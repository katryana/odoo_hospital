from odoo import models, fields


class Person(models.AbstractModel):
    _name = 'hr_hospital.person'
    _description = 'Abstract model for person'

    full_name = fields.Char(string='Full name')
    phone = fields.Char()
    email = fields.Char()
    photo = fields.Binary()
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ])
