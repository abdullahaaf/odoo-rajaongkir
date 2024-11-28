from odoo import fields, models

class ResCity(models.Model):
    _inherit = 'res.city'
    _rec_names_search = ['name', 'zipcode', 'province_name']

    rajaongkir_city_id = fields.Integer(string='Rajaongkir City ID', help='Store City ID received from rajaongkir')
    province_name = fields.Char(string='Province Name')
    city_type = fields.Char(string='City Type', help='City type received from rajaongkir, Kabupaten/Kota')

    def name_get(self):
        res = []
        for city in self:
            name = f'{city.city_type} {city.name} - {city.province_name} ({city.zipcode})'
            res.append((city.id, name))
        return res