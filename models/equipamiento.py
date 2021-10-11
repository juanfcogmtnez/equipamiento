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
	sub_ull_ids = fields.Many2many(
		comodel_name='sub_ull',
		string = 'Sub-ULL'
	)
	sub_ull_2_ids = fields.Many2many(
		comodel_name='sub_ull_2',
		string = 'Sub-ULL-2'
	)
	item_code = fields.Char(string="item-code")
	
	descripcion_es = fields.Text(string='Descripción')
	descripcion_fr = fields.Text(string='Description')
	descripcion_en = fields.Text(string='Description')
	tipo = fields.Char(string="Tipo")
	sub_tipo = fields.Char(string="Sub-tipo")
	tipo_arq = fields.Char(string="Tipo arquitéctonico")
	es_datasheet_es = fields.Boolean(string = 'Ficha técnica')
	datasheet_es = fields.Binary(string="Ficha técnica")
	datasheet_filename_es = fields.Char(string="Nombre de archivo")
	es_datasheet_fr = fields.Boolean(string = 'Fiche technique')
	datasheet_fr = fields.Binary(string="Fiche technique")
	datasheet_filename_fr = fields.Char(string="Nom du fichier")
	es_datasheet_en = fields.Boolean(string = 'Datasheet')
	datasheet_fr = fields.Binary(string="Datasheet")
	datasheet_filename_fr = fields.Char(string="File name")
