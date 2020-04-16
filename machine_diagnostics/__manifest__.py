{   # pylint: disable=C8101,C8103
    'name': "Prontuário de Notebooks",

    'summary': "Gerenciamento dos Prontuário de Notebooks",

    'description': "",
    'author': "Redmaxx",
    'website': "http://www.redmaxx.com.br",
    'category': '',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'contributors': [
        'Andrea Monicque dos Santos Silva <amonicquesantos@gmail.com>',
    ],
    'depends': ['base'],
    'data': [
        'views/notebook_diagnostics.xml',
        'views/diagnostic_records.xml',
        'views/agent_data.xml',
        'security/ir.model.access.csv'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
