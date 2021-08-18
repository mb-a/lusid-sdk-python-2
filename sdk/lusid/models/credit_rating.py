# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3401
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class CreditRating(object):
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
        'rating_source': 'str',
        'rating': 'str'
    }

    attribute_map = {
        'rating_source': 'ratingSource',
        'rating': 'rating'
    }

    required_map = {
        'rating_source': 'required',
        'rating': 'required'
    }

    def __init__(self, rating_source=None, rating=None):  # noqa: E501
        """
        CreditRating - a model defined in OpenAPI

        :param rating_source:  The provider of the credit rating, which will typically be an agency such as Moody's or Standard and Poor. (required)
        :type rating_source: str
        :param rating:  The credit rating provided by the rating source. This would expected to be consistent with the rating scheme of that agency/source. (required)
        :type rating: str

        """  # noqa: E501

        self._rating_source = None
        self._rating = None
        self.discriminator = None

        self.rating_source = rating_source
        self.rating = rating

    @property
    def rating_source(self):
        """Gets the rating_source of this CreditRating.  # noqa: E501

        The provider of the credit rating, which will typically be an agency such as Moody's or Standard and Poor.  # noqa: E501

        :return: The rating_source of this CreditRating.  # noqa: E501
        :rtype: str
        """
        return self._rating_source

    @rating_source.setter
    def rating_source(self, rating_source):
        """Sets the rating_source of this CreditRating.

        The provider of the credit rating, which will typically be an agency such as Moody's or Standard and Poor.  # noqa: E501

        :param rating_source: The rating_source of this CreditRating.  # noqa: E501
        :type: str
        """
        if rating_source is None:
            raise ValueError("Invalid value for `rating_source`, must not be `None`")  # noqa: E501
        if rating_source is not None and len(rating_source) > 64:
            raise ValueError("Invalid value for `rating_source`, length must be less than or equal to `64`")  # noqa: E501
        if rating_source is not None and len(rating_source) < 1:
            raise ValueError("Invalid value for `rating_source`, length must be greater than or equal to `1`")  # noqa: E501
        if (rating_source is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', rating_source)):  # noqa: E501
            raise ValueError(r"Invalid value for `rating_source`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._rating_source = rating_source

    @property
    def rating(self):
        """Gets the rating of this CreditRating.  # noqa: E501

        The credit rating provided by the rating source. This would expected to be consistent with the rating scheme of that agency/source.  # noqa: E501

        :return: The rating of this CreditRating.  # noqa: E501
        :rtype: str
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this CreditRating.

        The credit rating provided by the rating source. This would expected to be consistent with the rating scheme of that agency/source.  # noqa: E501

        :param rating: The rating of this CreditRating.  # noqa: E501
        :type: str
        """
        if rating is None:
            raise ValueError("Invalid value for `rating`, must not be `None`")  # noqa: E501
        if rating is not None and len(rating) > 64:
            raise ValueError("Invalid value for `rating`, length must be less than or equal to `64`")  # noqa: E501
        if rating is not None and len(rating) < 1:
            raise ValueError("Invalid value for `rating`, length must be greater than or equal to `1`")  # noqa: E501
        if (rating is not None and not re.search(r'^[a-zA-Z0-9\-+\/]+$', rating)):  # noqa: E501
            raise ValueError(r"Invalid value for `rating`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-+\/]+$/`")  # noqa: E501

        self._rating = rating

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
        if not isinstance(other, CreditRating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
