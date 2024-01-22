from odoo import models, fields


class ResearchType(models.Model):
    _name = 'hr_hospital.research.type'

    name = fields.Char()
    parent_id = fields.Many2one('hr_hospital.research.type', string='Parent Research Type')
    child_ids = fields.One2many('hr_hospital.research.type', 'parent_id', string='Child Research Types')
