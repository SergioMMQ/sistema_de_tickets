# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# © 2024 Sergio Martínez Meneses
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'Sistema de Tickets',
    'summary': 'Gestión de tickets para el área de sistemas',
    'author': 'Sergio Martinez Meneses',
    'website': 'https://sergiommq.github.io/portafolio/',
    'category': 'Herramientas',
    'version': '1.0.0',
    'description': """El Sistema de Tickets para Odoo 17 permite a las empresas gestionar solicitudes, problemas y tareas de manera organizada y eficiente. Con una interfaz intuitiva, flujo de trabajo flexible y seguimiento de actividades detallado, este módulo es la solución ideal para equipos técnicos y de soporte. Categoriza, asigna y resuelve tickets rápidamente, mejorando la productividad y garantizando un historial claro de todas las interacciones.""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ticket_views.xml',
        'views/ticket_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],  
    'price': 90,
    'currency': 'USD',
    'support': 'quetzal.mq97@gmail.com',
}
