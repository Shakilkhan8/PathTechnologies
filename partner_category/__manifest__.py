{
    'name': "Partner Category",

    'summary': """This module is used to create partner category""",

    'description': """
        In this module we creating partner category
    """,

    'author': "SK Technology",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/users.xml',
    ],

}
