# -*- coding: utf-8 -*-
# © 2024 Sergio Martínez Meneses
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

from odoo import models, fields, api
from odoo.exceptions import UserError

class TicketSystem(models.Model):
    _name = 'ticket.system'
    _description = 'Sistema de Tickets'

    name = fields.Char(string='Asunto', required=True)
    description = fields.Text(string='Descripción', required=True)
    category_id = fields.Many2one('ticket.category', string='Categoría', required=True)
    user_id = fields.Many2one('res.users', string='Asignado a', default=lambda self: self.env.user)
    history_ids = fields.One2many('ticket.history', 'ticket_id', string='Historial')
    state = fields.Selection([
    ('new', 'Nuevo'),
    ('pending', 'Pendiente'),
    ('in_progress', 'En Progreso'),
    ('under_review', 'En Revisión'),
    ('resolved', 'Resuelto'),
    ('closed', 'Cerrado'),
    ('escalated', 'Escalado'),
    ('cancelled', 'Cancelado'),
    ('reopened', 'Reabierto'),
    ], string='Estado', default='new')
    
    def action_progress(self):
        self.write({'state': 'in_progress'})

    def action_close(self):
        self.write({'state': 'closed'})

class TicketCategory(models.Model):
    _name = 'ticket.category'
    _description = 'Categoría de Ticket'
    
    name = fields.Char(string='Nombre', required=True)

class TicketHistory(models.Model):
    _name = 'ticket.history'
    _description = 'Historial de Actividad del Ticket'
    
    ticket_id = fields.Many2one('ticket.system', string='Ticket', required=True)
    message = fields.Text(string='Mensaje')
    create_date = fields.Datetime(string='Fecha', default=fields.Datetime.now)
    image = fields.Binary(string='Imagen')
