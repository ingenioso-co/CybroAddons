# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Ajith V (odoo@cybrosys.com)
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


class PosPaymentMethodKey(models.Model):
    """To create a new model and add new fields for defining shortcut keys
     related to payment methods"""
    _name = 'pos.payment.method.key'
    _description = 'Pos Payment Method Key'

    payment_method_id = fields.Many2one('pos.payment.method',
                                        String='Payment Method',
                                        help='This field represents the payment'
                                             'method used for transactions in '
                                             'the Point of Sale module. '
                                             'It allows users to select from '
                                             'predefined payment methods such '
                                             'as cash, credit card, '
                                             'or gift card when processing '
                                             'payments at the point of sale.')
    keyboard_shortcut_id = fields.Many2one('pos.keyboard.shortcut',
                                           string='Keyboard Shortcuts',
                                           help='This field associates a '
                                                'keyboard shortcut with a '
                                                'specific action or function in'
                                                'the Point of Sale interface. '
                                                'It allows users to quickly '
                                                'perform common tasks by '
                                                'pressing designated keys.')
    key_code = fields.Char(string='Key Code', help='This field stores the code '
                                                   'representing the key '
                                                   'or key combination'
                                                   ' assigned '
                                                   'to the keyboard shortcut. '
                                                   'It is '
                                                   'used to identify the '
                                                   'keystroke needed to '
                                                   'trigger the associated '
                                                   'action or function in '
                                                   'the Point of Sale '
                                                   'interface.')
