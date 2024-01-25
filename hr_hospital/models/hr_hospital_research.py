from odoo import models, fields


class Research(models.Model):
    _name = 'hr_hospital.research'

    patient = fields.Many2one('hr_hospital.patient', string='Patient')
    research_type = fields.Many2one('hr_hospital.research.type')
    doctor = fields.Many2one('hr_hospital.doctor')
    sample = fields.Many2one('hr_hospital.sample')
    conclusions = fields.Text()
    appointment_ids = fields.Many2many('hr_hospital.appointment')
    diagnosis_ids = fields.Many2many('hr_hospital.diagnosis')
