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


class Notifications(object):
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
        'page': 'int',
        'page_size': 'int',
        'prev_page': 'str',
        'netx_page': 'str',
        'uri': 'str',
        'notification': 'list[Notification]'
    }

    attribute_map = {
        'page': 'Page',
        'page_size': 'PageSize',
        'prev_page': 'PrevPage',
        'netx_page': 'NetxPage',
        'uri': 'Uri',
        'notification': 'Notification'
    }

    def __init__(self, page=None, page_size=None, prev_page=None, netx_page=None, uri=None, notification=None):
        """
        Notifications - a model defined in Swagger
        """

        self._page = None
        self._page_size = None
        self._prev_page = None
        self._netx_page = None
        self._uri = None
        self._notification = None

        if page is not None:
          self.page = page
        if page_size is not None:
          self.page_size = page_size
        if prev_page is not None:
          self.prev_page = prev_page
        if netx_page is not None:
          self.netx_page = netx_page
        if uri is not None:
          self.uri = uri
        if notification is not None:
          self.notification = notification

    @property
    def page(self):
        """
        Gets the page of this Notifications.

        :return: The page of this Notifications.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """
        Sets the page of this Notifications.

        :param page: The page of this Notifications.
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """
        Gets the page_size of this Notifications.

        :return: The page_size of this Notifications.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this Notifications.

        :param page_size: The page_size of this Notifications.
        :type: int
        """

        self._page_size = page_size

    @property
    def prev_page(self):
        """
        Gets the prev_page of this Notifications.

        :return: The prev_page of this Notifications.
        :rtype: str
        """
        return self._prev_page

    @prev_page.setter
    def prev_page(self, prev_page):
        """
        Sets the prev_page of this Notifications.

        :param prev_page: The prev_page of this Notifications.
        :type: str
        """

        self._prev_page = prev_page

    @property
    def netx_page(self):
        """
        Gets the netx_page of this Notifications.

        :return: The netx_page of this Notifications.
        :rtype: str
        """
        return self._netx_page

    @netx_page.setter
    def netx_page(self, netx_page):
        """
        Sets the netx_page of this Notifications.

        :param netx_page: The netx_page of this Notifications.
        :type: str
        """

        self._netx_page = netx_page

    @property
    def uri(self):
        """
        Gets the uri of this Notifications.

        :return: The uri of this Notifications.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Notifications.

        :param uri: The uri of this Notifications.
        :type: str
        """

        self._uri = uri

    @property
    def notification(self):
        """
        Gets the notification of this Notifications.

        :return: The notification of this Notifications.
        :rtype: list[Notification]
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """
        Sets the notification of this Notifications.

        :param notification: The notification of this Notifications.
        :type: list[Notification]
        """

        self._notification = notification

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
        if not isinstance(other, Notifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
