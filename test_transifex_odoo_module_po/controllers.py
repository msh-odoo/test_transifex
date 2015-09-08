# -*- coding: utf-8 -*-
from openerp import http

# class TestTransifexOdooModulePo(http.Controller):
#     @http.route('/test_transifex_odoo_module_po/test_transifex_odoo_module_po/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_transifex_odoo_module_po/test_transifex_odoo_module_po/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_transifex_odoo_module_po.listing', {
#             'root': '/test_transifex_odoo_module_po/test_transifex_odoo_module_po',
#             'objects': http.request.env['test_transifex_odoo_module_po.test_transifex_odoo_module_po'].search([]),
#         })

#     @http.route('/test_transifex_odoo_module_po/test_transifex_odoo_module_po/objects/<model("test_transifex_odoo_module_po.test_transifex_odoo_module_po"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_transifex_odoo_module_po.object', {
#             'object': obj
#         })