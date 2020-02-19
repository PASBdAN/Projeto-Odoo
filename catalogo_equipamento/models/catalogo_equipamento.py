# © 2019 Andrea Monicque, Redmaxx
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class CatalogoEquipamento(models.Model):
    _name = "catalogo.equipamento"
    _description = "Catálogo do Equipamento"

    name = fields.Char(
        string="Modelo")

    componente_line_ids = fields.One2many(          #nome do campo que aparece na tela (modo programador)- tipo de relação com a classe de baixo
        string="Componentes",                        #nome da string que aparece para o usuário
        comodel_name="catalogo.componente.line",    #nome do objeto da classe
        inverse_name="catalogo_id")                 #nome do campo que faz relação da subclasse(DeclaracaoProductLines) com a Classe global (CatalogoEquipamento)


class CatalogoComponenteLines(models.Model):
    _name = "catalogo.componente.line"

    catalogo_id = fields.Many2one(                  #relação que é feita para conversar com a classe global
        string="Catálogo",
        comodel_name="catalogo.equipamento")        #relaciona com o objeto da classe mae (CatalogoEquipamento)

    componente_id = fields.Many2one(                #relação que é feita para conversar com o objeto que está fora da classe, na classe global
        string="Componente",
        comodel_name="product.attribute",             #aqui que é feito o relacionamento com o campo do outro módulo que está alimentando esse campo
        ondelete="restrict")

    propriedade_id = fields.Char(                #relação que é feita para conversar com o objeto que está fora da classe, na classe global
        string="Propriedade")

    descricao_id = fields.Many2one(                #relação que é feita para conversar com o objeto que está fora da classe, na classe global
        string="Descrição",
        comodel_name="product.attribute.value",            #aqui que é feito o relacionamento com o campo do outro módulo que está alimentando esse campo
        ondelete="restrict")

    @api.onchange("componente_id")
    def _onchange_componente_id(self):
        self.name = self.componente_id.name
