from odoo import fields, models

class Lecturer(models.Model):
    _name = 'lecturer.user'
    _description = 'Lecturer'
    _inherit = 'staff.user'
