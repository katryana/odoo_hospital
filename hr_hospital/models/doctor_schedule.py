from odoo import models, fields


class DoctorSchedule(models.Model):
    _name = 'hr_hospital.doctor_schedule'

    doctor_id = fields.Many2one('hr_hospital.doctor')
    date = fields.Date()
    appointment_hours = fields.One2many('hr_hospital.appointment_datetime', 'schedule_id')

    _sql_constraints = [
        ('unique_doctor_date', 'unique(doctor, date)', 'Doctor can have only one schedule per day.'),
    ]
