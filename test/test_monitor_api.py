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
from layint_api.apis.monitor_api import MonitorApi


class TestMonitorApi(unittest.TestCase):
    """ MonitorApi unit test stubs """

    def setUp(self):
        self.api = layint_api.apis.monitor_api.MonitorApi()

    def tearDown(self):
        pass

    def test_monitor(self):
        """
        Test case for monitor

        Get policy hits
        """
        pass


if __name__ == '__main__':
    unittest.main()
