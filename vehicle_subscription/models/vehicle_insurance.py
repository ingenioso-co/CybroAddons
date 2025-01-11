# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2025-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Jumana Jabin MP (<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class VehicleInsurance(models.Model):
    """New model vehicle .insurance"""
    _name = "vehicle.insurance"
    _description = "Vehicle Insurance"
    _inherit = "mail.thread"
    _rec_name = "vehicle_id"

    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle",
                                 help="Help you to choose vehicle",
                                 required=True)
    start_date = fields.Date(string="Start Date", help="Insurance start date",
                             required=True)
    end_date = fields.Date(string="End Date", help="Insurance end date",
                           required=True)
    insurance_type_id = fields.Many2one('insurance.type',
                                        string='Insurance Type',
                                        help="Choose insurance type")
    insurance_amount = fields.Float(string="Amount",
                                    compute="_compute_insurance_amount",
                                    help="Calculate insurance amount")

    def _compute_insurance_amount(self):
        """Function used to compute insurance amount"""
        for rec in self:
            rec.insurance_amount = sum(rec.insurance_type_id.coverage_ids.
                                       mapped('coverage_price'))

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """Ensure that the start date is not greater than the end date."""
        for rec in self:
            if rec.start_date > rec.end_date:
                raise ValidationError(
                    "Start Date cannot be greater than End Date")
