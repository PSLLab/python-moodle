# -*- encoding: utf-8 -*-
##############################################################################
#
#    Moodle Webservice
#    Copyright (c) 2011 Zikzakmedia S.L. (http://zikzakmedia.com) All Rights Reserved.
#                       Raimon Esteve <resteve@zikzakmedia.com>
#                       Jesus Martín <jmartin@zikzakmedia.com>
#    $Id$
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

from config import *
from moodle_ws_client import moodle

mdl = moodle.MDL()
# xmlrpc Connection
print mdl.conn_xmlrpc(server)

"""
Create new cohorts

cohorts[0][categorytype][type]= string
cohorts[0][categorytype][value]= string
cohorts[0][name]= string
cohorts[0][idnumber]= string
cohorts[0][description]= string
cohorts[0][descriptionformat]= int
cohorts[0][visible]= int

"""
cohorts = [{
    'name': 'test1', # shortname must be unique
    'idnumber': 'co1',
    'description': 'Test 1',
    'descriptionformat': 2,
    'categorytype': { 'type': 'system', 'value': '' },
    'visible': 1
}]

print mdl.create_cohorts(server, cohorts)
