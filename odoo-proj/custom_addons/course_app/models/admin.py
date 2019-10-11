# -*- coding: utf-8 -*-
from odoo import fields, models

class Admin(models.Model) :
    _name = 'admin.user'
    _description = 'Admin'
    _inherit = 'staff.user'
    
