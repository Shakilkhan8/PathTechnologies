# -*- coding: utf-8 -*-
{
    'name': "Sale Order Changes",

    'summary': """this module is related sale order changes based on customer category""",

    'description': """
        In this module we are using customer category to group by sale orders 
        by country, province , city and regions
    """,

    'author': "SK Technology",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'partner_category', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

}
