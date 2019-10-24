# -*- coding: utf-8 -*-
# Part of Inceptus ERP Solutions Pvt.ltd.
# See LICENSE file for copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _name = 'product.template'

    _inherit = ["product.template", "ies.base"]

    @api.one
    @api.depends('coupon_ids')
    def _get_coupon_count(self):
        self.coupon_count = len(
            self.coupon_ids.filtered(lambda record: record.type in ['p'] and record.coupon_type == 'c'))

    # @api.model
    # def _get_discount_type(self):
    #     print "+===========++", self._context
    #     res = super(ProductTemplate, self)._get_discount_type()
    #     if self._context.get('coupon'):
    #         print [('p', 'Percentage')]
    #         return [('p', 'Percentage')]
    #
    # @api.model
    # def _get_default_type(self):
    #     if self._context.get('coupon'):
    #         return 'p'

    @api.multi
    def open_coupons(self):
        domain = [('product_id', '=', self.id)]
        view_id, form_view_id = False, False
        name = False
        if self._context.get('type') == 'p':
            name = _('Coupons')
            domain += [('type', '=', 'p')]
            view_id = self.env.ref('ies_coupons.ies_product_coupon_tree').id

            form_view_id = self.env.ref('ies_coupons.ies_product_coupon_form').id
        return {
            'name': name,
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'product.coupon',
            'domain': domain,
            'views': [(view_id, 'tree'), (form_view_id, 'form')]
        }
