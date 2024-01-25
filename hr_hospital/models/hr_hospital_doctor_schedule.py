from odoo import models, fields


class DoctorSchedule(models.Model):
    _name = 'hr_hospital.doctor_schedule'

    doctor = fields.Many2one('hr_hospital.doctor')
    date = fields.Date()
    appointment = fields.One2many("hr_hospital.appointment", "doctor_schedule")
    appointment_datetime = fields.Datetime(related="appointment.appointment_datetime")

    _sql_constraints = [
        (
            'unique_doctor_appointment_datetime',
            'unique(doctor, appointment_datetime)',
            'Doctor has already an appointment for this time.'
        ),
    ]
