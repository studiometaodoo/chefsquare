# -*- encoding: utf-8 -*-
{
    'name': 'link_event_to_sale_order',
    'summary': 'Link events with respective sale order',
    'description': """
       Automatically Change the status of event that has been created from an SO 
       at the confirmation of the SO and on the cancellation of the SO
    """,
    'author': "Odoo S.A.",
    'website': "http://www.odoo.com",
    'version': '1.0',
    'category': 'Customisation',

    'depends': ['base', 'event_sale', 'sale'],
    'data': [
        'views/sale_order.xml',
    ],
}