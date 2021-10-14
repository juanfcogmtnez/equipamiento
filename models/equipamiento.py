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
	datasheet_en = fields.Binary(string="Datasheet")
	datasheet_filename_en = fields.Char(string="File name")
	car_alto = fields.Float(string="Alto(cm)")
	car_ancho = fields.Float(string="Ancho(cm)")
	car_largo = fields.Float(string="Largo(cm)")
	car_peso = fields.Float(string="Peso(kg)")
	superficie = fields.Float(string="Superficie (cm2)",compute="_sup_basic",stored=True)
	@api.onchange('car_ancho','car_largo')
	def _sup_basic(self):
		cm_superficie = self.car_ancho * self.car_largo
		self.superficie = cm_superficie/10000
	ubicacion = fields.Selection(selection=[
	('suelo','suelo'),
	('mural','mural'),
	('sobremesa','sobremesa'),
	],
	string = 'Ubicación predeterminada'
	)
	movilidad = fields.Boolean(string="¿Tiene el equipo una ubicación fija?", default=True)
	fijacion = fields.Boolean(string="¿Necesita el equipo alguna fijación especial?", default=False)
	estructura = fields.Boolean(string="¿Necesita el equipamiento de cambios constructivos en la estructura?", default=False)
	conex_agua = fields.Boolean(string="¿Necesita el equipo conexión a circuito de agua corriente?", default=False)
	conex_tta = fields.Boolean(string="¿Necesita el equipo conexión a circuito de agua especial?", default=False)
	conex_elect = fields.Boolean(string="¿Necesita el equipo conexión a circuito eléctrico corriente?", default=False)
 	#conex_ups = fields.Boolean(string="¿Necesita el equipo conexión a circuito eléctrico de emergencia?", default=False)
	conex_com = fields.Boolean(string="¿Necesita el equipo conexión a red de comunicaciones?", default=False)
	conex_ups = fields.Boolean(string="¿Necesita el equipo conexión a circuito eléctrico de emergencia?", default=False)
