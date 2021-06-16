from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from email_validator import validate_email, EmailNotValidError


class Contact(models.Model):
    _name = 'contact'
    _rec_name = 'firstname'
    _description = 'Contact'

    firstname = fields.Char(string='Firstname', required=True)
    lastname = fields.Char(string='Surname', required=True)
    address = fields.Char(string='Address')
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string="Telephone Number")

    def email_validation(self, email):
        try:
            valid = validate_email(email)
            email = valid.email
        except EmailNotValidError:
            raise ValidationError(
                _("%s is an invalid email") % email.strip()
            )
        return email

    @api.model
    def create(self, vals):
        vals['email'] = self.email_validation(vals['email'])
        return super(Contact, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['email'] = self.email_validation(vals['email'])
        return super(Contact, self).write(vals)
