from odoo import models, fields


class DiseaseType(models.Model):
    _name = 'hr_hospital.disease.type'

    name = fields.Char(string='Disease Type Name')
    parent_id = fields.Many2one('hr_hospital.disease.type', string='Parent Disease Type')
    child_ids = fields.One2many('hr_hospital.disease.type', 'parent_id', string='Child Disease Types')
