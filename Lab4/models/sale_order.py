from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    deliveryman = fields.Many2one('res.users', string='Deliveryman')
    description = fields.Text(string='Description')
