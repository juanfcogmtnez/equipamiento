# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Ull(models.Model):
	_name = "ull"
	name = fields.Char(string="Nombre")
	descripcion = fields.Text()
	active = fields.Boolean(string="Activo",default="1")	
	equipamiento_ids = fields.Many2many(
		comodel_name='equipamiento',
		inverse_name = 'name',
		string = "Equipamiento",
		)
