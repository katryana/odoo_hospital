from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hr_hospital.patient'

    _inherit = 'hr_hospital.person'

    birth_date = fields.Date(string='Date of Birth')
    age = fields.Integer(compute='_compute_age')
    passport_data = fields.Char(string='Passport Data')
    contact_person = fields.Many2one('hr_hospital.person', string='Contact Person')

    @api.depends('birth_date')
    def _compute_age(self):
        for patient in self:
            if patient.birth_date:
                today = fields.Date.today()
                patient.age = today.year - patient.birth_date.year - (
                            (today.month, today.day) < (patient.birth_date.month, patient.birth_date.day))
            else:
                patient.age = 0
