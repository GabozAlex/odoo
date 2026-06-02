{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Real Estate/Brokerage',
    'summary': 'Manage property listings and offers',
    'description': """
        Real Estate Management Module
        =============================
        This module allows you to manage property listings,
        track offers, and handle real estate transactions.
    """,
    'depends': ['base'],
    'data': [
        'security/estate_security.xml',      
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        ],
    'demo': [],
    'installable': True,
    'application': True,  # Esto hace que aparezca como App
    'auto_install': False,
}