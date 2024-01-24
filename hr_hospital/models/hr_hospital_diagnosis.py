from odoo import models, fields


class Diagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'

    doctor = fields.Many2one('hr_hospital.doctor')
    patient = fields.Many2one('hr_hospital.patient')
    disease = fields.Many2one('hr_hospital.disease')
    treatment = fields.Text(string='Prescribed Treatment')
    diagnosis_date = fields.Date(string='Diagnosis Date')
    