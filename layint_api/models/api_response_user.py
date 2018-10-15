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


class APIResponseUser(object):
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
        'username': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'company_id': 'str',
        'suspended': 'str',
        'primary_group': 'object',
        'all_groups': 'list[Group]'
    }

    attribute_map = {
        'id': 'ID',
        'username': 'Username',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'email': 'Email',
        'company_id': 'CompanyID',
        'suspended': 'Suspended',
        'primary_group': 'PrimaryGroup',
        'all_groups': 'AllGroups'
    }

    def __init__(self, id=None, username=None, first_name=None, last_name=None, email=None, company_id=None, suspended=None, primary_group=None, all_groups=None):
        """
        APIResponseUser - a model defined in Swagger
        """

        self._id = None
        self._username = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._company_id = None
        self._suspended = None
        self._primary_group = None
        self._all_groups = None

        if id is not None:
          self.id = id
        if username is not None:
          self.username = username
        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if email is not None:
          self.email = email
        if company_id is not None:
          self.company_id = company_id
        if suspended is not None:
          self.suspended = suspended
        if primary_group is not None:
          self.primary_group = primary_group
        if all_groups is not None:
          self.all_groups = all_groups

    @property
    def id(self):
        """
        Gets the id of this APIResponseUser.
        BsonObjectID string unique to the User

        :return: The id of this APIResponseUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this APIResponseUser.
        BsonObjectID string unique to the User

        :param id: The id of this APIResponseUser.
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """
        Gets the username of this APIResponseUser.
        Username of the User

        :return: The username of this APIResponseUser.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this APIResponseUser.
        Username of the User

        :param username: The username of this APIResponseUser.
        :type: str
        """

        self._username = username

    @property
    def first_name(self):
        """
        Gets the first_name of this APIResponseUser.
        First Name of the User

        :return: The first_name of this APIResponseUser.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this APIResponseUser.
        First Name of the User

        :param first_name: The first_name of this APIResponseUser.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this APIResponseUser.
        Last Name of the User

        :return: The last_name of this APIResponseUser.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this APIResponseUser.
        Last Name of the User

        :param last_name: The last_name of this APIResponseUser.
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """
        Gets the email of this APIResponseUser.
        Email ID of the User

        :return: The email of this APIResponseUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this APIResponseUser.
        Email ID of the User

        :param email: The email of this APIResponseUser.
        :type: str
        """

        self._email = email

    @property
    def company_id(self):
        """
        Gets the company_id of this APIResponseUser.
        BsonObjectID string unique to the company

        :return: The company_id of this APIResponseUser.
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """
        Sets the company_id of this APIResponseUser.
        BsonObjectID string unique to the company

        :param company_id: The company_id of this APIResponseUser.
        :type: str
        """

        self._company_id = company_id

    @property
    def suspended(self):
        """
        Gets the suspended of this APIResponseUser.
        Indicates if the User has been suspended or not

        :return: The suspended of this APIResponseUser.
        :rtype: str
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """
        Sets the suspended of this APIResponseUser.
        Indicates if the User has been suspended or not

        :param suspended: The suspended of this APIResponseUser.
        :type: str
        """

        self._suspended = suspended

    @property
    def primary_group(self):
        """
        Gets the primary_group of this APIResponseUser.
        PrimaryGroup of the User

        :return: The primary_group of this APIResponseUser.
        :rtype: object
        """
        return self._primary_group

    @primary_group.setter
    def primary_group(self, primary_group):
        """
        Sets the primary_group of this APIResponseUser.
        PrimaryGroup of the User

        :param primary_group: The primary_group of this APIResponseUser.
        :type: object
        """

        self._primary_group = primary_group

    @property
    def all_groups(self):
        """
        Gets the all_groups of this APIResponseUser.
        All group assigned to the User

        :return: The all_groups of this APIResponseUser.
        :rtype: list[Group]
        """
        return self._all_groups

    @all_groups.setter
    def all_groups(self, all_groups):
        """
        Sets the all_groups of this APIResponseUser.
        All group assigned to the User

        :param all_groups: The all_groups of this APIResponseUser.
        :type: list[Group]
        """

        self._all_groups = all_groups

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
        if not isinstance(other, APIResponseUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
