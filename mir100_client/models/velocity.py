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


class Velocity(object):
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
        'angular': 'float',
        'linear': 'float'
    }

    attribute_map = {
        'angular': 'angular',
        'linear': 'linear'
    }

    def __init__(self, angular=None, linear=None):  # noqa: E501
        """Velocity - a model defined in Swagger"""  # noqa: E501
        self._angular = None
        self._linear = None
        self.discriminator = None
        if angular is not None:
            self.angular = angular
        if linear is not None:
            self.linear = linear

    @property
    def angular(self):
        """Gets the angular of this Velocity.  # noqa: E501

        The angular speed of the robot in degrees/s  # noqa: E501

        :return: The angular of this Velocity.  # noqa: E501
        :rtype: float
        """
        return self._angular

    @angular.setter
    def angular(self, angular):
        """Sets the angular of this Velocity.

        The angular speed of the robot in degrees/s  # noqa: E501

        :param angular: The angular of this Velocity.  # noqa: E501
        :type: float
        """

        self._angular = angular

    @property
    def linear(self):
        """Gets the linear of this Velocity.  # noqa: E501

        The linear speed of the robot in m/s  # noqa: E501

        :return: The linear of this Velocity.  # noqa: E501
        :rtype: float
        """
        return self._linear

    @linear.setter
    def linear(self, linear):
        """Sets the linear of this Velocity.

        The linear speed of the robot in m/s  # noqa: E501

        :param linear: The linear of this Velocity.  # noqa: E501
        :type: float
        """

        self._linear = linear

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
        if issubclass(Velocity, dict):
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
        if not isinstance(other, Velocity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
