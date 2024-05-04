from odoo import api, models, fields, _

class CPRPAdvertise(models.Model):
    _name = "cprp.advertise"
    _description = "Advertise CPRP"
    _sql_constraints = [
        ("name_unique", "unique(name)", "Name must be unique")
    ]

    name = fields.Char(required=True)
    code = fields.Char()
    target_audience = fields.Char()

