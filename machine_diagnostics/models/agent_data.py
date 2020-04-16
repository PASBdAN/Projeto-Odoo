
from odoo import api, fields, models


class AgentData(models.Model):
    _name = "agent.data"
    _description = "Dados do Agente"

    name = fields.Char(
        string="Número de Série", )
    age_attribute = fields.Char(
        string="Atributo", )
    age_value = fields.Char(
        string="Valor", )

    age_last_change = fields.Datetime(
        string="Última Alteração")
    age_last_check = fields.Datetime(
        string="Última Verificação", )
