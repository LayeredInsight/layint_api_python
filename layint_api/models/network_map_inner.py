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


class NetworkMapInner(object):
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
        'container_id': 'str',
        'neighbours': 'list[str]'
    }

    attribute_map = {
        'container_id': 'ContainerID',
        'neighbours': 'Neighbours'
    }

    def __init__(self, container_id=None, neighbours=None):
        """
        NetworkMapInner - a model defined in Swagger
        """

        self._container_id = None
        self._neighbours = None

        if container_id is not None:
          self.container_id = container_id
        if neighbours is not None:
          self.neighbours = neighbours

    @property
    def container_id(self):
        """
        Gets the container_id of this NetworkMapInner.

        :return: The container_id of this NetworkMapInner.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """
        Sets the container_id of this NetworkMapInner.

        :param container_id: The container_id of this NetworkMapInner.
        :type: str
        """

        self._container_id = container_id

    @property
    def neighbours(self):
        """
        Gets the neighbours of this NetworkMapInner.

        :return: The neighbours of this NetworkMapInner.
        :rtype: list[str]
        """
        return self._neighbours

    @neighbours.setter
    def neighbours(self, neighbours):
        """
        Sets the neighbours of this NetworkMapInner.

        :param neighbours: The neighbours of this NetworkMapInner.
        :type: list[str]
        """

        self._neighbours = neighbours

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
        if not isinstance(other, NetworkMapInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
