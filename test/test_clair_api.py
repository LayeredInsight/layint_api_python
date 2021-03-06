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
from layint_api.apis.clair_api import ClairApi


class TestClairApi(unittest.TestCase):
    """ ClairApi unit test stubs """

    def setUp(self):
        self.api = layint_api.apis.clair_api.ClairApi()

    def tearDown(self):
        pass

    def test_clair_update(self):
        """
        Test case for clair_update

        Notify user(s) of vulnerability update from clair notification
        """
        pass

    def test_get_clair_updates(self):
        """
        Test case for get_clair_updates

        Returns date/time estimation when clair updates will be done
        """
        pass


if __name__ == '__main__':
    unittest.main()
