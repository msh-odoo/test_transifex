# -*- coding: utf-8 -*-

from openerp import models, fields, api

class test_transifex_odoo_module_po(models.Model):
    _name = 'test_transifex_odoo_module_po.test_transifex_odoo_module_po'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    amount = fields.Float(string="Amount")

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100