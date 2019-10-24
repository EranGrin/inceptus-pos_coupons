# -*- coding: utf-8 -*-
# Part of Inceptus ERP Solutions Pvt.ltd.
# See LICENSE file for copyright and licensing details.

{
    'name': "POS Coupons",

    'summary': """
        Manage Coupons on POS""",

    'description': """
        Manage Coupons on POS
    """,

    'author': "Inceptus.io",
    'website': "http://www.inceptus.io",
    'category': '',
    'version': '1.0',

    'depends': ['ies_base_redeem', 'ies_base'],

    'data': [
        'views/coupon_view.xml',
        'views/pos_view.xml',
    ],

    'qweb': ['static/src/xml/*.xml'],

    'installable': True,
    'auto_install': False,
    'application': True,
}
