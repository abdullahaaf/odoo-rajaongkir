import os, requests

from odoo import api, SUPERUSER_ID

from . import models


def create_city_data(cr, registry):
    """
    fill Indonesian city data which received from
    Rajaongkir API

    This method called on `post_init_hook` on module manifest
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    country_code_id = env['res.country'].search([('code', '=', 'ID')])
    city_data = env['res.city'].search([('country_id', '=', country_code_id.id)])

    if not city_data:
        api_key = os.getenv('API_KEY')
        base_url = os.getenv('BASE_URL')
        headers = {'key': api_key}
        list_city_endpoint = f'{base_url}/city'

        result_city = requests.get(list_city_endpoint, headers=headers).json()

        city_data = result_city.get('rajaongkir').get('results')

        res_city_data = []
        for city in city_data:
            data = {
                'country_id': country_code_id.id,
                'zipcode': city.get('postal_code'),
                'name': city.get('city_name'),
                'province_name': city.get('province'),
                'rajaongkir_city_id': city.get('city_id')
            }
            res_city_data.append(data)

        env['res.city'].create(res_city_data)
