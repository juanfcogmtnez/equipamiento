# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Sub_ull_2(models.Model):
	_name = "sub_ull_2"
	name = fields.Char(string="Nombre")
	descripcion = fields.Text()
	active = fields.Boolean(string="Activo",default="1")	
	equipamiento_sub_ull_2_ids = fields.Many2many(
		comodel_name='equipamiento',
		inverse_name = 'sub_ull_2_ids',
		string = "Equipamiento",
	)
