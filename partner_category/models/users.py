from odoo import api, fields, models

class UserModelInherit(models.Model):
    _inherit = 'res.users'

    region_id = fields.Many2one('city.region', 'City')
    city_id = fields.Many2one('province.city')
    province_id = fields.Many2one('country.province')
    country_id = fields.Many2one('res.country')

    @api.model
    def create(self, vals_list):
        vals_list['country_id'] = self.region_id.city_id.province_id.country_id.id
        vals_list['province_id'] = self.self.region_id.city_id.province_id.id
        vals_list['city_id'] = self.self.region_id.city_id.id
        res = super().create(vals_list)
        return res


    # def write(self, vals):
    #
    #     vals['country_id'] = self.region_id.city_id.province_id.country_id.id
    #     vals['province_id'] = self.self.region_id.city_id.province_id.id
    #     vals['city_id'] = self.self.region_id.city_id.id
    #
    #     return super().write(vals)