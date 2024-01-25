from datetime import datetime

from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hr_hospital.patient'

    _inherit = 'hr_hospital.person'

    full_name = fields.Char(string='Patient name', required=True)
    birth_date = fields.Date(string='Date of Birth', required=True)
    age = fields.Integer(compute='_compute_age', store=True, readonly=True)
    passport_data = fields.Char(string='Passport Data')
    contact_person = fields.Many2one('hr_hospital.contact_person', string='Contact Person')

    @api.depends('birth_date')
    def _compute_age(self):
        for patient in self:
            if patient.birth_date:
                today = datetime.now().date()
                birth_date = fields.Date.from_string(patient.birth_date)
                age = today.year - birth_date.year
                if (today.month < birth_date.month) or (today.month == birth_date.month and today.day < birth_date.day):
                    age -= 1
                patient.age = age
            else:
                patient.age = 0
