# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Partner Title Pricelist
#    Copyright (C) 2013 Mariano Ruiz <mrsarm@gmail.com>
#    Enterprise Objects Consulting (<http://www.eoconsulting.com.ar>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields, osv


class res_partner_title(osv.osv):
    _inherit = 'res.partner.title'

    _columns = {
        'default_pricelist_id': fields.many2one('product.pricelist', 'Default Pricelist', required=False,
                            domain=[('type','=','sale')],
                            help='Will be used by default in new partner with this title.'),
    }

res_partner_title()


class res_partner(osv.osv):
    _inherit = 'res.partner'

    def onchange_title(self, cr, uid, ids, value, context={}):
        if value:
            title = self.pool.get('res.partner.title').browse(cr, uid, value, context=context)
            if title.default_pricelist_id:
                return {'value': {'property_product_pricelist': title.default_pricelist_id.id}}
            elif len(ids)==0:
                return {'value': {'property_product_pricelist': False}}
            else:
                partner = self.browse(cr,uid,ids[0],context=context)
                return {'value': {'property_product_pricelist': partner.property_product_pricelist.id}}
        return {}

res_partner()
