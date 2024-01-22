from odoo import models, fields


class SampleType(models.Model):
    _name = 'hr_hospital.sample_type'

    name = fields.Char()
