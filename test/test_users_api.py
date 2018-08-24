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
from layint_api.apis.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """ UsersApi unit test stubs """

    def setUp(self):
        self.api = layint_api.apis.users_api.UsersApi()

    def tearDown(self):
        pass

    def test_add_user(self):
        """
        Test case for add_user

        Add User
        """
        pass

    def test_assign_groups_to_user(self):
        """
        Test case for assign_groups_to_user

        Assign Group
        """
        pass

    def test_delete_user(self):
        """
        Test case for delete_user

        Delete the specified user
        """
        pass

    def test_list_user_by_id(self):
        """
        Test case for list_user_by_id

        Get specified UserID
        """
        pass

    def test_list_users(self):
        """
        Test case for list_users

        List Users
        """
        pass

    def test_modify_user(self):
        """
        Test case for modify_user

        Modify User
        """
        pass

    def test_search_user_by_email(self):
        """
        Test case for search_user_by_email

        Search User
        """
        pass

    def test_suspend_user(self):
        """
        Test case for suspend_user

        Suspend User
        """
        pass


if __name__ == '__main__':
    unittest.main()
