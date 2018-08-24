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


class ImageLog(object):
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
        'sid': 'str',
        'parent_sid': 'str',
        'user_id': 'str',
        'uri': 'str',
        'date_created': 'str',
        'event': 'str'
    }

    attribute_map = {
        'sid': 'Sid',
        'parent_sid': 'ParentSid',
        'user_id': 'UserID',
        'uri': 'Uri',
        'date_created': 'DateCreated',
        'event': 'Event'
    }

    def __init__(self, sid=None, parent_sid=None, user_id=None, uri=None, date_created=None, event=None):
        """
        ImageLog - a model defined in Swagger
        """

        self._sid = None
        self._parent_sid = None
        self._user_id = None
        self._uri = None
        self._date_created = None
        self._event = None

        if sid is not None:
          self.sid = sid
        if parent_sid is not None:
          self.parent_sid = parent_sid
        if user_id is not None:
          self.user_id = user_id
        if uri is not None:
          self.uri = uri
        if date_created is not None:
          self.date_created = date_created
        if event is not None:
          self.event = event

    @property
    def sid(self):
        """
        Gets the sid of this ImageLog.

        :return: The sid of this ImageLog.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """
        Sets the sid of this ImageLog.

        :param sid: The sid of this ImageLog.
        :type: str
        """

        self._sid = sid

    @property
    def parent_sid(self):
        """
        Gets the parent_sid of this ImageLog.

        :return: The parent_sid of this ImageLog.
        :rtype: str
        """
        return self._parent_sid

    @parent_sid.setter
    def parent_sid(self, parent_sid):
        """
        Sets the parent_sid of this ImageLog.

        :param parent_sid: The parent_sid of this ImageLog.
        :type: str
        """

        self._parent_sid = parent_sid

    @property
    def user_id(self):
        """
        Gets the user_id of this ImageLog.

        :return: The user_id of this ImageLog.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ImageLog.

        :param user_id: The user_id of this ImageLog.
        :type: str
        """

        self._user_id = user_id

    @property
    def uri(self):
        """
        Gets the uri of this ImageLog.

        :return: The uri of this ImageLog.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this ImageLog.

        :param uri: The uri of this ImageLog.
        :type: str
        """

        self._uri = uri

    @property
    def date_created(self):
        """
        Gets the date_created of this ImageLog.
        Creation date/time

        :return: The date_created of this ImageLog.
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this ImageLog.
        Creation date/time

        :param date_created: The date_created of this ImageLog.
        :type: str
        """

        self._date_created = date_created

    @property
    def event(self):
        """
        Gets the event of this ImageLog.

        :return: The event of this ImageLog.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """
        Sets the event of this ImageLog.

        :param event: The event of this ImageLog.
        :type: str
        """

        self._event = event

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
        if not isinstance(other, ImageLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
