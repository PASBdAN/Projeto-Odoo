{   # pylint: disable=C8101,C8103
    'name': "Catálogo do Equipamento",

    'summary': "Gerenciamento da Modelos de Notebooks",

    'description': "",
    'author': "Redmaxx",
    'website': "http://www.redmaxx.com.br",
    'category': 'stock',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'contributors': [
        'Andrea Monicque dos Santos Silva'
    ],
    'depends': ['stock'],
    'data': [
        'views/catalogo_equipamento.xml',
        'security/ir.model.access.csv'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
