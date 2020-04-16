
from odoo import api, fields, models



class NotebookDiagnostics(models.Model):
    _name = "notebook.diagnostics"
    _description = "Prontuário de Notebooks"

    name = fields.Char(
        string="Número de Série", )

    notediag_records_line_ids = fields.One2many(
        string="Registros",
        comodel_name="diagnostics.records.line",
        inverse_name="diagnostics_id")
