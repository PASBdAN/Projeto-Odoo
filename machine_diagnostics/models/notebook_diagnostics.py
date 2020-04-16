
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


class DiagnosticsRecordsLines(models.Model):
    _name = "diagnostics.records.line"

    diagnostics_id = fields.Many2one(
        string="Diagnostics",
        comodel_name="notebook.diagnostics")

    notediag_records_id = fields.Many2one(
        string="Registros",
        comodel_name="diagnostic.records",
        ondelete="restrict")


    @api.onchange("notediag_records_id")
    def _onchange_notediag_records_id(self):
        self.name = self.notediag_records_id.name
