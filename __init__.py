import requests

from odoo.tools.config import config

from . import models


def _init_city_data(env):
    """
    fill Indonesian city data which received from
    Rajaongkir API

    This method called on `post_init_hook` on module manifest
    """
    country_code_id = env['res.country'].search([('code', '=', 'ID')])
    city_data = env['res.city'].search([('country_id', '=', country_code_id.id)])

    if not city_data:
        api_key = config.get('rajaongkir_api_key')
        base_url = config.get('rajaongkir_base_url')
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
                'rajaongkir_city_id': city.get('city_id'),
                'city_type': city.get('type')
            }
            res_city_data.append(data)

        env['res.city'].create(res_city_data)
