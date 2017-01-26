# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from sng.sitecontent.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of sng.sitecontent into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sng.sitecontent is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.sngroductInstalled('sng.sitecontent'))

    def test_uninstall(self):
        """Test if sng.sitecontent is cleanly uninstalled."""
        self.installer.uninstallProducts(['sng.sitecontent'])
        self.assertFalse(self.installer.sngroductInstalled('sng.sitecontent'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ISngSitecontentLayer is registered."""
        from sng.sitecontent.interfaces import ISngSitecontentLayer
        from plone.browserlayer import utils
        self.failUnless(ISngSitecontentLayer in utils.registered_layers())
