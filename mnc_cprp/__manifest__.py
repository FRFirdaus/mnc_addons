# -*- coding: utf-8 -*-
{
    'name': 'MNC CPRP',
    'summary': 'MNC CPRP.',

    'author': 'Fahmi Roihanul Firdaus & Najib Arif',
    'website': 'https://www.linkedin.com/in/mnajibarif/',
    'description': '''Features:

* CPRP Reporting''',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'base', 'purchase'],

    # always loaded
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/advertise_views.xml',
        'views/agency_views.xml',
        'views/brand_views.xml',
        'views/report_views.xml',
        'views/media_views.xml',
        'views/menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],

    # license and application info
    'license': 'AGPL-3',
}
