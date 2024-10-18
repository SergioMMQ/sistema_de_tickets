
# Sistema de Tickets - Odoo Module

## Descripción

El **Sistema de Tickets** es un módulo desarrollado para gestionar solicitudes, problemas y tareas mediante la creación y seguimiento de tickets. Este módulo permite la organización de los tickets por categorías, asignación a usuarios específicos, y seguimiento del estado a través de un flujo de trabajo definido. También proporciona un historial de actividades con soporte para imágenes, permitiendo un registro visual de la evolución de cada ticket.

## Características

- **Gestión de Tickets**: Creación y asignación de tickets para diferentes categorías.
- **Flujo de Trabajo de Estados**: Seguimiento de tickets a través de múltiples estados como "Nuevo", "En Progreso", "Resuelto", "Cerrado", etc.
- **Historial de Actividades**: Registro de actividades del ticket con la posibilidad de agregar mensajes e imágenes.
- **Categorías de Tickets**: Organización de tickets por categorías para una mejor clasificación.
- **Interfaz de Usuario Amigable**: Interfaces intuitivas para gestionar tickets y ver el historial de actividades.
- **Compatibilidad**: Compatible con Odoo 17.

## Instalación

### Requisitos Previos
- Odoo 17 instalado.
- Permisos para agregar módulos personalizados.

1. **Instalar el módulo**:
    - Busca "Sistema de Tickets" y haz clic en `Instalar`.
2. **Actualizar la lista de módulos**:
    - Ve al menú de aplicaciones en Odoo.
    - Haz clic en `Actualizar lista de aplicaciones`.

### Creación de un Ticket

1. Ve al menú **Sistema de Tickets** en Odoo.
2. Haz clic en `Crear`.
3. Llena el formulario con el asunto, descripción, categoría, y asigna el ticket a un usuario específico si es necesario.
4. Guarda el ticket para comenzar el seguimiento.

### Flujo de Estados

- Los tickets pueden ser movidos a través de diferentes estados:
    - **Nuevo**: El estado por defecto al crear un ticket.
    - **Pendiente**: Para tickets que requieren revisión antes de proceder.
    - **En Progreso**: Los tickets que están siendo trabajados activamente.
    - **En Revisión**: Tickets que están siendo revisados.
    - **Resuelto**: Tickets que han sido solucionados y esperan cierre.
    - **Cerrado**: Tickets completados y cerrados.
    - **Escalado**: Tickets que requieren atención especial.
    - **Cancelado**: Tickets que han sido cancelados.
    - **Reabierto**: Tickets que fueron cerrados pero que necesitan ser revisados de nuevo.

## Licencia
Este software se distribuye bajo la **Licencia LGPL (Lesser General Public License)**. Para más detalles, consulta el archivo [LICENSE](./LICENSE).

## Contacto
**Sergio Martínez Meneses**  
**Email:** [quetzal.mq97@gmail.com]  
**Website:** [https://sergiommq.github.io/portafolio/](https://sergiommq.github.io/portafolio/)

## Historial de Versiones
### Versión 1.0.0
- Lanzamiento inicial con las siguientes funcionalidades:
  - Gestión de tickets.
  - Flujo de trabajo de estados.
  - Historial de actividades con soporte para imágenes.


# -*- coding: utf-8 -*-
# © 2024 Sergio Martínez Meneses
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).