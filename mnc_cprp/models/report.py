from odoo import api, models, fields, _
from datetime import datetime

class CPRPReport(models.Model):
    _name = "cprp.report"
    _description = "Report Details CPRP"

    name = fields.Char(required=True, compute="_compute_name_report", store=True, readonly=False)
    report = fields.Selection([
        ("tabungan", "Tabungan"),
        ("cancel", "Cancel"),
        ("Report", "Report")
    ])
    is_reported = fields.Boolean(default=False)
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user.id, string="Planner/User")
    note = fields.Text()
    sales = fields.Char()
    date = fields.Date(default=datetime.now().date(), required=True)
    planner_code = fields.Char()
    advertise_id = fields.Many2one("cprp.advertise")
    brand_id = fields.Many2one("cprp.brand")
    state = fields.Selection([
        ("PAID", "Paid"),
        ("KOMPGP", "Komp GP"),
        ("KOMPZR", "Komp ZR"),
        ("PREMIUM", "Premium"),
        ("CANCEL", "Cancel")
    ])
    purchase_order_id = fields.Many2one("cprp.media.purchase", domain="[('brand_id', '=', brand_id)]")
    media_order_id = fields.Many2one("cprp.media.order")
    start_date = fields.Date(default=datetime.now().date())
    to_date = fields.Date(default=datetime.now().date())
    jam_tayang = fields.Char()
    target_audience = fields.Char(related="advertise_id.target_audience", store=True)
    version_client = fields.Char()
    version_internal = fields.Char()
    duration = fields.Integer(string="Duration (Seconds)")
    budget_awal = fields.Float()
    budget_additional = fields.Float()
    budget_cancel = fields.Float()
    budget_final = fields.Float()
    level = fields.Float()
    prime_time = fields.Float()
    position_in_break = fields.Float()

    plan_ids = fields.One2many("cprp.report.plan", "report_id")
    actual_ids = fields.One2many("cprp.report.actual", "report_id")

    @api.onchange("date", "planner_code", "advertise_id", "brand_id", "state")
    def _compute_name_report(self):
        for rec in self:
            if rec.advertise_id and rec.brand_id and rec.planner_code and rec.date and rec.state:
                format_string = "1001-%s-%s-%s-%s-%s" % (
                    rec.advertise_id.code or "None",
                    rec.brand_id.code or "None",
                    rec.planner_code or "None",
                    rec.date.strftime("%d%m%y"),
                    rec.state or "None"
                )
                rec.name = format_string
    
    @api.onchange("purchase_order_id")
    def _compute_actual_rating(self):
        for rec in self:
            if rec.purchase_order_id and rec.purchase_order_id.actual_ids:
                rec.actual_ids = [(5, 0, 0)]
                list_of_week = list(set([act.week for act in rec.purchase_order_id.actual_ids]))

                list_of_actual_reports = []
                for lst in list_of_week:
                    actual_data_ids = rec.purchase_order_id.actual_ids.filtered(lambda act: act.week == lst)
                    total_rating = sum([actdt.tvr for actdt in actual_data_ids])
                    list_of_actual_reports.append((0, 0, {
                        "name": "A%s" % (lst),
                        "grp": total_rating
                    }))
                
                rec.write({
                    "actual_ids": list_of_actual_reports
                })

class CPRPReportPlan(models.Model):
    _name = "cprp.report.plan"
    _description = "Report Plan GRP CPRP"

    report_id = fields.Many2one("cprp.report")
    name = fields.Char(required=True)
    grp = fields.Float()

class CPRPReportActual(models.Model):
    _name = "cprp.report.actual"
    _description = "Report Actual GRP CPRP"

    report_id = fields.Many2one("cprp.report")
    name = fields.Char(required=True)
    grp = fields.Float() 



