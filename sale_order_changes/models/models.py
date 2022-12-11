from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.http import request


class SaleModelInherit(models.Model):
    _inherit = 'sale.order'

    partner_id = fields.Many2one(
        'res.partner', string='Customer', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain=lambda self: [('region_id', '=', self.env.user.region_id.id)])

    def return_sale_order_server(self):
        return {
            'name': 'Quotations',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'domain': [('region_id', '=', self.env.user.region_id.id)]
        }

    def return_sale_order(self):
        return {
            'name': 'Sale Orders',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'domain': [('region_id', '=', self.env.user.region_id.id),('state', '=', 'sale')]

        }

    def return_sale_quotations(self):
        return {
            'name': 'Quotations',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'domain': [('region_id', '=', self.env.user.region_id.id),('state', '=', 'draft')]

        }

    country_id = fields.Many2one('res.country')
    province_id = fields.Many2one('country.province')
    city_id = fields.Many2one('province.city')
    region_id = fields.Many2one('city.region')


    @api.model
    def create(self, vals_list):
        partner = self.partner_id.browse(vals_list['partner_id'])
        if partner.region_id:
            if self.env.user.region_id:
                vals_list['country_id'] = partner.region_id.city_id.province_id.country_id.id
                vals_list['province_id'] = partner.region_id.city_id.province_id.id
                vals_list['city_id'] = partner.region_id.city_id.id
                vals_list['region_id'] = partner.region_id.id
            else:
                raise ValidationError('Please specify login user region !')
        else:
            raise ValidationError('Please specify customer region !')

        res = super().create(vals_list)
        return res

    def write(self, vals):
        partner = self.partner_id
        if partner.region_id:
            if self.env.user.region_id:
                vals['country_id'] = partner.region_id.city_id.province_id.country_id.id
                vals['province_id'] = partner.region_id.city_id.province_id.id
                vals['city_id'] = partner.region_id.city_id.id
                vals['region_id'] = partner.region_id.id
            else:
                raise ValidationError('Please specify login user region !')
        else:
            raise ValidationError('Please specify customer region')

        return super().write(vals)
