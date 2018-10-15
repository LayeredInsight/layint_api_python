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


class AlertsMessages(object):
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
        'id': 'str',
        'level': 'str',
        'title': 'str',
        'text': 'str',
        'type': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'id': 'ID',
        'level': 'Level',
        'title': 'Title',
        'text': 'Text',
        'type': 'Type',
        'resource_id': 'ResourceID'
    }

    def __init__(self, id=None, level=None, title=None, text=None, type=None, resource_id=None):
        """
        AlertsMessages - a model defined in Swagger
        """

        self._id = None
        self._level = None
        self._title = None
        self._text = None
        self._type = None
        self._resource_id = None

        if id is not None:
          self.id = id
        if level is not None:
          self.level = level
        if title is not None:
          self.title = title
        if text is not None:
          self.text = text
        if type is not None:
          self.type = type
        if resource_id is not None:
          self.resource_id = resource_id

    @property
    def id(self):
        """
        Gets the id of this AlertsMessages.

        :return: The id of this AlertsMessages.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AlertsMessages.

        :param id: The id of this AlertsMessages.
        :type: str
        """

        self._id = id

    @property
    def level(self):
        """
        Gets the level of this AlertsMessages.

        :return: The level of this AlertsMessages.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this AlertsMessages.

        :param level: The level of this AlertsMessages.
        :type: str
        """

        self._level = level

    @property
    def title(self):
        """
        Gets the title of this AlertsMessages.

        :return: The title of this AlertsMessages.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this AlertsMessages.

        :param title: The title of this AlertsMessages.
        :type: str
        """

        self._title = title

    @property
    def text(self):
        """
        Gets the text of this AlertsMessages.

        :return: The text of this AlertsMessages.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this AlertsMessages.

        :param text: The text of this AlertsMessages.
        :type: str
        """

        self._text = text

    @property
    def type(self):
        """
        Gets the type of this AlertsMessages.

        :return: The type of this AlertsMessages.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AlertsMessages.

        :param type: The type of this AlertsMessages.
        :type: str
        """

        self._type = type

    @property
    def resource_id(self):
        """
        Gets the resource_id of this AlertsMessages.

        :return: The resource_id of this AlertsMessages.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this AlertsMessages.

        :param resource_id: The resource_id of this AlertsMessages.
        :type: str
        """

        self._resource_id = resource_id

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
        if not isinstance(other, AlertsMessages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other