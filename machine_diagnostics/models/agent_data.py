from odoo import fields, models, api


class AgentData(models.Model):
    _name = "agent.data"
    _description = "Dados do Agente"

    name = fields.Char(
        string="Número de Série",
        required=True)
    age_deviceid = fields.Char(
        string="ID Componente",
        required=True)
    age_attribute = fields.Char(
        string="Atributo",
        required=True)
    age_attribute_value = fields.Char(
        string="Valor Atributo",
        required=True)
    age_register_date = fields.Datetime(
        string="Data Cadastro",
        required=True)
    age_last_check = fields.Datetime(
        string="Última Verificação",
        required=True)

    @api.model
    def get_agent_data(self, payload):
        for attr in payload:
            domain = [
                ("name", "=", attr["name"]),
                ("age_deviceid", "=", attr["age_deviceid"]),
                ("age_attribute", "=", attr["age_attribute"]),
                ("age_attribute_value", "=", attr["age_attribute_value"]),
                ]
            register_line = self.search(domain, limit=1)

            # TODO: escrever no banco por CR
            if register_line:
                date = attr["age_last_check"]  # Verificar o formado da data
                register_line.sudo().write({"age_last_check": date})
            else:
                date_register = attr['age_register_date']
                date_last_check = attr['age_last_check']

                vals = {
                    'name': attr["name"],
                    'age_deviceid': attr['age_deviceid'],
                    'age_attribute': attr['age_attribute'],
                    'age_attribute_value': attr['age_attribute_value'],
                    'age_register_date': date_register,
                    'age_last_check': date_last_check,
                }
                self.sudo().create(vals)
        return True
