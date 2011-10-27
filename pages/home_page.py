#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Tests.
#
# The Initial Developer of the Original Code is Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): David Burns
#                 Zac Campbell
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
from pages.base_page import FlightDeckBasePage
from selenium.webdriver.common.by import By


class HomePage(FlightDeckBasePage):

    _create_addon_btn = (By.CSS_SELECTOR, "div.right_column div.fd_button > a")
    _create_lib_btn = (By.CSS_SELECTOR, "div.UI_Bottom_Info a[title='Create Library']")
    _browse_addons_list = (By.XPATH, "//ul[preceding-sibling::h2[text()='Browse Add-ons']]/li[@class='UI_Item']")
    _browse_libraries_list = (By.XPATH, "//ul[preceding-sibling::h2[text()='Browse Libraries']]/li[@class='UI_Item']")

    @property
    def browse_addons_count(self):
        return len(self.selenium.find_elements(*self._browse_addons_list))

    @property
    def browse_libraries_count(self):
        return len(self.selenium.find_elements(*self._browse_libraries_list))

    def click_create_addon_btn(self):
        self.selenium.find_element(*self._create_addon_btn).click()
        self.add_id()

    def click_create_lib_btn(self):
        self.selenium.find_element(*self._create_lib_btn).click()
        self.add_id()
