# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from sng.buildout.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of sng.buildout into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sng.buildout is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('sng.buildout'))

    def test_uninstall(self):
        """Test if sng.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['sng.buildout'])
        self.assertFalse(self.installer.isProductInstalled('sng.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ISngBuildoutLayer is registered."""
        from sng.buildout.interfaces import ISngBuildoutLayer
        from plone.browserlayer import utils
        self.failUnless(ISngBuildoutLayer in utils.registered_layers())
