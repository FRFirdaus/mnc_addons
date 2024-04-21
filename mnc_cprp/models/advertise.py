from odoo import api, models, fields, _

class CPRPAdvertise(models.Model):
    _name = "cprp.advertise"
    _description = "Advertise CPRP"

    name = fields.Char(required=True)
    code = fields.Char()
    target_audience = fields.Char()

