# -*- encoding: utf-8 -*-
{
    'name': 'waiting_attendees_on_event',
    'summary': 'Extra attendees in waiting status',
    'description': """
       Put extra attendees on a 'inactive' status when the limit is reached and notify by mail'inactive' attendees when 
       a confirmed attendee is cancelled.
    """,
    'author': "Odoo S.A.",
    'website': "http://www.odoo.com",
    'version': '1.0',
    'category': 'Customisation',

    'depends': ['base', 'event', 'event_sale',],
    'data': [
        'views/event.xml',
        'data/waiting_attendees_mail_template.xml',
    ],
}