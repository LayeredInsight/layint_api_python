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


class PackageSearchData(object):
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
        'package': 'str',
        'version': 'str'
    }

    attribute_map = {
        'package': 'Package',
        'version': 'Version'
    }

    def __init__(self, package=None, version=None):
        """
        PackageSearchData - a model defined in Swagger
        """

        self._package = None
        self._version = None

        if package is not None:
          self.package = package
        if version is not None:
          self.version = version

    @property
    def package(self):
        """
        Gets the package of this PackageSearchData.
        Name of software package to search for. If absent, will search on all package names

        :return: The package of this PackageSearchData.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """
        Sets the package of this PackageSearchData.
        Name of software package to search for. If absent, will search on all package names

        :param package: The package of this PackageSearchData.
        :type: str
        """

        self._package = package

    @property
    def version(self):
        """
        Gets the version of this PackageSearchData.
        Version of sare package to search for. If absent, will search on all package versions

        :return: The version of this PackageSearchData.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PackageSearchData.
        Version of sare package to search for. If absent, will search on all package versions

        :param version: The version of this PackageSearchData.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, PackageSearchData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
