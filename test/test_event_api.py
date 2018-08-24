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
from layint_api.apis.event_api import EventApi


class TestEventApi(unittest.TestCase):
    """ EventApi unit test stubs """

    def setUp(self):
        self.api = layint_api.apis.event_api.EventApi()

    def tearDown(self):
        pass

    def test_describe_event(self):
        """
        Test case for describe_event

        Gets description about specific event
        """
        pass

    def test_get_file_accessors(self):
        """
        Test case for get_file_accessors

        Get programs accessing a file
        """
        pass

    def test_get_file_executors(self):
        """
        Test case for get_file_executors

        Get programs executing a file
        """
        pass

    def test_get_source_ip(self):
        """
        Test case for get_source_ip

        Get IP address used in event
        """
        pass

    def test_get_source_log(self):
        """
        Test case for get_source_log

        Get log that resulted in an event
        """
        pass


if __name__ == '__main__':
    unittest.main()
