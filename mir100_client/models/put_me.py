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


class PutMe(object):
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
        'email': 'str',
        'name': 'str',
        'password': 'str',
        'pincode': 'str',
        'single_dashboard': 'bool',
        'user_group_id': 'str',
        'username': 'str'
    }

    attribute_map = {
        'dashboard_id': 'dashboard_id',
        'email': 'email',
        'name': 'name',
        'password': 'password',
        'pincode': 'pincode',
        'single_dashboard': 'single_dashboard',
        'user_group_id': 'user_group_id',
        'username': 'username'
    }

    def __init__(self, dashboard_id=None, email=None, name=None, password=None, pincode=None, single_dashboard=None, user_group_id=None, username=None):  # noqa: E501
        """PutMe - a model defined in Swagger"""  # noqa: E501
        self._dashboard_id = None
        self._email = None
        self._name = None
        self._password = None
        self._pincode = None
        self._single_dashboard = None
        self._user_group_id = None
        self._username = None
        self.discriminator = None
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if email is not None:
            self.email = email
        if name is not None:
            self.name = name
        if password is not None:
            self.password = password
        if pincode is not None:
            self.pincode = pincode
        if single_dashboard is not None:
            self.single_dashboard = single_dashboard
        if user_group_id is not None:
            self.user_group_id = user_group_id
        if username is not None:
            self.username = username

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this PutMe.  # noqa: E501


        :return: The dashboard_id of this PutMe.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this PutMe.


        :param dashboard_id: The dashboard_id of this PutMe.  # noqa: E501
        :type: str
        """

        self._dashboard_id = dashboard_id

    @property
    def email(self):
        """Gets the email of this PutMe.  # noqa: E501


        :return: The email of this PutMe.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PutMe.


        :param email: The email of this PutMe.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def name(self):
        """Gets the name of this PutMe.  # noqa: E501

        Min length: 2, Max length: 255  # noqa: E501

        :return: The name of this PutMe.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutMe.

        Min length: 2, Max length: 255  # noqa: E501

        :param name: The name of this PutMe.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def password(self):
        """Gets the password of this PutMe.  # noqa: E501


        :return: The password of this PutMe.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PutMe.


        :param password: The password of this PutMe.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def pincode(self):
        """Gets the pincode of this PutMe.  # noqa: E501


        :return: The pincode of this PutMe.  # noqa: E501
        :rtype: str
        """
        return self._pincode

    @pincode.setter
    def pincode(self, pincode):
        """Sets the pincode of this PutMe.


        :param pincode: The pincode of this PutMe.  # noqa: E501
        :type: str
        """

        self._pincode = pincode

    @property
    def single_dashboard(self):
        """Gets the single_dashboard of this PutMe.  # noqa: E501


        :return: The single_dashboard of this PutMe.  # noqa: E501
        :rtype: bool
        """
        return self._single_dashboard

    @single_dashboard.setter
    def single_dashboard(self, single_dashboard):
        """Sets the single_dashboard of this PutMe.


        :param single_dashboard: The single_dashboard of this PutMe.  # noqa: E501
        :type: bool
        """

        self._single_dashboard = single_dashboard

    @property
    def user_group_id(self):
        """Gets the user_group_id of this PutMe.  # noqa: E501


        :return: The user_group_id of this PutMe.  # noqa: E501
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """Sets the user_group_id of this PutMe.


        :param user_group_id: The user_group_id of this PutMe.  # noqa: E501
        :type: str
        """

        self._user_group_id = user_group_id

    @property
    def username(self):
        """Gets the username of this PutMe.  # noqa: E501

        Min length: 2, Max length: 63  # noqa: E501

        :return: The username of this PutMe.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this PutMe.

        Min length: 2, Max length: 63  # noqa: E501

        :param username: The username of this PutMe.  # noqa: E501
        :type: str
        """

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
        if issubclass(PutMe, dict):
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
        if not isinstance(other, PutMe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
