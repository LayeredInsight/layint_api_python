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


class UserGroup(object):
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
        'user_id': 'str',
        'group_id': 'str'
    }

    attribute_map = {
        'id': 'ID',
        'user_id': 'UserID',
        'group_id': 'GroupID'
    }

    def __init__(self, id=None, user_id=None, group_id=None):
        """
        UserGroup - a model defined in Swagger
        """

        self._id = None
        self._user_id = None
        self._group_id = None

        if id is not None:
          self.id = id
        if user_id is not None:
          self.user_id = user_id
        if group_id is not None:
          self.group_id = group_id

    @property
    def id(self):
        """
        Gets the id of this UserGroup.
        BsonObjectID string unique of UserGroup

        :return: The id of this UserGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserGroup.
        BsonObjectID string unique of UserGroup

        :param id: The id of this UserGroup.
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this UserGroup.
        BsonObjectID string unique of User

        :return: The user_id of this UserGroup.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UserGroup.
        BsonObjectID string unique of User

        :param user_id: The user_id of this UserGroup.
        :type: str
        """

        self._user_id = user_id

    @property
    def group_id(self):
        """
        Gets the group_id of this UserGroup.
        BsonObjectID string unique of Group

        :return: The group_id of this UserGroup.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this UserGroup.
        BsonObjectID string unique of Group

        :param group_id: The group_id of this UserGroup.
        :type: str
        """

        self._group_id = group_id

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
        if not isinstance(other, UserGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
