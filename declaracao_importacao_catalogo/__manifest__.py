{   # pylint: disable=C8101,C8103
    'name': "Importação DI",

    'summary': "Gerenciamento da Declaração de Importação (DI)",

    'description': "",
    'author': "Trustcode",
    'website': "http://www.trustcode.com.br",
    'category': 'purchase',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'contributors': [
        'Mackilem Van der Laan <mack.vdl@gmail.com>',
        'Andrea Monicque dos Santos Silva'
    ],
    'depends': ['purchase','stock'],
    'data': [
        'views/catalogo_equipamento.xml',
        'views/declaracao_importacao.xml',
        'wizards/declaracao_importacao_wizard.xml',
        'security/ir.model.access.csv'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
