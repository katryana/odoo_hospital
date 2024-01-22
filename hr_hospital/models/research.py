from odoo import models, fields


class Research(models.Model):
    _name = 'hr_hospital.research'

    patient_id = fields.Many2one('hr_hospital.patient', string='Patient')
    research_type = fields.Many2one('hr_hospital.research.type')
    assigning_doctor = fields.Many2one('hr_hospital.doctor')
    sample = fields.Many2one('hr_hospital.sample_type')
    conclusions = fields.Text()
    appointment_ids = fields.Many2many('hr_hospital.appointment')
    diagnosis_ids = fields.Many2many('your_module.diagnosis')
