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


class PostUserGroups(object):
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
        'created_by_id': 'str',
        'guid': 'str',
        'name': 'str'
    }

    attribute_map = {
        'created_by_id': 'created_by_id',
        'guid': 'guid',
        'name': 'name'
    }

    def __init__(self, created_by_id=None, guid=None, name=None):  # noqa: E501
        """PostUserGroups - a model defined in Swagger"""  # noqa: E501
        self._created_by_id = None
        self._guid = None
        self._name = None
        self.discriminator = None
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if guid is not None:
            self.guid = guid
        self.name = name

    @property
    def created_by_id(self):
        """Gets the created_by_id of this PostUserGroups.  # noqa: E501


        :return: The created_by_id of this PostUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this PostUserGroups.


        :param created_by_id: The created_by_id of this PostUserGroups.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def guid(self):
        """Gets the guid of this PostUserGroups.  # noqa: E501


        :return: The guid of this PostUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this PostUserGroups.


        :param guid: The guid of this PostUserGroups.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def name(self):
        """Gets the name of this PostUserGroups.  # noqa: E501

        Min length: 2, Max length: 255  # noqa: E501

        :return: The name of this PostUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostUserGroups.

        Min length: 2, Max length: 255  # noqa: E501

        :param name: The name of this PostUserGroups.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(PostUserGroups, dict):
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
        if not isinstance(other, PostUserGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
