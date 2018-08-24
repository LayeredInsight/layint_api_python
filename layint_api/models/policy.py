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


class Policy(object):
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
        'description': 'str',
        'user_id': 'str',
        'group_id': 'str',
        'schema_version': 'str',
        'default_file_action': 'str',
        'default_network_action': 'str',
        'default_program_action': 'str',
        'suspend': 'bool',
        'limits': 'Limit',
        'rules': 'list[PolicyRule]',
        'date_created': 'str',
        'date_updated': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'user_id': 'User_Id',
        'group_id': 'Group_Id',
        'schema_version': 'SchemaVersion',
        'default_file_action': 'DefaultFileAction',
        'default_network_action': 'DefaultNetworkAction',
        'default_program_action': 'DefaultProgramAction',
        'suspend': 'Suspend',
        'limits': 'Limits',
        'rules': 'Rules',
        'date_created': 'DateCreated',
        'date_updated': 'DateUpdated'
    }

    def __init__(self, id=None, name=None, description=None, user_id=None, group_id=None, schema_version=None, default_file_action=None, default_network_action=None, default_program_action=None, suspend=False, limits=None, rules=None, date_created=None, date_updated=None):
        """
        Policy - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._description = None
        self._user_id = None
        self._group_id = None
        self._schema_version = None
        self._default_file_action = None
        self._default_network_action = None
        self._default_program_action = None
        self._suspend = None
        self._limits = None
        self._rules = None
        self._date_created = None
        self._date_updated = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if user_id is not None:
          self.user_id = user_id
        if group_id is not None:
          self.group_id = group_id
        if schema_version is not None:
          self.schema_version = schema_version
        if default_file_action is not None:
          self.default_file_action = default_file_action
        if default_network_action is not None:
          self.default_network_action = default_network_action
        if default_program_action is not None:
          self.default_program_action = default_program_action
        if suspend is not None:
          self.suspend = suspend
        if limits is not None:
          self.limits = limits
        if rules is not None:
          self.rules = rules
        if date_created is not None:
          self.date_created = date_created
        if date_updated is not None:
          self.date_updated = date_updated

    @property
    def id(self):
        """
        Gets the id of this Policy.
        12 character internal hexadecimal identifier for this policy

        :return: The id of this Policy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Policy.
        12 character internal hexadecimal identifier for this policy

        :param id: The id of this Policy.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Policy.
        Name to refer to policy with and display

        :return: The name of this Policy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Policy.
        Name to refer to policy with and display

        :param name: The name of this Policy.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Policy.
        Free-form description of this policy

        :return: The description of this Policy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Policy.
        Free-form description of this policy

        :param description: The description of this Policy.
        :type: str
        """

        self._description = description

    @property
    def user_id(self):
        """
        Gets the user_id of this Policy.
        User ID of owner of the policy

        :return: The user_id of this Policy.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Policy.
        User ID of owner of the policy

        :param user_id: The user_id of this Policy.
        :type: str
        """

        self._user_id = user_id

    @property
    def group_id(self):
        """
        Gets the group_id of this Policy.
        Group ID of owner of the policy

        :return: The group_id of this Policy.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this Policy.
        Group ID of owner of the policy

        :param group_id: The group_id of this Policy.
        :type: str
        """

        self._group_id = group_id

    @property
    def schema_version(self):
        """
        Gets the schema_version of this Policy.
        Schema version for this policy

        :return: The schema_version of this Policy.
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """
        Sets the schema_version of this Policy.
        Schema version for this policy

        :param schema_version: The schema_version of this Policy.
        :type: str
        """

        self._schema_version = schema_version

    @property
    def default_file_action(self):
        """
        Gets the default_file_action of this Policy.
        Default action for file rules if no rule matches. This allows blacklisting or whitelisting.

        :return: The default_file_action of this Policy.
        :rtype: str
        """
        return self._default_file_action

    @default_file_action.setter
    def default_file_action(self, default_file_action):
        """
        Sets the default_file_action of this Policy.
        Default action for file rules if no rule matches. This allows blacklisting or whitelisting.

        :param default_file_action: The default_file_action of this Policy.
        :type: str
        """
        allowed_values = ["allow", "deny"]
        if default_file_action not in allowed_values:
            raise ValueError(
                "Invalid value for `default_file_action` ({0}), must be one of {1}"
                .format(default_file_action, allowed_values)
            )

        self._default_file_action = default_file_action

    @property
    def default_network_action(self):
        """
        Gets the default_network_action of this Policy.
        Default action for network rules if no rule matches. This allows blacklisting or whitelisting.

        :return: The default_network_action of this Policy.
        :rtype: str
        """
        return self._default_network_action

    @default_network_action.setter
    def default_network_action(self, default_network_action):
        """
        Sets the default_network_action of this Policy.
        Default action for network rules if no rule matches. This allows blacklisting or whitelisting.

        :param default_network_action: The default_network_action of this Policy.
        :type: str
        """
        allowed_values = ["allow", "deny"]
        if default_network_action not in allowed_values:
            raise ValueError(
                "Invalid value for `default_network_action` ({0}), must be one of {1}"
                .format(default_network_action, allowed_values)
            )

        self._default_network_action = default_network_action

    @property
    def default_program_action(self):
        """
        Gets the default_program_action of this Policy.
        Default action for program rules if no rule matches. This allows blacklisting or whitelisting.

        :return: The default_program_action of this Policy.
        :rtype: str
        """
        return self._default_program_action

    @default_program_action.setter
    def default_program_action(self, default_program_action):
        """
        Sets the default_program_action of this Policy.
        Default action for program rules if no rule matches. This allows blacklisting or whitelisting.

        :param default_program_action: The default_program_action of this Policy.
        :type: str
        """
        allowed_values = ["allow", "deny"]
        if default_program_action not in allowed_values:
            raise ValueError(
                "Invalid value for `default_program_action` ({0}), must be one of {1}"
                .format(default_program_action, allowed_values)
            )

        self._default_program_action = default_program_action

    @property
    def suspend(self):
        """
        Gets the suspend of this Policy.
        Allows suspension of policy enforcement

        :return: The suspend of this Policy.
        :rtype: bool
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """
        Sets the suspend of this Policy.
        Allows suspension of policy enforcement

        :param suspend: The suspend of this Policy.
        :type: bool
        """

        self._suspend = suspend

    @property
    def limits(self):
        """
        Gets the limits of this Policy.

        :return: The limits of this Policy.
        :rtype: Limit
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """
        Sets the limits of this Policy.

        :param limits: The limits of this Policy.
        :type: Limit
        """

        self._limits = limits

    @property
    def rules(self):
        """
        Gets the rules of this Policy.
        Policy rules defining control for this policy

        :return: The rules of this Policy.
        :rtype: list[PolicyRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this Policy.
        Policy rules defining control for this policy

        :param rules: The rules of this Policy.
        :type: list[PolicyRule]
        """

        self._rules = rules

    @property
    def date_created(self):
        """
        Gets the date_created of this Policy.
        Timestamp for when object was created

        :return: The date_created of this Policy.
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this Policy.
        Timestamp for when object was created

        :param date_created: The date_created of this Policy.
        :type: str
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """
        Gets the date_updated of this Policy.
        Timestamp for when object was last updated

        :return: The date_updated of this Policy.
        :rtype: str
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """
        Sets the date_updated of this Policy.
        Timestamp for when object was last updated

        :param date_updated: The date_updated of this Policy.
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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
