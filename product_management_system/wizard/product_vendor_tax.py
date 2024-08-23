# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Cybrosys Technologies (<https://www.cybrosys.com>)
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
################################################################################
from odoo import fields, models


class ProductVendorTax(models.TransientModel):
    """
        Model for updating vendor tax
    """
    _name = 'product.vendor.tax'
    _description = 'Product Vendor Tax'

    product_ids = fields.Many2many('product.template',
                                   string='Selected Products',
                                   readonly=True,
                                   help='Products which are selected to '
                                        'update the vendor tax')
    tax_ids = fields.Many2many('account.tax',
                               string="Vendor Tax",
                               help='Vendor tax to update for the selected '
                                    'product',
                               domain="[('type_tax_use', '=', 'purchase')]")

    def action_change_vendor_tax(self):
        """
        Function for updating vendor tax of the selected products
        """
        for products in self.product_ids:
                products.supplier_taxes_id = [fields.Command.set(self.tax_ids.ids)]
