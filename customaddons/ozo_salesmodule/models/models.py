# -*- coding: utf-8 -*-
from odoo import models, fields


# from odoo import models, fields, api


# create SaleSource Field in Database, with a field 'source' which will hold the Order Source Name
class database_saleSource(models.Model):
    _name = 'sale.source'
    _description = 'Sales Order Source'

    source = fields.Char(string='Source', required=False, ondelete='set null')

class ozo_salesmodule(models.Model):
    _inherit = 'sale.order'
    sources_id = fields.Many2one('sale.source', string='Source', ondelete='set null')


