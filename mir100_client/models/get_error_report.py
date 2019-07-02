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


class GetErrorReport(object):
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
        'description': 'str',
        'download_url': 'str',
        'id': 'int',
        'module': 'str',
        'ready': 'bool',
        'time': 'datetime'
    }

    attribute_map = {
        'description': 'description',
        'download_url': 'download_url',
        'id': 'id',
        'module': 'module',
        'ready': 'ready',
        'time': 'time'
    }

    def __init__(self, description=None, download_url=None, id=None, module=None, ready=None, time=None):  # noqa: E501
        """GetErrorReport - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._download_url = None
        self._id = None
        self._module = None
        self._ready = None
        self._time = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if download_url is not None:
            self.download_url = download_url
        if id is not None:
            self.id = id
        if module is not None:
            self.module = module
        if ready is not None:
            self.ready = ready
        if time is not None:
            self.time = time

    @property
    def description(self):
        """Gets the description of this GetErrorReport.  # noqa: E501


        :return: The description of this GetErrorReport.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetErrorReport.


        :param description: The description of this GetErrorReport.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def download_url(self):
        """Gets the download_url of this GetErrorReport.  # noqa: E501

        The url to where the bag can be downloaded  # noqa: E501

        :return: The download_url of this GetErrorReport.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this GetErrorReport.

        The url to where the bag can be downloaded  # noqa: E501

        :param download_url: The download_url of this GetErrorReport.  # noqa: E501
        :type: str
        """

        self._download_url = download_url

    @property
    def id(self):
        """Gets the id of this GetErrorReport.  # noqa: E501

        Id of the autobag  # noqa: E501

        :return: The id of this GetErrorReport.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetErrorReport.

        Id of the autobag  # noqa: E501

        :param id: The id of this GetErrorReport.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def module(self):
        """Gets the module of this GetErrorReport.  # noqa: E501

        The module that created the autolog  # noqa: E501

        :return: The module of this GetErrorReport.  # noqa: E501
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this GetErrorReport.

        The module that created the autolog  # noqa: E501

        :param module: The module of this GetErrorReport.  # noqa: E501
        :type: str
        """

        self._module = module

    @property
    def ready(self):
        """Gets the ready of this GetErrorReport.  # noqa: E501

        Status of the rosbag  # noqa: E501

        :return: The ready of this GetErrorReport.  # noqa: E501
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this GetErrorReport.

        Status of the rosbag  # noqa: E501

        :param ready: The ready of this GetErrorReport.  # noqa: E501
        :type: bool
        """

        self._ready = ready

    @property
    def time(self):
        """Gets the time of this GetErrorReport.  # noqa: E501

        The time where the autolog was created  # noqa: E501

        :return: The time of this GetErrorReport.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this GetErrorReport.

        The time where the autolog was created  # noqa: E501

        :param time: The time of this GetErrorReport.  # noqa: E501
        :type: datetime
        """

        self._time = time

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
        if issubclass(GetErrorReport, dict):
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
        if not isinstance(other, GetErrorReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
