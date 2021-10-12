# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Ull(models.Model):
	_name = "ull"
	name = fields.Char(string="Nombre")
	equipamiento = fields.Many2one(
		comodel_name = "equipamiento",
		string = "Equipamiento"
	)
	
	active = fields.Boolean(string = 'Activo',default=True)
	equipamiento_es = fields.Char(string="Nombre",related='equipamiento.name_es')
	cantidad = fields.Integer(string="Cantidad",default="1")
	ull_ids = fields.Char(string="ULL", related='equipamiento.ull_ids')
	tipo = fields.Char(string="Tipo",related='equipamiento.tipo')
	sub_tipo = fields.Char(string="Sub-tipo",related='equipamiento.sub_tipo')
	tipo_arq = fields.Char(string="Tipo Arq",related='equipamiento.tipo_arq')
