from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Appointment(models.Model):
    _name = 'hr_hospital.appointment'

    doctor = fields.Many2one('hr_hospital.doctor')
    patient = fields.Many2one('hr_hospital.patient')
    appointment_datetime = fields.Datetime()
    diagnosis = fields.Many2one('hr_hospital.disease')
    recommendations = fields.Text()
    research_ids = fields.Many2many('hr_hospital.research')
    is_completed = fields.Boolean()
    schedule_hour = fields.Float()

    _sql_constraints = [
        (
            'unique_doctor_patient_datetime',
            'unique(doctor, patient, appointment_date, appointment_time)',
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
                appointment.write({'appointment_date': appointment.appointment_date, 'appointment_time': appointment.appointment_time, 'doctor': appointment.doctor.id})

    @api.constrains('diagnosis')
    def _check_diagnosis_appointment(self):
        for appointment in self:
            if appointment.diagnosis:
                raise ValidationError("Cannot delete or archive appointments with diagnoses.")