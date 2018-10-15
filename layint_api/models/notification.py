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


class Notification(object):
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
        'name': 'str',
        'message': 'str',
        'severity': 'str',
        'date_created': 'str',
        'date_updated': 'str'
    }

    attribute_map = {
        'id': 'ID',
        'name': 'Name',
        'message': 'Message',
        'severity': 'Severity',
        'date_created': 'DateCreated',
        'date_updated': 'DateUpdated'
    }

    def __init__(self, id=None, name=None, message=None, severity=None, date_created=None, date_updated=None):
        """
        Notification - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._message = None
        self._severity = None
        self._date_created = None
        self._date_updated = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if message is not None:
          self.message = message
        if severity is not None:
          self.severity = severity
        if date_created is not None:
          self.date_created = date_created
        if date_updated is not None:
          self.date_updated = date_updated

    @property
    def id(self):
        """
        Gets the id of this Notification.

        :return: The id of this Notification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Notification.

        :param id: The id of this Notification.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Notification.

        :return: The name of this Notification.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Notification.

        :param name: The name of this Notification.
        :type: str
        """

        self._name = name

    @property
    def message(self):
        """
        Gets the message of this Notification.

        :return: The message of this Notification.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Notification.

        :param message: The message of this Notification.
        :type: str
        """

        self._message = message

    @property
    def severity(self):
        """
        Gets the severity of this Notification.

        :return: The severity of this Notification.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this Notification.

        :param severity: The severity of this Notification.
        :type: str
        """

        self._severity = severity

    @property
    def date_created(self):
        """
        Gets the date_created of this Notification.

        :return: The date_created of this Notification.
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this Notification.

        :param date_created: The date_created of this Notification.
        :type: str
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """
        Gets the date_updated of this Notification.

        :return: The date_updated of this Notification.
        :rtype: str
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """
        Sets the date_updated of this Notification.

        :param date_updated: The date_updated of this Notification.
        :type: str
        """

        self._date_updated = date_updated

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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
