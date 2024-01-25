from odoo import models, fields


class Sample(models.Model):
    _name = 'hr_hospital.sample'

    name = fields.Char()
