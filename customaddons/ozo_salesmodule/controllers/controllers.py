# -*- coding: utf-8 -*-
# from odoo import http


# class OzoSalesmodule(http.Controller):
#     @http.route('/ozo_salesmodule/ozo_salesmodule', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ozo_salesmodule/ozo_salesmodule/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ozo_salesmodule.listing', {
#             'root': '/ozo_salesmodule/ozo_salesmodule',
#             'objects': http.request.env['ozo_salesmodule.ozo_salesmodule'].search([]),
#         })

#     @http.route('/ozo_salesmodule/ozo_salesmodule/objects/<model("ozo_salesmodule.ozo_salesmodule"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ozo_salesmodule.object', {
#             'object': obj
#         })

