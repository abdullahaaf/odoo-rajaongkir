from odoo import fields, models

class ResCity(models.Model):
    _inherit = 'res.city'

    rajaongkir_city_id = fields.Integer(string='Rajaongkir City ID', help='Store City ID received from rajaongkir')
    province_name = fields.Char(string='Province Name')