
from odoo import api, fields, models


class DiagnosticRecords(models.Model):
    _name = "diagnostic_records"
    _description = "Registros de Prontuário"


        name= fields.Char(
            string="Id Componente", )
        diagrec_component = fields.Char(
            string="Componente", )
        diagrec_property = fields.Char(
            string="Propriedade", )
        diagrec_description = fields.Char(
            string="Descrição", )

        diagrec_last_change = fields.Datetime(string="Última Alteração")
        diagrec_last_check = fields.Datetime(string="Última Verificação", )



    diagrec_serial_number = fields.Many2one(
        string="Número de Série",
        comodel_name="notebook.diagnostics",
        ondelete="restrict")

    diagrec_product = fields.Many2one(
        string="Produto",
        comodel_name="product.product",
        domain="[('name', 'like', notebook)]",
        ondelete="set null")
