# -*- coding: utf-8 -*-
from odoo import fields, models

class User(models.Model):
    _name = 'user.user'
    _description = 'User'
    fName = fields.Char('First Name', required=True)
    lName = fields.Char('Last Name', required=True)
    
