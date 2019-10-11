from odoo import fields, models

class Module(models.Model):
    _name = 'module.program'
    _description = 'Module'
    _inherit = 'module.program'
