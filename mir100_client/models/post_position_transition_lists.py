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


class PostPositionTransitionLists(object):
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
        'goal_pos_id': 'str',
        'guid': 'str',
        'mission_id': 'str',
        'start_pos_id': 'str'
    }

    attribute_map = {
        'created_by_id': 'created_by_id',
        'goal_pos_id': 'goal_pos_id',
        'guid': 'guid',
        'mission_id': 'mission_id',
        'start_pos_id': 'start_pos_id'
    }

    def __init__(self, created_by_id=None, goal_pos_id=None, guid=None, mission_id=None, start_pos_id=None):  # noqa: E501
        """PostPositionTransitionLists - a model defined in Swagger"""  # noqa: E501
        self._created_by_id = None
        self._goal_pos_id = None
        self._guid = None
        self._mission_id = None
        self._start_pos_id = None
        self.discriminator = None
        if created_by_id is not None:
            self.created_by_id = created_by_id
        self.goal_pos_id = goal_pos_id
        if guid is not None:
            self.guid = guid
        self.mission_id = mission_id
        self.start_pos_id = start_pos_id

    @property
    def created_by_id(self):
        """Gets the created_by_id of this PostPositionTransitionLists.  # noqa: E501


        :return: The created_by_id of this PostPositionTransitionLists.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this PostPositionTransitionLists.


        :param created_by_id: The created_by_id of this PostPositionTransitionLists.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def goal_pos_id(self):
        """Gets the goal_pos_id of this PostPositionTransitionLists.  # noqa: E501


        :return: The goal_pos_id of this PostPositionTransitionLists.  # noqa: E501
        :rtype: str
        """
        return self._goal_pos_id

    @goal_pos_id.setter
    def goal_pos_id(self, goal_pos_id):
        """Sets the goal_pos_id of this PostPositionTransitionLists.


        :param goal_pos_id: The goal_pos_id of this PostPositionTransitionLists.  # noqa: E501
        :type: str
        """
        if goal_pos_id is None:
            raise ValueError("Invalid value for `goal_pos_id`, must not be `None`")  # noqa: E501

        self._goal_pos_id = goal_pos_id

    @property
    def guid(self):
        """Gets the guid of this PostPositionTransitionLists.  # noqa: E501


        :return: The guid of this PostPositionTransitionLists.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this PostPositionTransitionLists.


        :param guid: The guid of this PostPositionTransitionLists.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def mission_id(self):
        """Gets the mission_id of this PostPositionTransitionLists.  # noqa: E501


        :return: The mission_id of this PostPositionTransitionLists.  # noqa: E501
        :rtype: str
        """
        return self._mission_id

    @mission_id.setter
    def mission_id(self, mission_id):
        """Sets the mission_id of this PostPositionTransitionLists.


        :param mission_id: The mission_id of this PostPositionTransitionLists.  # noqa: E501
        :type: str
        """
        if mission_id is None:
            raise ValueError("Invalid value for `mission_id`, must not be `None`")  # noqa: E501

        self._mission_id = mission_id

    @property
    def start_pos_id(self):
        """Gets the start_pos_id of this PostPositionTransitionLists.  # noqa: E501


        :return: The start_pos_id of this PostPositionTransitionLists.  # noqa: E501
        :rtype: str
        """
        return self._start_pos_id

    @start_pos_id.setter
    def start_pos_id(self, start_pos_id):
        """Sets the start_pos_id of this PostPositionTransitionLists.


        :param start_pos_id: The start_pos_id of this PostPositionTransitionLists.  # noqa: E501
        :type: str
        """
        if start_pos_id is None:
            raise ValueError("Invalid value for `start_pos_id`, must not be `None`")  # noqa: E501

        self._start_pos_id = start_pos_id

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
        if issubclass(PostPositionTransitionLists, dict):
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
        if not isinstance(other, PostPositionTransitionLists):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
