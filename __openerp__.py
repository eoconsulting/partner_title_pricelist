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


{
    'name': 'Partner Title Pricelist',
    'version': '1.0',
    'category': 'Sales Management',
    'description': """
Make visible the 'Title' field in the Partner form, and
add 'Default Pricelist' field in Partner Titles.

When a new partner is created, if the title have a default
price list, that list is assigned to the new client.
""",
    'author': 'Enterprise Objects Consulting',
    'website': 'http://www.eoconsulting.com.ar',
    'depends': ['base', 'product'],
    'init_xml': [],
    'update_xml': ['partner_view.xml',],
    'installable': True,
    'active': False,
}
