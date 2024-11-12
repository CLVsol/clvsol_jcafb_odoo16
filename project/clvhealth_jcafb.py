# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

import images

from clvsol_odoo_client2.db import *

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)


class CLVhealthJCAFB(object):

    def __init__(
        self,

        server='http://localhost:8069',
        super_user_pw='',

        CompanyName='CLVhealth-JCAFB',
        Company_image=images.Company_image,
        website='https://github.com/CLVsol',

        admin_user_pw='admin',
        admin_user_email='admin@clvsol.com',
        Administrator_image=images.Administrator_image,

        data_admin_user_name='Data Administrator',
        data_admin_user='data.admin',
        data_admin_user_pw='data.admin',
        data_admin_user_email='data.admin@clvsol.com',
        DataAdministrator_image=images.DataAdministrator_image,

        dbname='clvhealth_jcafb',

        lang='pt_BR',
        tz='America/Sao_Paulo',

        demo_data=False,
        upgrade_all=False,
        modules_to_upgrade=[],
    ):

        self.server = server
        self.super_user_pw = super_user_pw

        self.CompanyName = CompanyName
        self.Company_image = Company_image
        self.website = website

        self.admin_user_pw = admin_user_pw
        self.admin_user_email = admin_user_email
        self.Administrator_image = Administrator_image

        self.data_admin_user_name = data_admin_user_name
        self.data_admin_user = data_admin_user
        self.data_admin_user_pw = data_admin_user_pw
        self.data_admin_user_email = data_admin_user_email
        self.DataAdministrator_image = DataAdministrator_image

        self.dbname = dbname

        self.lang = lang
        self.tz = tz

        self.demo_data = demo_data
        self.upgrade_all = upgrade_all
        self.modules_to_upgrade = modules_to_upgrade

        self.db = DB(
            server=self.server,
            super_user_pw=self.super_user_pw,
            admin_user_pw=self.admin_user_pw,
            data_admin_user_pw=self.data_admin_user_pw,
            dbname=self.dbname,
            demo_data=self.demo_data,
            lang=self.lang,
            tz=self.tz
        )

    def install(self):

        newDB = self.db.create()

        if newDB:
            pass
        else:
            _logger.info(u'%s %s', '--> newDB:', newDB)

