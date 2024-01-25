import re

from odoo import api, models, fields
from odoo.exceptions import ValidationError


class Person(models.Model):
    _name = 'hr_hospital.person'
    _description = 'Abstract model for person'

    full_name = fields.Char(string='Full name', required=True)
    phone = fields.Char(
        string='Phone number',
        help='Enter a valid phone number (e.g., +1234567890)'
    )
    email = fields.Char()
    photo = fields.Binary()
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ],
    default='male'
    )

    _sql_constraints = [
        (
            'check_valid_phone',
            'CHECK (phone IS NULL OR (LENGTH(phone) >= 10 AND LENGTH(phone) <= 15))',
            'Phone number should be between 10 and 15 characters.'
        ),
    ]

    @api.constrains('phone')
    def _check_valid_phone(self):
        for record in self:
            if record.phone:
                if not re.match(r'^\+?[0-9]+$', record.phone):
                    raise ValidationError(
                        'Invalid phone number. Please use only digits and an optional leading +.'
                    )
