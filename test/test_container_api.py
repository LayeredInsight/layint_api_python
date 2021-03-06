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
from layint_api.apis.container_api import ContainerApi


class TestContainerApi(unittest.TestCase):
    """ ContainerApi unit test stubs """

    def setUp(self):
        self.api = layint_api.apis.container_api.ContainerApi()

    def tearDown(self):
        pass

    def test_assign_configuration_to_container(self):
        """
        Test case for assign_configuration_to_container

        Assign configuration to a container
        """
        pass

    def test_build_container_dossier_tempate(self):
        """
        Test case for build_container_dossier_tempate

        Builds a security policy based on containers behavior
        """
        pass

    def test_delete_container(self):
        """
        Test case for delete_container

        Delete a container
        """
        pass

    def test_dropped_logs_of_container(self):
        """
        Test case for dropped_logs_of_container

        Generates data used for UI
        """
        pass

    def test_edit_container(self):
        """
        Test case for edit_container

        Edit a container
        """
        pass

    def test_five_most_divergent_containers(self):
        """
        Test case for five_most_divergent_containers

        
        """
        pass

    def test_function_metrics(self):
        """
        Test case for function_metrics

        Get occurance of system calls in time
        """
        pass

    def test_functions(self):
        """
        Test case for functions

        Get a list of system calls a container has made
        """
        pass

    def test_get_agent_config(self):
        """
        Test case for get_agent_config

        Get the specified container configuration for the LI agent. The configuration consists of agent settings and policy rules.
        """
        pass

    def test_get_container_dossier(self):
        """
        Test case for get_container_dossier

        Gets dossier for container
        """
        pass

    def test_get_container_logs(self):
        """
        Test case for get_container_logs

        Gets behavioral logs for container
        """
        pass

    def test_get_containers(self):
        """
        Test case for get_containers

        Get containers
        """
        pass

    def test_get_resource_matrics(self):
        """
        Test case for get_resource_matrics

        Get current total container resource usage
        """
        pass

    def test_languages(self):
        """
        Test case for languages

        Get information about what languages are running in the container
        """
        pass

    def test_level_syscall_category_metrics(self):
        """
        Test case for level_syscall_category_metrics

        Get histograph information for system calls divided into category groups
        """
        pass

    def test_level_syscall_metrics(self):
        """
        Test case for level_syscall_metrics

        Get histograph information for system calls
        """
        pass

    def test_number_of_running_containers(self):
        """
        Test case for number_of_running_containers

        Get number of containers currently running
        """
        pass

    def test_passivate_container(self):
        """
        Test case for passivate_container

        Toggle the container behavior between passive and active
        """
        pass

    def test_post_behavioral_logging(self):
        """
        Test case for post_behavioral_logging

        Toggle behavioral logging on/off
        """
        pass

    def test_seccomp(self):
        """
        Test case for seccomp

        Get a Seccomp profile based on the list of system calls a container has made.
        """
        pass

    def test_show_container_details(self):
        """
        Test case for show_container_details

        Get a container
        """
        pass

    def test_singel_syscall(self):
        """
        Test case for singel_syscall

        Get amount of calls to a system call number in the last 5 seconds
        """
        pass

    def test_toggle_container_sniffer(self):
        """
        Test case for toggle_container_sniffer

        Toggles network sniffer
        """
        pass


if __name__ == '__main__':
    unittest.main()
