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


class GetWifiConnection(object):
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
        'bssid': 'str',
        'connected': 'bool',
        'device': 'str',
        'dns': 'str',
        'ip_address': 'str',
        'last_connected': 'str',
        'mac': 'str',
        'name': 'str',
        'netmask': 'str',
        'security': 'str',
        'type': 'str',
        'url': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'bssid': 'bssid',
        'connected': 'connected',
        'device': 'device',
        'dns': 'dns',
        'ip_address': 'ip_address',
        'last_connected': 'last_connected',
        'mac': 'mac',
        'name': 'name',
        'netmask': 'netmask',
        'security': 'security',
        'type': 'type',
        'url': 'url',
        'uuid': 'uuid'
    }

    def __init__(self, bssid=None, connected=None, device=None, dns=None, ip_address=None, last_connected=None, mac=None, name=None, netmask=None, security=None, type=None, url=None, uuid=None):  # noqa: E501
        """GetWifiConnection - a model defined in Swagger"""  # noqa: E501
        self._bssid = None
        self._connected = None
        self._device = None
        self._dns = None
        self._ip_address = None
        self._last_connected = None
        self._mac = None
        self._name = None
        self._netmask = None
        self._security = None
        self._type = None
        self._url = None
        self._uuid = None
        self.discriminator = None
        if bssid is not None:
            self.bssid = bssid
        if connected is not None:
            self.connected = connected
        if device is not None:
            self.device = device
        if dns is not None:
            self.dns = dns
        if ip_address is not None:
            self.ip_address = ip_address
        if last_connected is not None:
            self.last_connected = last_connected
        if mac is not None:
            self.mac = mac
        if name is not None:
            self.name = name
        if netmask is not None:
            self.netmask = netmask
        if security is not None:
            self.security = security
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if uuid is not None:
            self.uuid = uuid

    @property
    def bssid(self):
        """Gets the bssid of this GetWifiConnection.  # noqa: E501

        Access point mac address  # noqa: E501

        :return: The bssid of this GetWifiConnection.  # noqa: E501
        :rtype: str
        """
        return self._bssid

    @bssid.setter
    def bssid(self, bssid):
        """Sets the bssid of this GetWifiConnection.

        Access point mac address  # noqa: E501

        :param bssid: The bssid of this GetWifiConnection.  # noqa: E501
        :type: str
        """

        self._bssid = bssid

    @property
    def connected(self):
        """Gets the connected of this GetWifiConnection.  # noqa: E501

        Connected to the network of this connection  # noqa: E501

        :return: The connected of this GetWifiConnection.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this GetWifiConnection.

        Connected to the network of this connection  # noqa: E501

        :param connected: The connected of this GetWifiConnection.  # noqa: E501
        :type: bool
        """

        self._connected = connected

    @property
    def device(self):
        """Gets the device of this GetWifiConnection.  # noqa: E501

        Device to use for this connection  # noqa: E501

        :return: The device of this GetWifiConnection.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this GetWifiConnection.

        Device to use for this connection  # noqa: E501

        :param device: The device of this GetWifiConnection.  # noqa: E501
        :type: str
        """

        self._device = device

    @property
    def dns(self):
        """Gets the dns of this GetWifiConnection.  # noqa: E501

        Dnss for the connection  # noqa: E501

        :return: The dns of this GetWifiConnection.  # noqa: E501
        :rtype: str
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this GetWifiConnection.

        Dnss for the connection  # noqa: E501

        :param dns: The dns of this GetWifiConnection.  # noqa: E501
        :type: str
        """

        self._dns = dns

    @property
    def ip_address(self):
        """Gets the ip_address of this GetWifiConnection.  # noqa: E501

        Ip address for the connection  # noqa: E501

        :return: The ip_address of this GetWifiConnection.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this GetWifiConnection.

        Ip address for the connection  # noqa: E501

        :param ip_address: The ip_address of this GetWifiConnection.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def last_connected(self):
        """Gets the last_connected of this GetWifiConnection.  # noqa: E501

        Date and time for when the connection was last successfully connected  # noqa: E501

        :return: The last_connected of this GetWifiConnection.  # noqa: E501
        :rtype: str
        """
        return self._last_connected

    @last_connected.setter
    def last_connected(self, last_connected):
        """Sets the last_connected of this GetWifiConnection.

        Date and time for when the connection was last successfully connected  # noqa: E501

        :param last_connected: The last_connected of this GetWifiConnection.  # noqa: E501
        :type: str
        """

        self._last_connected = last_connected

    @property
    def mac(self):
        """Gets the mac of this GetWifiConnection.  # noqa: E501

        Network adapter mac address  # noqa: E501

        :return: The mac of this GetWifiConnection.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this GetWifiConnection.

        Network adapter mac address  # noqa: E501

        :param mac: The mac of this GetWifiConnection.  # noqa: E501
        :type: str
        """

        self._mac = mac

    @property
    def name(self):
        """Gets the name of this GetWifiConnection.  # noqa: E501

        Name or id of the connection  # noqa: E501

        :return: The name of this GetWifiConnection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetWifiConnection.

        Name or id of the connection  # noqa: E501

        :param name: The name of this GetWifiConnection.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def netmask(self):
        """Gets the netmask of this GetWifiConnection.  # noqa: E501

        Netmask for the connection  # noqa: E501

        :return: The netmask of this GetWifiConnection.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this GetWifiConnection.

        Netmask for the connection  # noqa: E501

        :param netmask: The netmask of this GetWifiConnection.  # noqa: E501
        :type: str
        """

        self._netmask = netmask

    @property
    def security(self):
        """Gets the security of this GetWifiConnection.  # noqa: E501

        The security method used by the connection  # noqa: E501

        :return: The security of this GetWifiConnection.  # noqa: E501
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this GetWifiConnection.

        The security method used by the connection  # noqa: E501

        :param security: The security of this GetWifiConnection.  # noqa: E501
        :type: str
        """

        self._security = security

    @property
    def type(self):
        """Gets the type of this GetWifiConnection.  # noqa: E501

        Connection type e.g. 802-11-wireless  # noqa: E501

        :return: The type of this GetWifiConnection.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetWifiConnection.

        Connection type e.g. 802-11-wireless  # noqa: E501

        :param type: The type of this GetWifiConnection.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this GetWifiConnection.  # noqa: E501

        Specific connection  # noqa: E501

        :return: The url of this GetWifiConnection.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetWifiConnection.

        Specific connection  # noqa: E501

        :param url: The url of this GetWifiConnection.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def uuid(self):
        """Gets the uuid of this GetWifiConnection.  # noqa: E501

        Uuid of the connection  # noqa: E501

        :return: The uuid of this GetWifiConnection.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this GetWifiConnection.

        Uuid of the connection  # noqa: E501

        :param uuid: The uuid of this GetWifiConnection.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(GetWifiConnection, dict):
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
        if not isinstance(other, GetWifiConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
