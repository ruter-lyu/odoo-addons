# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2014 Elico Corp. All Rights Reserved.
#    Bob Lucas <luo.yumeng@elico-corp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later versionself.
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
    'name': 'ID Display',
    'version': '8.0.1.0.5',
    'category': 'project,CRM',
    'depends': ['project', 'crm', 'sale'],
    'author': 'Elico-Corp',
    'license': 'AGPL-3',
    'website': 'https://www.elico-corp.com',
    'support': 'support@elico-corp.com',
    'data': [
        'views/project_task_view.xml',
        'views/crm_lead_view.xml',
        'views/project_view.xml'
    ],
    'installable': True,
    'application': False,
}
