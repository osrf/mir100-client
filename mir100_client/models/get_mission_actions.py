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


class GetMissionActions(object):
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
        'action_type': 'str',
        'guid': 'str',
        'mission_id': 'str',
        'parameters': 'list[object]',
        'priority': 'int',
        'url': 'str'
    }

    attribute_map = {
        'action_type': 'action_type',
        'guid': 'guid',
        'mission_id': 'mission_id',
        'parameters': 'parameters',
        'priority': 'priority',
        'url': 'url'
    }

    def __init__(self, action_type=None, guid=None, mission_id=None, parameters=None, priority=None, url=None):  # noqa: E501
        """GetMissionActions - a model defined in Swagger"""  # noqa: E501
        self._action_type = None
        self._guid = None
        self._mission_id = None
        self._parameters = None
        self._priority = None
        self._url = None
        self.discriminator = None
        if action_type is not None:
            self.action_type = action_type
        if guid is not None:
            self.guid = guid
        if mission_id is not None:
            self.mission_id = mission_id
        if parameters is not None:
            self.parameters = parameters
        if priority is not None:
            self.priority = priority
        if url is not None:
            self.url = url

    @property
    def action_type(self):
        """Gets the action_type of this GetMissionActions.  # noqa: E501

        The id of the type of action  # noqa: E501

        :return: The action_type of this GetMissionActions.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this GetMissionActions.

        The id of the type of action  # noqa: E501

        :param action_type: The action_type of this GetMissionActions.  # noqa: E501
        :type: str
        """

        self._action_type = action_type

    @property
    def guid(self):
        """Gets the guid of this GetMissionActions.  # noqa: E501

        The global id unique across robots that identifies this mission  # noqa: E501

        :return: The guid of this GetMissionActions.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetMissionActions.

        The global id unique across robots that identifies this mission  # noqa: E501

        :param guid: The guid of this GetMissionActions.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def mission_id(self):
        """Gets the mission_id of this GetMissionActions.  # noqa: E501

        The id of the mission the action belongs to  # noqa: E501

        :return: The mission_id of this GetMissionActions.  # noqa: E501
        :rtype: str
        """
        return self._mission_id

    @mission_id.setter
    def mission_id(self, mission_id):
        """Sets the mission_id of this GetMissionActions.

        The id of the mission the action belongs to  # noqa: E501

        :param mission_id: The mission_id of this GetMissionActions.  # noqa: E501
        :type: str
        """

        self._mission_id = mission_id

    @property
    def parameters(self):
        """Gets the parameters of this GetMissionActions.  # noqa: E501


        :return: The parameters of this GetMissionActions.  # noqa: E501
        :rtype: list[object]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this GetMissionActions.


        :param parameters: The parameters of this GetMissionActions.  # noqa: E501
        :type: list[object]
        """

        self._parameters = parameters

    @property
    def priority(self):
        """Gets the priority of this GetMissionActions.  # noqa: E501

        The priority of the action  # noqa: E501

        :return: The priority of this GetMissionActions.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this GetMissionActions.

        The priority of the action  # noqa: E501

        :param priority: The priority of this GetMissionActions.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def url(self):
        """Gets the url of this GetMissionActions.  # noqa: E501

        The URL of the resource  # noqa: E501

        :return: The url of this GetMissionActions.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetMissionActions.

        The URL of the resource  # noqa: E501

        :param url: The url of this GetMissionActions.  # noqa: E501
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
        if issubclass(GetMissionActions, dict):
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
        if not isinstance(other, GetMissionActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
