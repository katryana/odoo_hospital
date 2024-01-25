from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _inherit = 'hr_hospital.person'

    specialty = fields.Char()
    is_intern = fields.Boolean()
    mentor_id = fields.Many2one('hr_hospital.doctor', domain="[('is_intern', '=', False)]")

    @api.constrains('is_intern', 'mentor_id')
    def _check_intern_mentor(self):
        for doctor in self:
            if doctor.is_intern and not doctor.mentor_id:
                raise ValidationError("Interns must have mentors.")
