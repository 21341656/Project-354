# -*- coding: utf-8 -*-
from odoo import fields, models

class Student(models.Model) :
    _name = 'student.user'
    _description = 'Student'
    _inherit = 'user.user'
    student_number = fields.Char('Student Number', required=True)
