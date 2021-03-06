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


class ScanImage(object):
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
        'image_name': 'str',
        'image_url': 'str',
        'uri': 'str',
        'sid': 'str',
        'user_id': 'str',
        'registry': 'str',
        'status': 'str',
        'events': 'list[str]',
        'sha_sum': 'str',
        'layers': 'list[str]'
    }

    attribute_map = {
        'image_name': 'ImageName',
        'image_url': 'ImageUrl',
        'uri': 'Uri',
        'sid': 'Sid',
        'user_id': 'UserID',
        'registry': 'Registry',
        'status': 'Status',
        'events': 'Events',
        'sha_sum': 'ShaSum',
        'layers': 'Layers'
    }

    def __init__(self, image_name=None, image_url=None, uri=None, sid=None, user_id=None, registry=None, status=None, events=None, sha_sum=None, layers=None):
        """
        ScanImage - a model defined in Swagger
        """

        self._image_name = None
        self._image_url = None
        self._uri = None
        self._sid = None
        self._user_id = None
        self._registry = None
        self._status = None
        self._events = None
        self._sha_sum = None
        self._layers = None

        if image_name is not None:
          self.image_name = image_name
        if image_url is not None:
          self.image_url = image_url
        if uri is not None:
          self.uri = uri
        if sid is not None:
          self.sid = sid
        if user_id is not None:
          self.user_id = user_id
        if registry is not None:
          self.registry = registry
        if status is not None:
          self.status = status
        if events is not None:
          self.events = events
        if sha_sum is not None:
          self.sha_sum = sha_sum
        if layers is not None:
          self.layers = layers

    @property
    def image_name(self):
        """
        Gets the image_name of this ScanImage.
        name of container image

        :return: The image_name of this ScanImage.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """
        Sets the image_name of this ScanImage.
        name of container image

        :param image_name: The image_name of this ScanImage.
        :type: str
        """

        self._image_name = image_name

    @property
    def image_url(self):
        """
        Gets the image_url of this ScanImage.
        URL to registry store location of image

        :return: The image_url of this ScanImage.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """
        Sets the image_url of this ScanImage.
        URL to registry store location of image

        :param image_url: The image_url of this ScanImage.
        :type: str
        """

        self._image_url = image_url

    @property
    def uri(self):
        """
        Gets the uri of this ScanImage.
        Relative URI to this image within the Scan API

        :return: The uri of this ScanImage.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this ScanImage.
        Relative URI to this image within the Scan API

        :param uri: The uri of this ScanImage.
        :type: str
        """

        self._uri = uri

    @property
    def sid(self):
        """
        Gets the sid of this ScanImage.
        Unique ID of image in Scan

        :return: The sid of this ScanImage.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """
        Sets the sid of this ScanImage.
        Unique ID of image in Scan

        :param sid: The sid of this ScanImage.
        :type: str
        """

        self._sid = sid

    @property
    def user_id(self):
        """
        Gets the user_id of this ScanImage.
        User id of owner of this object

        :return: The user_id of this ScanImage.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ScanImage.
        User id of owner of this object

        :param user_id: The user_id of this ScanImage.
        :type: str
        """

        self._user_id = user_id

    @property
    def registry(self):
        """
        Gets the registry of this ScanImage.
        registry hostname

        :return: The registry of this ScanImage.
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """
        Sets the registry of this ScanImage.
        registry hostname

        :param registry: The registry of this ScanImage.
        :type: str
        """

        self._registry = registry

    @property
    def status(self):
        """
        Gets the status of this ScanImage.
        Current status of the scan of this image

        :return: The status of this ScanImage.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ScanImage.
        Current status of the scan of this image

        :param status: The status of this ScanImage.
        :type: str
        """
        allowed_values = ["pending", "done", "failed"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def events(self):
        """
        Gets the events of this ScanImage.
        a list of events that have occurred on this image. Could be considered a log of the scan process.

        :return: The events of this ScanImage.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """
        Sets the events of this ScanImage.
        a list of events that have occurred on this image. Could be considered a log of the scan process.

        :param events: The events of this ScanImage.
        :type: list[str]
        """

        self._events = events

    @property
    def sha_sum(self):
        """
        Gets the sha_sum of this ScanImage.
        Sha256 checksum for the image

        :return: The sha_sum of this ScanImage.
        :rtype: str
        """
        return self._sha_sum

    @sha_sum.setter
    def sha_sum(self, sha_sum):
        """
        Sets the sha_sum of this ScanImage.
        Sha256 checksum for the image

        :param sha_sum: The sha_sum of this ScanImage.
        :type: str
        """

        self._sha_sum = sha_sum

    @property
    def layers(self):
        """
        Gets the layers of this ScanImage.
        A list of checksums for each discovered layer in the image

        :return: The layers of this ScanImage.
        :rtype: list[str]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """
        Sets the layers of this ScanImage.
        A list of checksums for each discovered layer in the image

        :param layers: The layers of this ScanImage.
        :type: list[str]
        """

        self._layers = layers

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
        if not isinstance(other, ScanImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
