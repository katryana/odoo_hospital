from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Appointment(models.Model):
    _name = 'hr_hospital.appointment'

    doctor = fields.Many2one('hr_hospital.doctor')
    doctor_schedule = fields.Many2one('hr_hospital.doctor_schedule')
    patient = fields.Many2one('hr_hospital.patient')
    appointment_datetime = fields.Datetime()
    diagnosis = fields.Many2one('hr_hospital.diagnosis')
    recommendations = fields.Text()
    research_ids = fields.Many2many('hr_hospital.research')
    is_completed = fields.Boolean()

    _sql_constraints = [
        (
            'unique_doctor_patient_datetime',
            'unique(doctor, patient, appointment_datetime)',
            'A patient cannot have multiple appointments with the same doctor at the same date and time.'
        ),
        (
            'completed_appointment_no_changes',
            'CHECK(is_completed = False)',
            'Cannot modify completed appointments.'
        ),
    ]

    @api.constrains('is_completed')
    def _check_completed_appointment(self):
        for appointment in self:
            if appointment.is_completed:
                appointment.write(
                    {
                        'appointment_datetime': appointment.appointment_datetime,
                        'doctor': appointment.doctor.id
                    }
                )

    @api.constrains('diagnosis')
    def _check_diagnosis_appointment(self):
        for appointment in self:
            if appointment.diagnosis:
                raise ValidationError(
                    'Cannot delete or archive appointments with diagnoses.'
                )