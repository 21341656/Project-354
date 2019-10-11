from odoo import fields, models

class Result(models.Model):
    _name = 'result.module'
    _description = 'Result'
    value = fields.Char('Result Value', required=True)
