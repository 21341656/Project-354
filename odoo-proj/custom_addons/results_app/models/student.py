from odoo import fields, models

class Student(models.Model):
    _name = 'student.user'
    _description = 'Student'
    _inherit = 'student.user'
