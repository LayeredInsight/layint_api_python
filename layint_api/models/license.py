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


class License(object):
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
        'version': 'str',
        'licensee': 'str',
        'issue': 'str',
        'product': 'LicenseProduct',
        'scan': 'LicenseScan',
        'runtime': 'LicenseRuntime'
    }

    attribute_map = {
        'version': 'Version',
        'licensee': 'Licensee',
        'issue': 'Issue',
        'product': 'Product',
        'scan': 'Scan',
        'runtime': 'Runtime'
    }

    def __init__(self, version=None, licensee=None, issue=None, product=None, scan=None, runtime=None):
        """
        License - a model defined in Swagger
        """

        self._version = None
        self._licensee = None
        self._issue = None
        self._product = None
        self._scan = None
        self._runtime = None

        if version is not None:
          self.version = version
        if licensee is not None:
          self.licensee = licensee
        if issue is not None:
          self.issue = issue
        if product is not None:
          self.product = product
        if scan is not None:
          self.scan = scan
        if runtime is not None:
          self.runtime = runtime

    @property
    def version(self):
        """
        Gets the version of this License.
        License version

        :return: The version of this License.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this License.
        License version

        :param version: The version of this License.
        :type: str
        """

        self._version = version

    @property
    def licensee(self):
        """
        Gets the licensee of this License.
        Licensee to whom the license is issued

        :return: The licensee of this License.
        :rtype: str
        """
        return self._licensee

    @licensee.setter
    def licensee(self, licensee):
        """
        Sets the licensee of this License.
        Licensee to whom the license is issued

        :param licensee: The licensee of this License.
        :type: str
        """

        self._licensee = licensee

    @property
    def issue(self):
        """
        Gets the issue of this License.
        Issue date/time

        :return: The issue of this License.
        :rtype: str
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        """
        Sets the issue of this License.
        Issue date/time

        :param issue: The issue of this License.
        :type: str
        """

        self._issue = issue

    @property
    def product(self):
        """
        Gets the product of this License.

        :return: The product of this License.
        :rtype: LicenseProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this License.

        :param product: The product of this License.
        :type: LicenseProduct
        """

        self._product = product

    @property
    def scan(self):
        """
        Gets the scan of this License.

        :return: The scan of this License.
        :rtype: LicenseScan
        """
        return self._scan

    @scan.setter
    def scan(self, scan):
        """
        Sets the scan of this License.

        :param scan: The scan of this License.
        :type: LicenseScan
        """

        self._scan = scan

    @property
    def runtime(self):
        """
        Gets the runtime of this License.

        :return: The runtime of this License.
        :rtype: LicenseRuntime
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """
        Sets the runtime of this License.

        :param runtime: The runtime of this License.
        :type: LicenseRuntime
        """

        self._runtime = runtime

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
        if not isinstance(other, License):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
