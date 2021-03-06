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


class GetPosition(object):
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
        'created_by': 'str',
        'created_by_id': 'str',
        'docking_offsets': 'str',
        'guid': 'str',
        'help_positions': 'str',
        'map': 'str',
        'map_id': 'str',
        'name': 'str',
        'orientation': 'float',
        'parent': 'str',
        'parent_id': 'str',
        'pos_x': 'float',
        'pos_y': 'float',
        'type': 'str',
        'type_id': 'int'
    }

    attribute_map = {
        'created_by': 'created_by',
        'created_by_id': 'created_by_id',
        'docking_offsets': 'docking_offsets',
        'guid': 'guid',
        'help_positions': 'help_positions',
        'map': 'map',
        'map_id': 'map_id',
        'name': 'name',
        'orientation': 'orientation',
        'parent': 'parent',
        'parent_id': 'parent_id',
        'pos_x': 'pos_x',
        'pos_y': 'pos_y',
        'type': 'type',
        'type_id': 'type_id'
    }

    def __init__(self, created_by=None, created_by_id=None, docking_offsets=None, guid=None, help_positions=None, map=None, map_id=None, name=None, orientation=None, parent=None, parent_id=None, pos_x=None, pos_y=None, type=None, type_id=None):  # noqa: E501
        """GetPosition - a model defined in Swagger"""  # noqa: E501
        self._created_by = None
        self._created_by_id = None
        self._docking_offsets = None
        self._guid = None
        self._help_positions = None
        self._map = None
        self._map_id = None
        self._name = None
        self._orientation = None
        self._parent = None
        self._parent_id = None
        self._pos_x = None
        self._pos_y = None
        self._type = None
        self._type_id = None
        self.discriminator = None
        if created_by is not None:
            self.created_by = created_by
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if docking_offsets is not None:
            self.docking_offsets = docking_offsets
        if guid is not None:
            self.guid = guid
        if help_positions is not None:
            self.help_positions = help_positions
        if map is not None:
            self.map = map
        if map_id is not None:
            self.map_id = map_id
        if name is not None:
            self.name = name
        if orientation is not None:
            self.orientation = orientation
        if parent is not None:
            self.parent = parent
        if parent_id is not None:
            self.parent_id = parent_id
        if pos_x is not None:
            self.pos_x = pos_x
        if pos_y is not None:
            self.pos_y = pos_y
        if type is not None:
            self.type = type
        if type_id is not None:
            self.type_id = type_id

    @property
    def created_by(self):
        """Gets the created_by of this GetPosition.  # noqa: E501

        The url to the description of the type of this position  # noqa: E501

        :return: The created_by of this GetPosition.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GetPosition.

        The url to the description of the type of this position  # noqa: E501

        :param created_by: The created_by of this GetPosition.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetPosition.  # noqa: E501

        The global id of the user who created this entry  # noqa: E501

        :return: The created_by_id of this GetPosition.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetPosition.

        The global id of the user who created this entry  # noqa: E501

        :param created_by_id: The created_by_id of this GetPosition.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def docking_offsets(self):
        """Gets the docking_offsets of this GetPosition.  # noqa: E501

        The url to the possible docking offset. if the position does not have a docking offset then this field is empty  # noqa: E501

        :return: The docking_offsets of this GetPosition.  # noqa: E501
        :rtype: str
        """
        return self._docking_offsets

    @docking_offsets.setter
    def docking_offsets(self, docking_offsets):
        """Sets the docking_offsets of this GetPosition.

        The url to the possible docking offset. if the position does not have a docking offset then this field is empty  # noqa: E501

        :param docking_offsets: The docking_offsets of this GetPosition.  # noqa: E501
        :type: str
        """

        self._docking_offsets = docking_offsets

    @property
    def guid(self):
        """Gets the guid of this GetPosition.  # noqa: E501

        The global id unique across robots that identifies this position  # noqa: E501

        :return: The guid of this GetPosition.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetPosition.

        The global id unique across robots that identifies this position  # noqa: E501

        :param guid: The guid of this GetPosition.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def help_positions(self):
        """Gets the help_positions of this GetPosition.  # noqa: E501


        :return: The help_positions of this GetPosition.  # noqa: E501
        :rtype: str
        """
        return self._help_positions

    @help_positions.setter
    def help_positions(self, help_positions):
        """Sets the help_positions of this GetPosition.


        :param help_positions: The help_positions of this GetPosition.  # noqa: E501
        :type: str
        """

        self._help_positions = help_positions

    @property
    def map(self):
        """Gets the map of this GetPosition.  # noqa: E501

        The url to the map this position belongs to  # noqa: E501

        :return: The map of this GetPosition.  # noqa: E501
        :rtype: str
        """
        return self._map

    @map.setter
    def map(self, map):
        """Sets the map of this GetPosition.

        The url to the map this position belongs to  # noqa: E501

        :param map: The map of this GetPosition.  # noqa: E501
        :type: str
        """

        self._map = map

    @property
    def map_id(self):
        """Gets the map_id of this GetPosition.  # noqa: E501

        The global id of the map this positions belongs to  # noqa: E501

        :return: The map_id of this GetPosition.  # noqa: E501
        :rtype: str
        """
        return self._map_id

    @map_id.setter
    def map_id(self, map_id):
        """Sets the map_id of this GetPosition.

        The global id of the map this positions belongs to  # noqa: E501

        :param map_id: The map_id of this GetPosition.  # noqa: E501
        :type: str
        """

        self._map_id = map_id

    @property
    def name(self):
        """Gets the name of this GetPosition.  # noqa: E501

        The name of the position  # noqa: E501

        :return: The name of this GetPosition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetPosition.

        The name of the position  # noqa: E501

        :param name: The name of this GetPosition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def orientation(self):
        """Gets the orientation of this GetPosition.  # noqa: E501

        The orientation of the position in degrees relative to origo of the underlying map  # noqa: E501

        :return: The orientation of this GetPosition.  # noqa: E501
        :rtype: float
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this GetPosition.

        The orientation of the position in degrees relative to origo of the underlying map  # noqa: E501

        :param orientation: The orientation of this GetPosition.  # noqa: E501
        :type: float
        """

        self._orientation = orientation

    @property
    def parent(self):
        """Gets the parent of this GetPosition.  # noqa: E501

        The url to the possible parent position. if the position does not have a parent position then this field is empty  # noqa: E501

        :return: The parent of this GetPosition.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this GetPosition.

        The url to the possible parent position. if the position does not have a parent position then this field is empty  # noqa: E501

        :param parent: The parent of this GetPosition.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def parent_id(self):
        """Gets the parent_id of this GetPosition.  # noqa: E501

        The global id of the possible parent position of the current position. a parent position is a position related to the current position, for instance the parent position of a trolley left entry position is the actual trolley position. if the position does not have a parent position then this field is empty  # noqa: E501

        :return: The parent_id of this GetPosition.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this GetPosition.

        The global id of the possible parent position of the current position. a parent position is a position related to the current position, for instance the parent position of a trolley left entry position is the actual trolley position. if the position does not have a parent position then this field is empty  # noqa: E501

        :param parent_id: The parent_id of this GetPosition.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def pos_x(self):
        """Gets the pos_x of this GetPosition.  # noqa: E501

        The x-coordinate of the position relative to origo of the underlying map  # noqa: E501

        :return: The pos_x of this GetPosition.  # noqa: E501
        :rtype: float
        """
        return self._pos_x

    @pos_x.setter
    def pos_x(self, pos_x):
        """Sets the pos_x of this GetPosition.

        The x-coordinate of the position relative to origo of the underlying map  # noqa: E501

        :param pos_x: The pos_x of this GetPosition.  # noqa: E501
        :type: float
        """

        self._pos_x = pos_x

    @property
    def pos_y(self):
        """Gets the pos_y of this GetPosition.  # noqa: E501

        The y-coordinate of the position relative to origo of the underlying map  # noqa: E501

        :return: The pos_y of this GetPosition.  # noqa: E501
        :rtype: float
        """
        return self._pos_y

    @pos_y.setter
    def pos_y(self, pos_y):
        """Sets the pos_y of this GetPosition.

        The y-coordinate of the position relative to origo of the underlying map  # noqa: E501

        :param pos_y: The pos_y of this GetPosition.  # noqa: E501
        :type: float
        """

        self._pos_y = pos_y

    @property
    def type(self):
        """Gets the type of this GetPosition.  # noqa: E501

        The url to the description of the type of this position  # noqa: E501

        :return: The type of this GetPosition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetPosition.

        The url to the description of the type of this position  # noqa: E501

        :param type: The type of this GetPosition.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def type_id(self):
        """Gets the type_id of this GetPosition.  # noqa: E501

        The type of position. see the general description above  # noqa: E501

        :return: The type_id of this GetPosition.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetPosition.

        The type of position. see the general description above  # noqa: E501

        :param type_id: The type_id of this GetPosition.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

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
        if issubclass(GetPosition, dict):
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
        if not isinstance(other, GetPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
