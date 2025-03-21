# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3430
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class PropertyInterval(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'value': 'PropertyValue',
        'effective_range': 'DateRange',
        'as_at_range': 'DateRange',
        'status': 'str'
    }

    attribute_map = {
        'value': 'value',
        'effective_range': 'effectiveRange',
        'as_at_range': 'asAtRange',
        'status': 'status'
    }

    required_map = {
        'value': 'required',
        'effective_range': 'required',
        'as_at_range': 'required',
        'status': 'required'
    }

    def __init__(self, value=None, effective_range=None, as_at_range=None, status=None):  # noqa: E501
        """
        PropertyInterval - a model defined in OpenAPI

        :param value:  (required)
        :type value: lusid.PropertyValue
        :param effective_range:  (required)
        :type effective_range: lusid.DateRange
        :param as_at_range:  (required)
        :type as_at_range: lusid.DateRange
        :param status:  Indicates whether the value is part of the prevailing effective date timeline for the requested asAt date, or whether it has been superseded by correctional activity (required)
        :type status: str

        """  # noqa: E501

        self._value = None
        self._effective_range = None
        self._as_at_range = None
        self._status = None
        self.discriminator = None

        self.value = value
        self.effective_range = effective_range
        self.as_at_range = as_at_range
        self.status = status

    @property
    def value(self):
        """Gets the value of this PropertyInterval.  # noqa: E501


        :return: The value of this PropertyInterval.  # noqa: E501
        :rtype: PropertyValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PropertyInterval.


        :param value: The value of this PropertyInterval.  # noqa: E501
        :type: PropertyValue
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def effective_range(self):
        """Gets the effective_range of this PropertyInterval.  # noqa: E501


        :return: The effective_range of this PropertyInterval.  # noqa: E501
        :rtype: DateRange
        """
        return self._effective_range

    @effective_range.setter
    def effective_range(self, effective_range):
        """Sets the effective_range of this PropertyInterval.


        :param effective_range: The effective_range of this PropertyInterval.  # noqa: E501
        :type: DateRange
        """
        if effective_range is None:
            raise ValueError("Invalid value for `effective_range`, must not be `None`")  # noqa: E501

        self._effective_range = effective_range

    @property
    def as_at_range(self):
        """Gets the as_at_range of this PropertyInterval.  # noqa: E501


        :return: The as_at_range of this PropertyInterval.  # noqa: E501
        :rtype: DateRange
        """
        return self._as_at_range

    @as_at_range.setter
    def as_at_range(self, as_at_range):
        """Sets the as_at_range of this PropertyInterval.


        :param as_at_range: The as_at_range of this PropertyInterval.  # noqa: E501
        :type: DateRange
        """
        if as_at_range is None:
            raise ValueError("Invalid value for `as_at_range`, must not be `None`")  # noqa: E501

        self._as_at_range = as_at_range

    @property
    def status(self):
        """Gets the status of this PropertyInterval.  # noqa: E501

        Indicates whether the value is part of the prevailing effective date timeline for the requested asAt date, or whether it has been superseded by correctional activity  # noqa: E501

        :return: The status of this PropertyInterval.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PropertyInterval.

        Indicates whether the value is part of the prevailing effective date timeline for the requested asAt date, or whether it has been superseded by correctional activity  # noqa: E501

        :param status: The status of this PropertyInterval.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PropertyInterval):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
