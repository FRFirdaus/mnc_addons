from odoo import api, models, fields, _

class CPRPBrand(models.Model):
    _name = "cprp.brand"
    _description = "Brand of Advertise CPRP"

    name = fields.Char(required=True)
    code = fields.Char()
    advertise_id = fields.Many2one("cprp.advertise", required=True)
    agency_id = fields.Many2one("cprp.agency")
    sales_account_executive = fields.Char()
    sales_group_head = fields.Char()
    sales_manager = fields.Char()
    

