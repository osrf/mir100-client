# coding: utf-8

"""
    MIR100 Rest Interface

    Automatically converted from v270 pdf  # noqa: E501

    OpenAPI spec version: 2.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Error(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'error_code': 'str',
        'error_human': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_human': 'error_human'
    }

    def __init__(self, error_code=None, error_human=None):  # noqa: E501
        """Error - a model defined in Swagger"""  # noqa: E501
        self._error_code = None
        self._error_human = None
        self.discriminator = None
        if error_code is not None:
            self.error_code = error_code
        if error_human is not None:
            self.error_human = error_human

    @property
    def error_code(self):
        """Gets the error_code of this Error.  # noqa: E501

        The error in machine format  # noqa: E501

        :return: The error_code of this Error.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this Error.

        The error in machine format  # noqa: E501

        :param error_code: The error_code of this Error.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_human(self):
        """Gets the error_human of this Error.  # noqa: E501

        The error in human friendly format  # noqa: E501

        :return: The error_human of this Error.  # noqa: E501
        :rtype: str
        """
        return self._error_human

    @error_human.setter
    def error_human(self, error_human):
        """Sets the error_human of this Error.

        The error in human friendly format  # noqa: E501

        :param error_human: The error_human of this Error.  # noqa: E501
        :type: str
        """

        self._error_human = error_human

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Error, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
