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


class GetIoModule(object):
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
        'address': 'str',
        'created_by': 'str',
        'created_by_id': 'str',
        'guid': 'str',
        'name': 'str',
        'num_inputs': 'int',
        'num_outputs': 'int',
        'type': 'str'
    }

    attribute_map = {
        'address': 'address',
        'created_by': 'created_by',
        'created_by_id': 'created_by_id',
        'guid': 'guid',
        'name': 'name',
        'num_inputs': 'num_inputs',
        'num_outputs': 'num_outputs',
        'type': 'type'
    }

    def __init__(self, address=None, created_by=None, created_by_id=None, guid=None, name=None, num_inputs=None, num_outputs=None, type=None):  # noqa: E501
        """GetIoModule - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._created_by = None
        self._created_by_id = None
        self._guid = None
        self._name = None
        self._num_inputs = None
        self._num_outputs = None
        self._type = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if created_by is not None:
            self.created_by = created_by
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if guid is not None:
            self.guid = guid
        if name is not None:
            self.name = name
        if num_inputs is not None:
            self.num_inputs = num_inputs
        if num_outputs is not None:
            self.num_outputs = num_outputs
        if type is not None:
            self.type = type

    @property
    def address(self):
        """Gets the address of this GetIoModule.  # noqa: E501

        The address for connecting to the device. it can be a mac address or an ip depending on the type of io module  # noqa: E501

        :return: The address of this GetIoModule.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this GetIoModule.

        The address for connecting to the device. it can be a mac address or an ip depending on the type of io module  # noqa: E501

        :param address: The address of this GetIoModule.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def created_by(self):
        """Gets the created_by of this GetIoModule.  # noqa: E501

        The url to the description of the type of this io module  # noqa: E501

        :return: The created_by of this GetIoModule.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GetIoModule.

        The url to the description of the type of this io module  # noqa: E501

        :param created_by: The created_by of this GetIoModule.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetIoModule.  # noqa: E501

        The global id of the user who created this entry  # noqa: E501

        :return: The created_by_id of this GetIoModule.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetIoModule.

        The global id of the user who created this entry  # noqa: E501

        :param created_by_id: The created_by_id of this GetIoModule.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def guid(self):
        """Gets the guid of this GetIoModule.  # noqa: E501

        The global unique id across robots that identifies this io module  # noqa: E501

        :return: The guid of this GetIoModule.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetIoModule.

        The global unique id across robots that identifies this io module  # noqa: E501

        :param guid: The guid of this GetIoModule.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def name(self):
        """Gets the name of this GetIoModule.  # noqa: E501

        The name of the io module  # noqa: E501

        :return: The name of this GetIoModule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetIoModule.

        The name of the io module  # noqa: E501

        :param name: The name of this GetIoModule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def num_inputs(self):
        """Gets the num_inputs of this GetIoModule.  # noqa: E501

        The number of inputs that the io module has  # noqa: E501

        :return: The num_inputs of this GetIoModule.  # noqa: E501
        :rtype: int
        """
        return self._num_inputs

    @num_inputs.setter
    def num_inputs(self, num_inputs):
        """Sets the num_inputs of this GetIoModule.

        The number of inputs that the io module has  # noqa: E501

        :param num_inputs: The num_inputs of this GetIoModule.  # noqa: E501
        :type: int
        """

        self._num_inputs = num_inputs

    @property
    def num_outputs(self):
        """Gets the num_outputs of this GetIoModule.  # noqa: E501

        The number or outputs that the io module has  # noqa: E501

        :return: The num_outputs of this GetIoModule.  # noqa: E501
        :rtype: int
        """
        return self._num_outputs

    @num_outputs.setter
    def num_outputs(self, num_outputs):
        """Sets the num_outputs of this GetIoModule.

        The number or outputs that the io module has  # noqa: E501

        :param num_outputs: The num_outputs of this GetIoModule.  # noqa: E501
        :type: int
        """

        self._num_outputs = num_outputs

    @property
    def type(self):
        """Gets the type of this GetIoModule.  # noqa: E501

        The type of the io module. currently supported devices [bluetooth, wise].  # noqa: E501

        :return: The type of this GetIoModule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetIoModule.

        The type of the io module. currently supported devices [bluetooth, wise].  # noqa: E501

        :param type: The type of this GetIoModule.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(GetIoModule, dict):
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
        if not isinstance(other, GetIoModule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
