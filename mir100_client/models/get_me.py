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


class GetMe(object):
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
        'guid': 'str',
        'name': 'str',
        'url': 'str',
        'user_group': 'str',
        'user_group_id': 'str'
    }

    attribute_map = {
        'guid': 'guid',
        'name': 'name',
        'url': 'url',
        'user_group': 'user_group',
        'user_group_id': 'user_group_id'
    }

    def __init__(self, guid=None, name=None, url=None, user_group=None, user_group_id=None):  # noqa: E501
        """GetMe - a model defined in Swagger"""  # noqa: E501
        self._guid = None
        self._name = None
        self._url = None
        self._user_group = None
        self._user_group_id = None
        self.discriminator = None
        if guid is not None:
            self.guid = guid
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if user_group is not None:
            self.user_group = user_group
        if user_group_id is not None:
            self.user_group_id = user_group_id

    @property
    def guid(self):
        """Gets the guid of this GetMe.  # noqa: E501

        The global unique id across robots that identifies this user  # noqa: E501

        :return: The guid of this GetMe.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetMe.

        The global unique id across robots that identifies this user  # noqa: E501

        :param guid: The guid of this GetMe.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def name(self):
        """Gets the name of this GetMe.  # noqa: E501

        The name of the user  # noqa: E501

        :return: The name of this GetMe.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetMe.

        The name of the user  # noqa: E501

        :param name: The name of this GetMe.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this GetMe.  # noqa: E501

        The URL of the resource  # noqa: E501

        :return: The url of this GetMe.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetMe.

        The URL of the resource  # noqa: E501

        :param url: The url of this GetMe.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def user_group(self):
        """Gets the user_group of this GetMe.  # noqa: E501

        Url for the user group this user is in  # noqa: E501

        :return: The user_group of this GetMe.  # noqa: E501
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        """Sets the user_group of this GetMe.

        Url for the user group this user is in  # noqa: E501

        :param user_group: The user_group of this GetMe.  # noqa: E501
        :type: str
        """

        self._user_group = user_group

    @property
    def user_group_id(self):
        """Gets the user_group_id of this GetMe.  # noqa: E501

        Global id of the user group this user is in  # noqa: E501

        :return: The user_group_id of this GetMe.  # noqa: E501
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """Sets the user_group_id of this GetMe.

        Global id of the user group this user is in  # noqa: E501

        :param user_group_id: The user_group_id of this GetMe.  # noqa: E501
        :type: str
        """

        self._user_group_id = user_group_id

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
        if issubclass(GetMe, dict):
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
        if not isinstance(other, GetMe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
