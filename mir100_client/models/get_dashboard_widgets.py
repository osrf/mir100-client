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


class GetDashboardWidgets(object):
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
        'dashboard_id': 'str',
        'guid': 'str',
        'url': 'str'
    }

    attribute_map = {
        'dashboard_id': 'dashboard_id',
        'guid': 'guid',
        'url': 'url'
    }

    def __init__(self, dashboard_id=None, guid=None, url=None):  # noqa: E501
        """GetDashboardWidgets - a model defined in Swagger"""  # noqa: E501
        self._dashboard_id = None
        self._guid = None
        self._url = None
        self.discriminator = None
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if guid is not None:
            self.guid = guid
        if url is not None:
            self.url = url

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this GetDashboardWidgets.  # noqa: E501

        The guid of the dashboard this widget belongs to  # noqa: E501

        :return: The dashboard_id of this GetDashboardWidgets.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this GetDashboardWidgets.

        The guid of the dashboard this widget belongs to  # noqa: E501

        :param dashboard_id: The dashboard_id of this GetDashboardWidgets.  # noqa: E501
        :type: str
        """

        self._dashboard_id = dashboard_id

    @property
    def guid(self):
        """Gets the guid of this GetDashboardWidgets.  # noqa: E501

        The global id unique across robots that identifies this widget  # noqa: E501

        :return: The guid of this GetDashboardWidgets.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetDashboardWidgets.

        The global id unique across robots that identifies this widget  # noqa: E501

        :param guid: The guid of this GetDashboardWidgets.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def url(self):
        """Gets the url of this GetDashboardWidgets.  # noqa: E501

        The URL of the resource  # noqa: E501

        :return: The url of this GetDashboardWidgets.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetDashboardWidgets.

        The URL of the resource  # noqa: E501

        :param url: The url of this GetDashboardWidgets.  # noqa: E501
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
        if issubclass(GetDashboardWidgets, dict):
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
        if not isinstance(other, GetDashboardWidgets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
