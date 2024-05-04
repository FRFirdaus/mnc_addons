from datetime import datetime
from odoo import api, models, fields, _

class CPRPMediaPurchase(models.Model):
    _name = "cprp.media.purchase"
    _description = "Media Purchase CPRP MNC"

    name = fields.Char(required=True)
    brand_id = fields.Many2one("cprp.brand")
    actual_ids = fields.One2many("cprp.media.purchase.actual", "media_purchase_id")

class CPRPMediaPurchaseActual(models.Model):
    _name = "cprp.media.purchase.actual"
    _description = "Media Purchase Actual CPRP MNC"

    media_purchase_id = fields.Many2one("cprp.media.purchase")
    duration = fields.Integer()
    date = fields.Datetime(default=datetime.now())
    start_time = fields.Char()
    end_time = fields.Char()
    week = fields.Integer()
    tvr = fields.Float(string="TVR")
