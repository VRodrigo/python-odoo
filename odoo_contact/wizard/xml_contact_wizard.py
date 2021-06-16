from odoo import fields, models
import xml.etree.ElementTree as ET
import logging
import base64

_logger = logging.getLogger(__name__)


class XmlContactWizard(models.TransientModel):
    _name = "xml.contact.wizard"
    _description = "Create now contact through xml"

    xml_file = fields.Binary(name="Upload XML")

    def load_xml(self):
        input = base64.decodestring(self.xml_file).decode('utf-8')
        data = ET.fromstring(input)
        for contact in data:
            vals = {}
            for field in contact:
                vals.update({field.tag: field.text})
            self.env["contact"].create(vals)
