from odoo import api, models, fields, _

class CPRPAgency(models.Model):
    _name = "cprp.agency"
    _description = "Agency CPRP"

    name = fields.Char(required=True)

