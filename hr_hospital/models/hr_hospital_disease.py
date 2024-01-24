from odoo import models, fields


class Disease(models.Model):
    _name = 'hr_hospital.disease'
    _description = 'Reference of diseases'

    name = fields.Char()
    description = fields.Text()
