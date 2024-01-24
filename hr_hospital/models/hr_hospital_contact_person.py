from odoo import models


class ContactPerson(models.Model):
    _name = 'hr_hospital.contact_person'

    _inherit = 'hr_hospital.person'
