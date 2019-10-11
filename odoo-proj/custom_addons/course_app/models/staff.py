# -*- coding: utf-8 -*-
from odoo import fields, models

class Staff(models.Model):
    _name = 'staff.user'
    _description = 'Staff'
    _inherit = 'user.user'
    staff_number = fields.Char('Staff Number', required=True)
    office_number = fields.Char('Office Number')
