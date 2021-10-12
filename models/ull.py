# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Ull(models.Model):
	_name = "ull"
	name = fields.Char(string="Nombre")
	detalle_ids = fields.One2many(
		comodel_name = 'ull.detalle',
		inverse_name = 'ull_id',
		string = 'Detalles',
	)

class UllDetalle(models.Model):
	_name="ull.detalle"
	ull_id = fields.Many2one(
		comodel_name = 'ull',
		string = "ULL"
	)
	name = fields.Many2one(
		comodel_name = "equipamiento",
		string = "Equipamiento"
	)
	name_es = fields.Char(string="Nombre",related='name.name_es')
	cantidad = fields.Integer(string="Cantidad",default="1")
	tipo = fields.Char(string="Tipo",related='name.tipo')
	sub_tipo = fields.Char(string="Sub-tipo",related='name.sub_tipo')
	tipo_arq = fields.Char(string="Tipo Arq",related='name.tipo_arq')
