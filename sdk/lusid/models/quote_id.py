# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2362
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class QuoteId(object):
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
        'quote_series_id': 'QuoteSeriesId',
        'effective_at': 'str'
    }

    attribute_map = {
        'quote_series_id': 'quoteSeriesId',
        'effective_at': 'effectiveAt'
    }

    required_map = {
        'quote_series_id': 'required',
        'effective_at': 'required'
    }

    def __init__(self, quote_series_id=None, effective_at=None):  # noqa: E501
        """
        QuoteId - a model defined in OpenAPI

        :param quote_series_id:  (required)
        :type quote_series_id: lusid.QuoteSeriesId
        :param effective_at:  The effective datetime or cut label at which the quote is valid from. (required)
        :type effective_at: str

        """  # noqa: E501

        self._quote_series_id = None
        self._effective_at = None
        self.discriminator = None

        self.quote_series_id = quote_series_id
        self.effective_at = effective_at

    @property
    def quote_series_id(self):
        """Gets the quote_series_id of this QuoteId.  # noqa: E501


        :return: The quote_series_id of this QuoteId.  # noqa: E501
        :rtype: QuoteSeriesId
        """
        return self._quote_series_id

    @quote_series_id.setter
    def quote_series_id(self, quote_series_id):
        """Sets the quote_series_id of this QuoteId.


        :param quote_series_id: The quote_series_id of this QuoteId.  # noqa: E501
        :type: QuoteSeriesId
        """
        if quote_series_id is None:
            raise ValueError("Invalid value for `quote_series_id`, must not be `None`")  # noqa: E501

        self._quote_series_id = quote_series_id

    @property
    def effective_at(self):
        """Gets the effective_at of this QuoteId.  # noqa: E501

        The effective datetime or cut label at which the quote is valid from.  # noqa: E501

        :return: The effective_at of this QuoteId.  # noqa: E501
        :rtype: str
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this QuoteId.

        The effective datetime or cut label at which the quote is valid from.  # noqa: E501

        :param effective_at: The effective_at of this QuoteId.  # noqa: E501
        :type: str
        """
        if effective_at is None:
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

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
        if not isinstance(other, QuoteId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
