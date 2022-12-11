from odoo import api, fields, models

class CountryProvince(models.Model):
    _name = 'country.province'

    name = fields.Char('Main Category')
    country_id = fields.Many2one('res.country', 'Country')

class ProvinceCity(models.Model):
    _name = 'province.city'

    name = fields.Char('Sub Category')
    province_id = fields.Many2one('country.province', 'Main Category')

class CityRegion(models.Model):
    _name = 'city.region'

    name = fields.Char('City')
    city_id = fields.Many2one('province.city','Sub Category')
    main_cat_id = fields.Many2one('country.province','Main Category')



class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    region_id = fields.Many2one('city.region', 'City / Area')
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

    def write(self, vals):
        vals['country_id'] = self.region_id.city_id.province_id.country_id.id
        vals['province_id'] = self.self.region_id.city_id.province_id.id
        vals['city_id'] = self.self.region_id.city_id.id
        res = super().write(vals)
        return res