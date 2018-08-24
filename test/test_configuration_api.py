# coding: utf-8

"""
    Layered Insight Assessment, Compliance, Witness & Control

    LI Assessment & Compliance performs static vulnerability analysis, license and package compliance. LI Witness provides deep insight and analytics into containerized applications. Control provides dynamic runtime security and analytics for containerized applications. You can find out more about the Layered Insight Suite at [http://layeredinsight.com](http://layeredinsight.com).

    OpenAPI spec version: 0.10
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import layint_api
from layint_api.rest import ApiException
from layint_api.apis.configuration_api import ConfigurationApi


class TestConfigurationApi(unittest.TestCase):
    """ ConfigurationApi unit test stubs """

    def setUp(self):
        self.api = layint_api.apis.configuration_api.ConfigurationApi()

    def tearDown(self):
        pass

    def test_add_config(self):
        """
        Test case for add_config

        Create new configuration definition
        """
        pass

    def test_delete_config(self):
        """
        Test case for delete_config

        Delete configuration
        """
        pass

    def test_get_config(self):
        """
        Test case for get_config

        Get configuration
        """
        pass

    def test_get_config_by_name(self):
        """
        Test case for get_config_by_name

        Get configuration by name
        """
        pass

    def test_list_all_configurations(self):
        """
        Test case for list_all_configurations

        Get configurations
        """
        pass

    def test_update_config(self):
        """
        Test case for update_config

        Update configuration
        """
        pass


if __name__ == '__main__':
    unittest.main()
