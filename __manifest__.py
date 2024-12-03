# -*- coding: utf-8 -*-
{
    'name': 'Rajaongkir Odoo',
    'author': 'Abdullah Amin Firdaus',
    'category': 'General',
    'description': """
    This is module to get courier cost in Indonesia which its data provided by Rajaongkir
    """,
    'depends': [
        'base',
        'base_address_extended',
        'mail'
    ],
    'post_init_hook': '_init_city_data'
}