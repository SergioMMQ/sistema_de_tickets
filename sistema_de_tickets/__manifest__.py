# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# © 2024 Sergio Martínez Meneses
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'Sistema de Tickets',
    'summary': 'Gestión de tickets para el área de sistemas',
    'author': 'Sergio Martinez Meneses',
    'website': 'https://sergiommq.github.io/portafolio/',
    'category': 'Soporte Técnico',
    'version': '1.0.0',
    'description': """
    <p><strong>Sistema de Tickets para Odoo 17</strong></p>
    <p>El Sistema de Tickets es una solución completa para gestionar solicitudes, problemas y tareas de manera organizada y eficiente. Con una interfaz intuitiva y un flujo de trabajo flexible, este módulo permite:</p>
    <ul>
        <li>Categorizar, asignar y gestionar tickets de soporte técnico.</li>
        <li>Seguir el progreso de cada ticket desde su creación hasta la resolución.</li>
        <li>Mantener un historial detallado de actividades para cada ticket.</li>
    </ul>
    <p>Ideal para equipos técnicos y de soporte, mejora la productividad al centralizar la gestión de tareas en un solo lugar. ¡Optimiza tu flujo de trabajo y garantiza una atención rápida y eficaz!</p>
    """,
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
