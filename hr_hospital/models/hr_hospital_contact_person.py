from odoo import fields, models


class ContactPerson(models.Model):
    _name = 'hr_hospital.contact_person'
    _inherit = 'hr_hospital.person'

    full_name = fields.Char(string='Contact person name', required=True)

