# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3084
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class Transaction(object):
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
        'transaction_id': 'str',
        'type': 'str',
        'instrument_identifiers': 'dict(str, str)',
        'instrument_uid': 'str',
        'transaction_date': 'datetime',
        'settlement_date': 'datetime',
        'units': 'float',
        'transaction_price': 'TransactionPrice',
        'total_consideration': 'CurrencyAndAmount',
        'exchange_rate': 'float',
        'transaction_currency': 'str',
        'properties': 'dict(str, PerpetualProperty)',
        'counterparty_id': 'str',
        'source': 'str',
        'entry_date_time': 'datetime'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'type': 'type',
        'instrument_identifiers': 'instrumentIdentifiers',
        'instrument_uid': 'instrumentUid',
        'transaction_date': 'transactionDate',
        'settlement_date': 'settlementDate',
        'units': 'units',
        'transaction_price': 'transactionPrice',
        'total_consideration': 'totalConsideration',
        'exchange_rate': 'exchangeRate',
        'transaction_currency': 'transactionCurrency',
        'properties': 'properties',
        'counterparty_id': 'counterpartyId',
        'source': 'source',
        'entry_date_time': 'entryDateTime'
    }

    required_map = {
        'transaction_id': 'required',
        'type': 'required',
        'instrument_identifiers': 'optional',
        'instrument_uid': 'required',
        'transaction_date': 'required',
        'settlement_date': 'required',
        'units': 'required',
        'transaction_price': 'optional',
        'total_consideration': 'required',
        'exchange_rate': 'optional',
        'transaction_currency': 'optional',
        'properties': 'optional',
        'counterparty_id': 'optional',
        'source': 'optional',
        'entry_date_time': 'optional'
    }

    def __init__(self, transaction_id=None, type=None, instrument_identifiers=None, instrument_uid=None, transaction_date=None, settlement_date=None, units=None, transaction_price=None, total_consideration=None, exchange_rate=None, transaction_currency=None, properties=None, counterparty_id=None, source=None, entry_date_time=None):  # noqa: E501
        """
        Transaction - a model defined in OpenAPI

        :param transaction_id:  The unique identifier for the transaction. (required)
        :type transaction_id: str
        :param type:  The type of the transaction e.g. 'Buy', 'Sell'. The transaction type should have been pre-configured via the System Configuration API endpoint. (required)
        :type type: str
        :param instrument_identifiers:  A set of instrument identifiers that can resolve the transaction to a unique instrument.
        :type instrument_identifiers: dict(str, str)
        :param instrument_uid:  The unqiue Lusid Instrument Id (LUID) of the instrument that the transaction is in. (required)
        :type instrument_uid: str
        :param transaction_date:  The date of the transaction. (required)
        :type transaction_date: datetime
        :param settlement_date:  The settlement date of the transaction. (required)
        :type settlement_date: datetime
        :param units:  The number of units transacted in the associated instrument. (required)
        :type units: float
        :param transaction_price: 
        :type transaction_price: lusid.TransactionPrice
        :param total_consideration:  (required)
        :type total_consideration: lusid.CurrencyAndAmount
        :param exchange_rate:  The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate.
        :type exchange_rate: float
        :param transaction_currency:  The transaction currency.
        :type transaction_currency: str
        :param properties:  Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the 'Transaction' domain.
        :type properties: dict[str, lusid.PerpetualProperty]
        :param counterparty_id:  The identifier for the counterparty of the transaction.
        :type counterparty_id: str
        :param source:  The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration.
        :type source: str
        :param entry_date_time:  The asAt datetime that the transaction was added to LUSID.
        :type entry_date_time: datetime

        """  # noqa: E501

        self._transaction_id = None
        self._type = None
        self._instrument_identifiers = None
        self._instrument_uid = None
        self._transaction_date = None
        self._settlement_date = None
        self._units = None
        self._transaction_price = None
        self._total_consideration = None
        self._exchange_rate = None
        self._transaction_currency = None
        self._properties = None
        self._counterparty_id = None
        self._source = None
        self._entry_date_time = None
        self.discriminator = None

        self.transaction_id = transaction_id
        self.type = type
        self.instrument_identifiers = instrument_identifiers
        self.instrument_uid = instrument_uid
        self.transaction_date = transaction_date
        self.settlement_date = settlement_date
        self.units = units
        if transaction_price is not None:
            self.transaction_price = transaction_price
        self.total_consideration = total_consideration
        self.exchange_rate = exchange_rate
        self.transaction_currency = transaction_currency
        self.properties = properties
        self.counterparty_id = counterparty_id
        self.source = source
        if entry_date_time is not None:
            self.entry_date_time = entry_date_time

    @property
    def transaction_id(self):
        """Gets the transaction_id of this Transaction.  # noqa: E501

        The unique identifier for the transaction.  # noqa: E501

        :return: The transaction_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this Transaction.

        The unique identifier for the transaction.  # noqa: E501

        :param transaction_id: The transaction_id of this Transaction.  # noqa: E501
        :type: str
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def type(self):
        """Gets the type of this Transaction.  # noqa: E501

        The type of the transaction e.g. 'Buy', 'Sell'. The transaction type should have been pre-configured via the System Configuration API endpoint.  # noqa: E501

        :return: The type of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Transaction.

        The type of the transaction e.g. 'Buy', 'Sell'. The transaction type should have been pre-configured via the System Configuration API endpoint.  # noqa: E501

        :param type: The type of this Transaction.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this Transaction.  # noqa: E501

        A set of instrument identifiers that can resolve the transaction to a unique instrument.  # noqa: E501

        :return: The instrument_identifiers of this Transaction.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this Transaction.

        A set of instrument identifiers that can resolve the transaction to a unique instrument.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this Transaction.  # noqa: E501
        :type: dict(str, str)
        """

        self._instrument_identifiers = instrument_identifiers

    @property
    def instrument_uid(self):
        """Gets the instrument_uid of this Transaction.  # noqa: E501

        The unqiue Lusid Instrument Id (LUID) of the instrument that the transaction is in.  # noqa: E501

        :return: The instrument_uid of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._instrument_uid

    @instrument_uid.setter
    def instrument_uid(self, instrument_uid):
        """Sets the instrument_uid of this Transaction.

        The unqiue Lusid Instrument Id (LUID) of the instrument that the transaction is in.  # noqa: E501

        :param instrument_uid: The instrument_uid of this Transaction.  # noqa: E501
        :type: str
        """
        if instrument_uid is None:
            raise ValueError("Invalid value for `instrument_uid`, must not be `None`")  # noqa: E501

        self._instrument_uid = instrument_uid

    @property
    def transaction_date(self):
        """Gets the transaction_date of this Transaction.  # noqa: E501

        The date of the transaction.  # noqa: E501

        :return: The transaction_date of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this Transaction.

        The date of the transaction.  # noqa: E501

        :param transaction_date: The transaction_date of this Transaction.  # noqa: E501
        :type: datetime
        """
        if transaction_date is None:
            raise ValueError("Invalid value for `transaction_date`, must not be `None`")  # noqa: E501

        self._transaction_date = transaction_date

    @property
    def settlement_date(self):
        """Gets the settlement_date of this Transaction.  # noqa: E501

        The settlement date of the transaction.  # noqa: E501

        :return: The settlement_date of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this Transaction.

        The settlement date of the transaction.  # noqa: E501

        :param settlement_date: The settlement_date of this Transaction.  # noqa: E501
        :type: datetime
        """
        if settlement_date is None:
            raise ValueError("Invalid value for `settlement_date`, must not be `None`")  # noqa: E501

        self._settlement_date = settlement_date

    @property
    def units(self):
        """Gets the units of this Transaction.  # noqa: E501

        The number of units transacted in the associated instrument.  # noqa: E501

        :return: The units of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this Transaction.

        The number of units transacted in the associated instrument.  # noqa: E501

        :param units: The units of this Transaction.  # noqa: E501
        :type: float
        """
        if units is None:
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501

        self._units = units

    @property
    def transaction_price(self):
        """Gets the transaction_price of this Transaction.  # noqa: E501


        :return: The transaction_price of this Transaction.  # noqa: E501
        :rtype: TransactionPrice
        """
        return self._transaction_price

    @transaction_price.setter
    def transaction_price(self, transaction_price):
        """Sets the transaction_price of this Transaction.


        :param transaction_price: The transaction_price of this Transaction.  # noqa: E501
        :type: TransactionPrice
        """

        self._transaction_price = transaction_price

    @property
    def total_consideration(self):
        """Gets the total_consideration of this Transaction.  # noqa: E501


        :return: The total_consideration of this Transaction.  # noqa: E501
        :rtype: CurrencyAndAmount
        """
        return self._total_consideration

    @total_consideration.setter
    def total_consideration(self, total_consideration):
        """Sets the total_consideration of this Transaction.


        :param total_consideration: The total_consideration of this Transaction.  # noqa: E501
        :type: CurrencyAndAmount
        """
        if total_consideration is None:
            raise ValueError("Invalid value for `total_consideration`, must not be `None`")  # noqa: E501

        self._total_consideration = total_consideration

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this Transaction.  # noqa: E501

        The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate.  # noqa: E501

        :return: The exchange_rate of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this Transaction.

        The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate.  # noqa: E501

        :param exchange_rate: The exchange_rate of this Transaction.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def transaction_currency(self):
        """Gets the transaction_currency of this Transaction.  # noqa: E501

        The transaction currency.  # noqa: E501

        :return: The transaction_currency of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_currency

    @transaction_currency.setter
    def transaction_currency(self, transaction_currency):
        """Sets the transaction_currency of this Transaction.

        The transaction currency.  # noqa: E501

        :param transaction_currency: The transaction_currency of this Transaction.  # noqa: E501
        :type: str
        """

        self._transaction_currency = transaction_currency

    @property
    def properties(self):
        """Gets the properties of this Transaction.  # noqa: E501

        Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the 'Transaction' domain.  # noqa: E501

        :return: The properties of this Transaction.  # noqa: E501
        :rtype: dict(str, PerpetualProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Transaction.

        Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the 'Transaction' domain.  # noqa: E501

        :param properties: The properties of this Transaction.  # noqa: E501
        :type: dict(str, PerpetualProperty)
        """

        self._properties = properties

    @property
    def counterparty_id(self):
        """Gets the counterparty_id of this Transaction.  # noqa: E501

        The identifier for the counterparty of the transaction.  # noqa: E501

        :return: The counterparty_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._counterparty_id

    @counterparty_id.setter
    def counterparty_id(self, counterparty_id):
        """Sets the counterparty_id of this Transaction.

        The identifier for the counterparty of the transaction.  # noqa: E501

        :param counterparty_id: The counterparty_id of this Transaction.  # noqa: E501
        :type: str
        """

        self._counterparty_id = counterparty_id

    @property
    def source(self):
        """Gets the source of this Transaction.  # noqa: E501

        The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration.  # noqa: E501

        :return: The source of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Transaction.

        The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration.  # noqa: E501

        :param source: The source of this Transaction.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def entry_date_time(self):
        """Gets the entry_date_time of this Transaction.  # noqa: E501

        The asAt datetime that the transaction was added to LUSID.  # noqa: E501

        :return: The entry_date_time of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._entry_date_time

    @entry_date_time.setter
    def entry_date_time(self, entry_date_time):
        """Sets the entry_date_time of this Transaction.

        The asAt datetime that the transaction was added to LUSID.  # noqa: E501

        :param entry_date_time: The entry_date_time of this Transaction.  # noqa: E501
        :type: datetime
        """

        self._entry_date_time = entry_date_time

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
        if not isinstance(other, Transaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
