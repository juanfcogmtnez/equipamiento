# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Equipamiento(models.Model):
	_name = "equipamiento"
	_inherit = ['image.mixin']
	name = fields.Char(string='Equipo')
	name_es = fields.Char(string='Equipo')
	name_fr = fields.Char(string='Équipement')
	name_en = fields.Char(string='Equipment')
	active = fields.Boolean(string = 'Activo',default=True)
	ull_ids = fields.Many2many(
		comodel_name='ull',
		string = 'ULL'
	)
	descripcion = fields.Text(string='Descripción')
	es_datasheet = fields.Boolean(string = 'Ficha técnica')
	datasheet = fields.Binary(string="Ficha técnica")
	datasheet_filename = fields.Char(string="Nombre de archivo")
