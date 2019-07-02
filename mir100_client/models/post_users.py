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


class PostUsers(object):
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
        'dashboard_id': 'str',
        'email': 'str',
        'guid': 'str',
        'name': 'str',
        'password': 'str',
        'pincode': 'str',
        'single_dashboard': 'bool',
        'user_group_id': 'str',
        'username': 'str'
    }

    attribute_map = {
        'created_by_id': 'created_by_id',
        'dashboard_id': 'dashboard_id',
        'email': 'email',
        'guid': 'guid',
        'name': 'name',
        'password': 'password',
        'pincode': 'pincode',
        'single_dashboard': 'single_dashboard',
        'user_group_id': 'user_group_id',
        'username': 'username'
    }

    def __init__(self, created_by_id=None, dashboard_id=None, email=None, guid=None, name=None, password=None, pincode=None, single_dashboard=None, user_group_id=None, username=None):  # noqa: E501
        """PostUsers - a model defined in Swagger"""  # noqa: E501
        self._created_by_id = None
        self._dashboard_id = None
        self._email = None
        self._guid = None
        self._name = None
        self._password = None
        self._pincode = None
        self._single_dashboard = None
        self._user_group_id = None
        self._username = None
        self.discriminator = None
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if email is not None:
            self.email = email
        if guid is not None:
            self.guid = guid
        self.name = name
        self.password = password
        if pincode is not None:
            self.pincode = pincode
        if single_dashboard is not None:
            self.single_dashboard = single_dashboard
        self.user_group_id = user_group_id
        self.username = username

    @property
    def created_by_id(self):
        """Gets the created_by_id of this PostUsers.  # noqa: E501


        :return: The created_by_id of this PostUsers.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this PostUsers.


        :param created_by_id: The created_by_id of this PostUsers.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this PostUsers.  # noqa: E501


        :return: The dashboard_id of this PostUsers.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this PostUsers.


        :param dashboard_id: The dashboard_id of this PostUsers.  # noqa: E501
        :type: str
        """

        self._dashboard_id = dashboard_id

    @property
    def email(self):
        """Gets the email of this PostUsers.  # noqa: E501


        :return: The email of this PostUsers.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PostUsers.


        :param email: The email of this PostUsers.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def guid(self):
        """Gets the guid of this PostUsers.  # noqa: E501


        :return: The guid of this PostUsers.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this PostUsers.


        :param guid: The guid of this PostUsers.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def name(self):
        """Gets the name of this PostUsers.  # noqa: E501

        Min length: 2, Max length: 255  # noqa: E501

        :return: The name of this PostUsers.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostUsers.

        Min length: 2, Max length: 255  # noqa: E501

        :param name: The name of this PostUsers.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this PostUsers.  # noqa: E501


        :return: The password of this PostUsers.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PostUsers.


        :param password: The password of this PostUsers.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def pincode(self):
        """Gets the pincode of this PostUsers.  # noqa: E501


        :return: The pincode of this PostUsers.  # noqa: E501
        :rtype: str
        """
        return self._pincode

    @pincode.setter
    def pincode(self, pincode):
        """Sets the pincode of this PostUsers.


        :param pincode: The pincode of this PostUsers.  # noqa: E501
        :type: str
        """

        self._pincode = pincode

    @property
    def single_dashboard(self):
        """Gets the single_dashboard of this PostUsers.  # noqa: E501


        :return: The single_dashboard of this PostUsers.  # noqa: E501
        :rtype: bool
        """
        return self._single_dashboard

    @single_dashboard.setter
    def single_dashboard(self, single_dashboard):
        """Sets the single_dashboard of this PostUsers.


        :param single_dashboard: The single_dashboard of this PostUsers.  # noqa: E501
        :type: bool
        """

        self._single_dashboard = single_dashboard

    @property
    def user_group_id(self):
        """Gets the user_group_id of this PostUsers.  # noqa: E501


        :return: The user_group_id of this PostUsers.  # noqa: E501
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """Sets the user_group_id of this PostUsers.


        :param user_group_id: The user_group_id of this PostUsers.  # noqa: E501
        :type: str
        """
        if user_group_id is None:
            raise ValueError("Invalid value for `user_group_id`, must not be `None`")  # noqa: E501

        self._user_group_id = user_group_id

    @property
    def username(self):
        """Gets the username of this PostUsers.  # noqa: E501

        Min length: 2, Max length: 63  # noqa: E501

        :return: The username of this PostUsers.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this PostUsers.

        Min length: 2, Max length: 63  # noqa: E501

        :param username: The username of this PostUsers.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

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
        if issubclass(PostUsers, dict):
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
        if not isinstance(other, PostUsers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
