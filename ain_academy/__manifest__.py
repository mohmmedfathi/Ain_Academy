# -*- coding: utf-8 -*-
{
    'name': "Ain_Academy",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/room_reservation_wizard_view.xml',
        'wizards/room_unreservation_wizard_view.xml',
        'views/ain_academy_parent_menu.xml',
        'views/partner.xml',
        'views/course.xml',
        'views/session.xml',
        'views/room.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

