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


class PutMap(object):
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
        'map': 'str',
        'metadata': 'str',
        'name': 'str',
        'one_way_map': 'str',
        'origin_theta': 'float',
        'origin_x': 'float',
        'origin_y': 'float',
        'resolution': 'float'
    }

    attribute_map = {
        'map': 'map',
        'metadata': 'metadata',
        'name': 'name',
        'one_way_map': 'one_way_map',
        'origin_theta': 'origin_theta',
        'origin_x': 'origin_x',
        'origin_y': 'origin_y',
        'resolution': 'resolution'
    }

    def __init__(self, map=None, metadata=None, name=None, one_way_map=None, origin_theta=None, origin_x=None, origin_y=None, resolution=None):  # noqa: E501
        """PutMap - a model defined in Swagger"""  # noqa: E501
        self._map = None
        self._metadata = None
        self._name = None
        self._one_way_map = None
        self._origin_theta = None
        self._origin_x = None
        self._origin_y = None
        self._resolution = None
        self.discriminator = None
        if map is not None:
            self.map = map
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if one_way_map is not None:
            self.one_way_map = one_way_map
        if origin_theta is not None:
            self.origin_theta = origin_theta
        if origin_x is not None:
            self.origin_x = origin_x
        if origin_y is not None:
            self.origin_y = origin_y
        if resolution is not None:
            self.resolution = resolution

    @property
    def map(self):
        """Gets the map of this PutMap.  # noqa: E501


        :return: The map of this PutMap.  # noqa: E501
        :rtype: str
        """
        return self._map

    @map.setter
    def map(self, map):
        """Sets the map of this PutMap.


        :param map: The map of this PutMap.  # noqa: E501
        :type: str
        """

        self._map = map

    @property
    def metadata(self):
        """Gets the metadata of this PutMap.  # noqa: E501


        :return: The metadata of this PutMap.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PutMap.


        :param metadata: The metadata of this PutMap.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this PutMap.  # noqa: E501

        Min length: 1, Max length: 40  # noqa: E501

        :return: The name of this PutMap.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutMap.

        Min length: 1, Max length: 40  # noqa: E501

        :param name: The name of this PutMap.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def one_way_map(self):
        """Gets the one_way_map of this PutMap.  # noqa: E501


        :return: The one_way_map of this PutMap.  # noqa: E501
        :rtype: str
        """
        return self._one_way_map

    @one_way_map.setter
    def one_way_map(self, one_way_map):
        """Sets the one_way_map of this PutMap.


        :param one_way_map: The one_way_map of this PutMap.  # noqa: E501
        :type: str
        """

        self._one_way_map = one_way_map

    @property
    def origin_theta(self):
        """Gets the origin_theta of this PutMap.  # noqa: E501


        :return: The origin_theta of this PutMap.  # noqa: E501
        :rtype: float
        """
        return self._origin_theta

    @origin_theta.setter
    def origin_theta(self, origin_theta):
        """Sets the origin_theta of this PutMap.


        :param origin_theta: The origin_theta of this PutMap.  # noqa: E501
        :type: float
        """

        self._origin_theta = origin_theta

    @property
    def origin_x(self):
        """Gets the origin_x of this PutMap.  # noqa: E501


        :return: The origin_x of this PutMap.  # noqa: E501
        :rtype: float
        """
        return self._origin_x

    @origin_x.setter
    def origin_x(self, origin_x):
        """Sets the origin_x of this PutMap.


        :param origin_x: The origin_x of this PutMap.  # noqa: E501
        :type: float
        """

        self._origin_x = origin_x

    @property
    def origin_y(self):
        """Gets the origin_y of this PutMap.  # noqa: E501


        :return: The origin_y of this PutMap.  # noqa: E501
        :rtype: float
        """
        return self._origin_y

    @origin_y.setter
    def origin_y(self, origin_y):
        """Sets the origin_y of this PutMap.


        :param origin_y: The origin_y of this PutMap.  # noqa: E501
        :type: float
        """

        self._origin_y = origin_y

    @property
    def resolution(self):
        """Gets the resolution of this PutMap.  # noqa: E501


        :return: The resolution of this PutMap.  # noqa: E501
        :rtype: float
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this PutMap.


        :param resolution: The resolution of this PutMap.  # noqa: E501
        :type: float
        """

        self._resolution = resolution

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
        if issubclass(PutMap, dict):
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
        if not isinstance(other, PutMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
