# -*- coding: utf-8 -*-
from odoo import fields, models

class Module(models.Model):
    _name = 'module.program'
    _description = 'Module'
    name = fields.Char('Module name', required=True)
    code = fields.Char('Module code', required=True)
    
