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


class LicenseRuntime(object):
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
        'expire': 'str',
        'max_instrumented_images': 'int',
        'max_running_containers': 'int',
        'mq_hosts': 'list[str]',
        'options': 'object'
    }

    attribute_map = {
        'expire': 'Expire',
        'max_instrumented_images': 'MaxInstrumentedImages',
        'max_running_containers': 'MaxRunningContainers',
        'mq_hosts': 'MQHosts',
        'options': 'Options'
    }

    def __init__(self, expire=None, max_instrumented_images=None, max_running_containers=None, mq_hosts=None, options=None):
        """
        LicenseRuntime - a model defined in Swagger
        """

        self._expire = None
        self._max_instrumented_images = None
        self._max_running_containers = None
        self._mq_hosts = None
        self._options = None

        if expire is not None:
          self.expire = expire
        if max_instrumented_images is not None:
          self.max_instrumented_images = max_instrumented_images
        if max_running_containers is not None:
          self.max_running_containers = max_running_containers
        if mq_hosts is not None:
          self.mq_hosts = mq_hosts
        if options is not None:
          self.options = options

    @property
    def expire(self):
        """
        Gets the expire of this LicenseRuntime.
        Expiration date/time for runtime

        :return: The expire of this LicenseRuntime.
        :rtype: str
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        """
        Sets the expire of this LicenseRuntime.
        Expiration date/time for runtime

        :param expire: The expire of this LicenseRuntime.
        :type: str
        """

        self._expire = expire

    @property
    def max_instrumented_images(self):
        """
        Gets the max_instrumented_images of this LicenseRuntime.
        Maximum number of allowed instrumented images to be stored

        :return: The max_instrumented_images of this LicenseRuntime.
        :rtype: int
        """
        return self._max_instrumented_images

    @max_instrumented_images.setter
    def max_instrumented_images(self, max_instrumented_images):
        """
        Sets the max_instrumented_images of this LicenseRuntime.
        Maximum number of allowed instrumented images to be stored

        :param max_instrumented_images: The max_instrumented_images of this LicenseRuntime.
        :type: int
        """

        self._max_instrumented_images = max_instrumented_images

    @property
    def max_running_containers(self):
        """
        Gets the max_running_containers of this LicenseRuntime.
        Maximum number of simultaneous running containers

        :return: The max_running_containers of this LicenseRuntime.
        :rtype: int
        """
        return self._max_running_containers

    @max_running_containers.setter
    def max_running_containers(self, max_running_containers):
        """
        Sets the max_running_containers of this LicenseRuntime.
        Maximum number of simultaneous running containers

        :param max_running_containers: The max_running_containers of this LicenseRuntime.
        :type: int
        """

        self._max_running_containers = max_running_containers

    @property
    def mq_hosts(self):
        """
        Gets the mq_hosts of this LicenseRuntime.

        :return: The mq_hosts of this LicenseRuntime.
        :rtype: list[str]
        """
        return self._mq_hosts

    @mq_hosts.setter
    def mq_hosts(self, mq_hosts):
        """
        Sets the mq_hosts of this LicenseRuntime.

        :param mq_hosts: The mq_hosts of this LicenseRuntime.
        :type: list[str]
        """

        self._mq_hosts = mq_hosts

    @property
    def options(self):
        """
        Gets the options of this LicenseRuntime.
        Options

        :return: The options of this LicenseRuntime.
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this LicenseRuntime.
        Options

        :param options: The options of this LicenseRuntime.
        :type: object
        """

        self._options = options

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
        if not isinstance(other, LicenseRuntime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other