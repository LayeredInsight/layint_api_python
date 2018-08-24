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


class ComplianceHistoryFailCompliance(object):
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
        'policy_name': 'str',
        'fail_rules': 'list[str]'
    }

    attribute_map = {
        'policy_name': 'PolicyName',
        'fail_rules': 'FailRules'
    }

    def __init__(self, policy_name=None, fail_rules=None):
        """
        ComplianceHistoryFailCompliance - a model defined in Swagger
        """

        self._policy_name = None
        self._fail_rules = None

        if policy_name is not None:
          self.policy_name = policy_name
        if fail_rules is not None:
          self.fail_rules = fail_rules

    @property
    def policy_name(self):
        """
        Gets the policy_name of this ComplianceHistoryFailCompliance.

        :return: The policy_name of this ComplianceHistoryFailCompliance.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """
        Sets the policy_name of this ComplianceHistoryFailCompliance.

        :param policy_name: The policy_name of this ComplianceHistoryFailCompliance.
        :type: str
        """

        self._policy_name = policy_name

    @property
    def fail_rules(self):
        """
        Gets the fail_rules of this ComplianceHistoryFailCompliance.

        :return: The fail_rules of this ComplianceHistoryFailCompliance.
        :rtype: list[str]
        """
        return self._fail_rules

    @fail_rules.setter
    def fail_rules(self, fail_rules):
        """
        Sets the fail_rules of this ComplianceHistoryFailCompliance.

        :param fail_rules: The fail_rules of this ComplianceHistoryFailCompliance.
        :type: list[str]
        """

        self._fail_rules = fail_rules

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
        if not isinstance(other, ComplianceHistoryFailCompliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
