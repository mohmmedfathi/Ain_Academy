# -*- coding: utf-8 -*-
# from odoo import http


# class AinAcademy(http.Controller):
#     @http.route('/ain__academy/ain__academy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ain__academy/ain__academy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ain__academy.listing', {
#             'root': '/ain__academy/ain__academy',
#             'objects': http.request.env['ain__academy.ain__academy'].search([]),
#         })

#     @http.route('/ain__academy/ain__academy/objects/<model("ain__academy.ain__academy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ain__academy.object', {
#             'object': obj
#         })

