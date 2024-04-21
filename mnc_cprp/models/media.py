from odoo import api, models, fields, _

class CPRPMediaOrder(models.Model):
    _name = "cprp.media.order"
    _description = "Media Order CPRP"

    name = fields.Char(required=True)