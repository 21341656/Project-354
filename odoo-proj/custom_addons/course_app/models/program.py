# -*- coding: utf-8 -*-
from odoo import fields, models

class Program(models.Model):
    _name = 'program.course'
    _description = 'Program'
    name = fields.Char('Program name', required=True)
    code = fields.Char('Program code', required=True)
    short_code = fields.Char('Shortened form', required=True)
