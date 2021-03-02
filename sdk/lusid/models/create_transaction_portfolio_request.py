# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2679
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class CreateTransactionPortfolioRequest(object):
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
        'display_name': 'str',
        'description': 'str',
        'code': 'str',
        'created': 'datetime',
        'base_currency': 'str',
        'corporate_action_source_id': 'ResourceId',
        'accounting_method': 'str',
        'sub_holding_keys': 'list[str]',
        'properties': 'dict(str, ModelProperty)'
    }

    attribute_map = {
        'display_name': 'displayName',
        'description': 'description',
        'code': 'code',
        'created': 'created',
        'base_currency': 'baseCurrency',
        'corporate_action_source_id': 'corporateActionSourceId',
        'accounting_method': 'accountingMethod',
        'sub_holding_keys': 'subHoldingKeys',
        'properties': 'properties'
    }

    required_map = {
        'display_name': 'required',
        'description': 'optional',
        'code': 'required',
        'created': 'optional',
        'base_currency': 'required',
        'corporate_action_source_id': 'optional',
        'accounting_method': 'optional',
        'sub_holding_keys': 'optional',
        'properties': 'optional'
    }

    def __init__(self, display_name=None, description=None, code=None, created=None, base_currency=None, corporate_action_source_id=None, accounting_method=None, sub_holding_keys=None, properties=None):  # noqa: E501
        """
        CreateTransactionPortfolioRequest - a model defined in OpenAPI

        :param display_name:  The name of the transaction portfolio. (required)
        :type display_name: str
        :param description:  A long form description of the transaction portfolio.
        :type description: str
        :param code:  The code that the transaction portfolio will be created with. Together with the scope this uniquely identifies the transaction portfolio. (required)
        :type code: str
        :param created:  The effective datetime at which the transaction portfolio will be created. No transactions can be added to the transaction portfolio before this date. Defaults to the current LUSID system datetime if not specified.
        :type created: datetime
        :param base_currency:  The base currency of the transaction portfolio. (required)
        :type base_currency: str
        :param corporate_action_source_id: 
        :type corporate_action_source_id: lusid.ResourceId
        :param accounting_method:  Determines the accounting treatment given to the transaction portfolio's tax lots. The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst
        :type accounting_method: str
        :param sub_holding_keys:  A set of unique transaction properties to group the transaction portfolio's holdings by. Each property must be from the 'Transaction' domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. 'Transaction/strategies/quantsignal'.
        :type sub_holding_keys: list[str]
        :param properties:  A set of unique portfolio properties to add to the transaction portfolio. Each property must be from the 'Portfolio' domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'. These properties must be pre-defined.
        :type properties: dict[str, lusid.ModelProperty]

        """  # noqa: E501

        self._display_name = None
        self._description = None
        self._code = None
        self._created = None
        self._base_currency = None
        self._corporate_action_source_id = None
        self._accounting_method = None
        self._sub_holding_keys = None
        self._properties = None
        self.discriminator = None

        self.display_name = display_name
        self.description = description
        self.code = code
        self.created = created
        self.base_currency = base_currency
        if corporate_action_source_id is not None:
            self.corporate_action_source_id = corporate_action_source_id
        if accounting_method is not None:
            self.accounting_method = accounting_method
        self.sub_holding_keys = sub_holding_keys
        self.properties = properties

    @property
    def display_name(self):
        """Gets the display_name of this CreateTransactionPortfolioRequest.  # noqa: E501

        The name of the transaction portfolio.  # noqa: E501

        :return: The display_name of this CreateTransactionPortfolioRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateTransactionPortfolioRequest.

        The name of the transaction portfolio.  # noqa: E501

        :param display_name: The display_name of this CreateTransactionPortfolioRequest.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this CreateTransactionPortfolioRequest.  # noqa: E501

        A long form description of the transaction portfolio.  # noqa: E501

        :return: The description of this CreateTransactionPortfolioRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTransactionPortfolioRequest.

        A long form description of the transaction portfolio.  # noqa: E501

        :param description: The description of this CreateTransactionPortfolioRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def code(self):
        """Gets the code of this CreateTransactionPortfolioRequest.  # noqa: E501

        The code that the transaction portfolio will be created with. Together with the scope this uniquely identifies the transaction portfolio.  # noqa: E501

        :return: The code of this CreateTransactionPortfolioRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreateTransactionPortfolioRequest.

        The code that the transaction portfolio will be created with. Together with the scope this uniquely identifies the transaction portfolio.  # noqa: E501

        :param code: The code of this CreateTransactionPortfolioRequest.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def created(self):
        """Gets the created of this CreateTransactionPortfolioRequest.  # noqa: E501

        The effective datetime at which the transaction portfolio will be created. No transactions can be added to the transaction portfolio before this date. Defaults to the current LUSID system datetime if not specified.  # noqa: E501

        :return: The created of this CreateTransactionPortfolioRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CreateTransactionPortfolioRequest.

        The effective datetime at which the transaction portfolio will be created. No transactions can be added to the transaction portfolio before this date. Defaults to the current LUSID system datetime if not specified.  # noqa: E501

        :param created: The created of this CreateTransactionPortfolioRequest.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def base_currency(self):
        """Gets the base_currency of this CreateTransactionPortfolioRequest.  # noqa: E501

        The base currency of the transaction portfolio.  # noqa: E501

        :return: The base_currency of this CreateTransactionPortfolioRequest.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this CreateTransactionPortfolioRequest.

        The base currency of the transaction portfolio.  # noqa: E501

        :param base_currency: The base_currency of this CreateTransactionPortfolioRequest.  # noqa: E501
        :type: str
        """
        if base_currency is None:
            raise ValueError("Invalid value for `base_currency`, must not be `None`")  # noqa: E501

        self._base_currency = base_currency

    @property
    def corporate_action_source_id(self):
        """Gets the corporate_action_source_id of this CreateTransactionPortfolioRequest.  # noqa: E501


        :return: The corporate_action_source_id of this CreateTransactionPortfolioRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._corporate_action_source_id

    @corporate_action_source_id.setter
    def corporate_action_source_id(self, corporate_action_source_id):
        """Sets the corporate_action_source_id of this CreateTransactionPortfolioRequest.


        :param corporate_action_source_id: The corporate_action_source_id of this CreateTransactionPortfolioRequest.  # noqa: E501
        :type: ResourceId
        """

        self._corporate_action_source_id = corporate_action_source_id

    @property
    def accounting_method(self):
        """Gets the accounting_method of this CreateTransactionPortfolioRequest.  # noqa: E501

        Determines the accounting treatment given to the transaction portfolio's tax lots. The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst  # noqa: E501

        :return: The accounting_method of this CreateTransactionPortfolioRequest.  # noqa: E501
        :rtype: str
        """
        return self._accounting_method

    @accounting_method.setter
    def accounting_method(self, accounting_method):
        """Sets the accounting_method of this CreateTransactionPortfolioRequest.

        Determines the accounting treatment given to the transaction portfolio's tax lots. The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst  # noqa: E501

        :param accounting_method: The accounting_method of this CreateTransactionPortfolioRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Default", "AverageCost", "FirstInFirstOut", "LastInFirstOut", "HighestCostFirst", "LowestCostFirst"]  # noqa: E501
        if accounting_method not in allowed_values:
            raise ValueError(
                "Invalid value for `accounting_method` ({0}), must be one of {1}"  # noqa: E501
                .format(accounting_method, allowed_values)
            )

        self._accounting_method = accounting_method

    @property
    def sub_holding_keys(self):
        """Gets the sub_holding_keys of this CreateTransactionPortfolioRequest.  # noqa: E501

        A set of unique transaction properties to group the transaction portfolio's holdings by. Each property must be from the 'Transaction' domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. 'Transaction/strategies/quantsignal'.  # noqa: E501

        :return: The sub_holding_keys of this CreateTransactionPortfolioRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._sub_holding_keys

    @sub_holding_keys.setter
    def sub_holding_keys(self, sub_holding_keys):
        """Sets the sub_holding_keys of this CreateTransactionPortfolioRequest.

        A set of unique transaction properties to group the transaction portfolio's holdings by. Each property must be from the 'Transaction' domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. 'Transaction/strategies/quantsignal'.  # noqa: E501

        :param sub_holding_keys: The sub_holding_keys of this CreateTransactionPortfolioRequest.  # noqa: E501
        :type: list[str]
        """

        self._sub_holding_keys = sub_holding_keys

    @property
    def properties(self):
        """Gets the properties of this CreateTransactionPortfolioRequest.  # noqa: E501

        A set of unique portfolio properties to add to the transaction portfolio. Each property must be from the 'Portfolio' domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'. These properties must be pre-defined.  # noqa: E501

        :return: The properties of this CreateTransactionPortfolioRequest.  # noqa: E501
        :rtype: dict(str, ModelProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CreateTransactionPortfolioRequest.

        A set of unique portfolio properties to add to the transaction portfolio. Each property must be from the 'Portfolio' domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'. These properties must be pre-defined.  # noqa: E501

        :param properties: The properties of this CreateTransactionPortfolioRequest.  # noqa: E501
        :type: dict(str, ModelProperty)
        """

        self._properties = properties

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
        if not isinstance(other, CreateTransactionPortfolioRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
