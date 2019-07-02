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


class GetUserMePermissions(object):
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
        'endpoint': 'str',
        'guid': 'str',
        'permission_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'guid': 'guid',
        'permission_type': 'permission_type',
        'url': 'url'
    }

    def __init__(self, endpoint=None, guid=None, permission_type=None, url=None):  # noqa: E501
        """GetUserMePermissions - a model defined in Swagger"""  # noqa: E501
        self._endpoint = None
        self._guid = None
        self._permission_type = None
        self._url = None
        self.discriminator = None
        if endpoint is not None:
            self.endpoint = endpoint
        if guid is not None:
            self.guid = guid
        if permission_type is not None:
            self.permission_type = permission_type
        if url is not None:
            self.url = url

    @property
    def endpoint(self):
        """Gets the endpoint of this GetUserMePermissions.  # noqa: E501


        :return: The endpoint of this GetUserMePermissions.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this GetUserMePermissions.


        :param endpoint: The endpoint of this GetUserMePermissions.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def guid(self):
        """Gets the guid of this GetUserMePermissions.  # noqa: E501

        The global unique id across robots that identifies this permission  # noqa: E501

        :return: The guid of this GetUserMePermissions.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetUserMePermissions.

        The global unique id across robots that identifies this permission  # noqa: E501

        :param guid: The guid of this GetUserMePermissions.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def permission_type(self):
        """Gets the permission_type of this GetUserMePermissions.  # noqa: E501

        The permission type  # noqa: E501

        :return: The permission_type of this GetUserMePermissions.  # noqa: E501
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        """Sets the permission_type of this GetUserMePermissions.

        The permission type  # noqa: E501

        :param permission_type: The permission_type of this GetUserMePermissions.  # noqa: E501
        :type: str
        """

        self._permission_type = permission_type

    @property
    def url(self):
        """Gets the url of this GetUserMePermissions.  # noqa: E501

        The URL of the resource  # noqa: E501

        :return: The url of this GetUserMePermissions.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetUserMePermissions.

        The URL of the resource  # noqa: E501

        :param url: The url of this GetUserMePermissions.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(GetUserMePermissions, dict):
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
        if not isinstance(other, GetUserMePermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
