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
    
    <h2>Sistema de Tickets para Odoo 17</h2> <p>El <strong>Sistema de Tickets</strong> es una solución integral diseñada para optimizar la gestión de solicitudes, problemas y tareas en el ámbito tecnológico. Este módulo permite a los equipos de soporte técnico organizar, priorizar y resolver tickets de manera eficiente, mejorando la productividad y la satisfacción del usuario final.</p> <h3>Características Principales:</h3> <ul> <li><strong>Interfaz Intuitiva:</strong> Navega fácilmente por la plataforma con un diseño amigable que permite a los usuarios crear y gestionar tickets sin complicaciones.</li> <li><strong>Flujo de Trabajo Flexible:</strong> Adapta el flujo de trabajo a las necesidades de tu equipo, permitiendo una personalización en la asignación y seguimiento de tickets.</li> <li><strong>Categorización de Tickets:</strong> Clasifica las solicitudes según su naturaleza, facilitando la organización y el acceso a información relevante.</li> <li><strong>Asignación de Responsables:</strong> Distribuye tareas entre miembros del equipo de soporte, asegurando que cada ticket sea atendido por la persona adecuada.</li> <li><strong>Historial de Actividades:</strong> Mantén un registro detallado de todas las interacciones y acciones realizadas en cada ticket, lo que permite un seguimiento claro y efectivo.</li> </ul> <h3>Beneficios:</h3> <p>Implementar el <strong>Sistema de Tickets</strong> no solo mejora la eficiencia operativa, sino que también potencia la capacidad de respuesta ante incidencias, promoviendo un ambiente de trabajo más colaborativo y productivo.</p> <p>Con este módulo, las empresas pueden garantizar que cada solicitud sea tratada con la atención necesaria, mejorando la comunicación entre los usuarios y el equipo de soporte.</p>
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
