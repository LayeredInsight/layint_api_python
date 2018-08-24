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


class PackageSearchResult(object):
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
        'package_version': 'PackageVersion',
        'images': 'list[ImageRef]'
    }

    attribute_map = {
        'package_version': 'PackageVersion',
        'images': 'Images'
    }

    def __init__(self, package_version=None, images=None):
        """
        PackageSearchResult - a model defined in Swagger
        """

        self._package_version = None
        self._images = None

        if package_version is not None:
          self.package_version = package_version
        if images is not None:
          self.images = images

    @property
    def package_version(self):
        """
        Gets the package_version of this PackageSearchResult.

        :return: The package_version of this PackageSearchResult.
        :rtype: PackageVersion
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """
        Sets the package_version of this PackageSearchResult.

        :param package_version: The package_version of this PackageSearchResult.
        :type: PackageVersion
        """

        self._package_version = package_version

    @property
    def images(self):
        """
        Gets the images of this PackageSearchResult.

        :return: The images of this PackageSearchResult.
        :rtype: list[ImageRef]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this PackageSearchResult.

        :param images: The images of this PackageSearchResult.
        :type: list[ImageRef]
        """

        self._images = images

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
        if not isinstance(other, PackageSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
