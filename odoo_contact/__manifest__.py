# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Odoo Contacts',
    'summary': "Contacts",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'CRM',
    'author': 'Victor Rodrigo',
    'website': '',
    'depends': [],
    'external_dependencies': {
        'python': ['email_validator']
    },
    'data': [
        'security/contact_security.xml',
        'views/menu_contact_view.xml',
        'wizard/xml_contact_wizard_view.xml',
        'views/contact_view.xml',
        'security/ir.model.access.csv'
    ],
    'application': True,
    'installable': True,
}
