# coding: utf-8

"""
    Layered Insight Assessment, Compliance, Witness & Control

    LI Assessment & Compliance performs static vulnerability analysis, license and package compliance. LI Witness provides deep insight and analytics into containerized applications. Control provides dynamic runtime security and analytics for containerized applications. You can find out more about the Layered Insight Suite at [http://layeredinsight.com](http://layeredinsight.com).

    OpenAPI spec version: 0.10
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LevelSyscallCategoryMetrics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_access': 'list[int]',
        'file_descriptor': 'list[int]',
        'network_access': 'list[int]',
        'process_control': 'list[int]',
        'system_wide': 'list[int]'
    }

    attribute_map = {
        'file_access': 'FileAccess',
        'file_descriptor': 'FileDescriptor',
        'network_access': 'NetworkAccess',
        'process_control': 'ProcessControl',
        'system_wide': 'SystemWide'
    }

    def __init__(self, file_access=None, file_descriptor=None, network_access=None, process_control=None, system_wide=None):
        """
        LevelSyscallCategoryMetrics - a model defined in Swagger
        """

        self._file_access = None
        self._file_descriptor = None
        self._network_access = None
        self._process_control = None
        self._system_wide = None

        if file_access is not None:
          self.file_access = file_access
        if file_descriptor is not None:
          self.file_descriptor = file_descriptor
        if network_access is not None:
          self.network_access = network_access
        if process_control is not None:
          self.process_control = process_control
        if system_wide is not None:
          self.system_wide = system_wide

    @property
    def file_access(self):
        """
        Gets the file_access of this LevelSyscallCategoryMetrics.

        :return: The file_access of this LevelSyscallCategoryMetrics.
        :rtype: list[int]
        """
        return self._file_access

    @file_access.setter
    def file_access(self, file_access):
        """
        Sets the file_access of this LevelSyscallCategoryMetrics.

        :param file_access: The file_access of this LevelSyscallCategoryMetrics.
        :type: list[int]
        """

        self._file_access = file_access

    @property
    def file_descriptor(self):
        """
        Gets the file_descriptor of this LevelSyscallCategoryMetrics.

        :return: The file_descriptor of this LevelSyscallCategoryMetrics.
        :rtype: list[int]
        """
        return self._file_descriptor

    @file_descriptor.setter
    def file_descriptor(self, file_descriptor):
        """
        Sets the file_descriptor of this LevelSyscallCategoryMetrics.

        :param file_descriptor: The file_descriptor of this LevelSyscallCategoryMetrics.
        :type: list[int]
        """

        self._file_descriptor = file_descriptor

    @property
    def network_access(self):
        """
        Gets the network_access of this LevelSyscallCategoryMetrics.

        :return: The network_access of this LevelSyscallCategoryMetrics.
        :rtype: list[int]
        """
        return self._network_access

    @network_access.setter
    def network_access(self, network_access):
        """
        Sets the network_access of this LevelSyscallCategoryMetrics.

        :param network_access: The network_access of this LevelSyscallCategoryMetrics.
        :type: list[int]
        """

        self._network_access = network_access

    @property
    def process_control(self):
        """
        Gets the process_control of this LevelSyscallCategoryMetrics.

        :return: The process_control of this LevelSyscallCategoryMetrics.
        :rtype: list[int]
        """
        return self._process_control

    @process_control.setter
    def process_control(self, process_control):
        """
        Sets the process_control of this LevelSyscallCategoryMetrics.

        :param process_control: The process_control of this LevelSyscallCategoryMetrics.
        :type: list[int]
        """

        self._process_control = process_control

    @property
    def system_wide(self):
        """
        Gets the system_wide of this LevelSyscallCategoryMetrics.

        :return: The system_wide of this LevelSyscallCategoryMetrics.
        :rtype: list[int]
        """
        return self._system_wide

    @system_wide.setter
    def system_wide(self, system_wide):
        """
        Sets the system_wide of this LevelSyscallCategoryMetrics.

        :param system_wide: The system_wide of this LevelSyscallCategoryMetrics.
        :type: list[int]
        """

        self._system_wide = system_wide

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, LevelSyscallCategoryMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
