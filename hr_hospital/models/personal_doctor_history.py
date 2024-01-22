from odoo import models, fields, api


class PersonalDoctorHistory(models.Model):
    _name = 'hr_hospital.personal_doctor_history'

    patient = fields.Many2one('hr_hospital.patient')
    doctor = fields.Many2one('hr_hospital.doctor')
    assignment_date = fields.Date()

    @api.onchange('personal_doctor')
    def _onchange_personal_doctor(self):
        for record in self:
            if record.doctor:
                record.assignment_date = fields.Date.today()
