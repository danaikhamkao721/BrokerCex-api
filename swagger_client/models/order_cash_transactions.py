# coding: utf-8

"""
    Broker API.

    the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec. There are no TOS at this moment, use at your own risk we take no responsibility  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: support@cexbro.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OrderCashTransactions(object):
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
        'account': 'str',
        'client_order_id': 'str',
        'currency': 'str',
        'order_code': 'str',
        'trade_code': 'str',
        'transaction_code': 'str',
        'transaction_time': 'datetime',
        'type': 'str',
        'value': 'float',
        'version': 'int'
    }

    attribute_map = {
        'account': 'account',
        'client_order_id': 'clientOrderId',
        'currency': 'currency',
        'order_code': 'orderCode',
        'trade_code': 'tradeCode',
        'transaction_code': 'transactionCode',
        'transaction_time': 'transactionTime',
        'type': 'type',
        'value': 'value',
        'version': 'version'
    }

    def __init__(self, account=None, client_order_id=None, currency=None, order_code=None, trade_code=None, transaction_code=None, transaction_time=None, type=None, value=None, version=None):  # noqa: E501
        """OrderCashTransactions - a model defined in Swagger"""  # noqa: E501

        self._account = None
        self._client_order_id = None
        self._currency = None
        self._order_code = None
        self._trade_code = None
        self._transaction_code = None
        self._transaction_time = None
        self._type = None
        self._value = None
        self._version = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if client_order_id is not None:
            self.client_order_id = client_order_id
        if currency is not None:
            self.currency = currency
        if order_code is not None:
            self.order_code = order_code
        if trade_code is not None:
            self.trade_code = trade_code
        if transaction_code is not None:
            self.transaction_code = transaction_code
        if transaction_time is not None:
            self.transaction_time = transaction_time
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if version is not None:
            self.version = version

    @property
    def account(self):
        """Gets the account of this OrderCashTransactions.  # noqa: E501


        :return: The account of this OrderCashTransactions.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this OrderCashTransactions.


        :param account: The account of this OrderCashTransactions.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def client_order_id(self):
        """Gets the client_order_id of this OrderCashTransactions.  # noqa: E501


        :return: The client_order_id of this OrderCashTransactions.  # noqa: E501
        :rtype: str
        """
        return self._client_order_id

    @client_order_id.setter
    def client_order_id(self, client_order_id):
        """Sets the client_order_id of this OrderCashTransactions.


        :param client_order_id: The client_order_id of this OrderCashTransactions.  # noqa: E501
        :type: str
        """

        self._client_order_id = client_order_id

    @property
    def currency(self):
        """Gets the currency of this OrderCashTransactions.  # noqa: E501


        :return: The currency of this OrderCashTransactions.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this OrderCashTransactions.


        :param currency: The currency of this OrderCashTransactions.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def order_code(self):
        """Gets the order_code of this OrderCashTransactions.  # noqa: E501


        :return: The order_code of this OrderCashTransactions.  # noqa: E501
        :rtype: str
        """
        return self._order_code

    @order_code.setter
    def order_code(self, order_code):
        """Sets the order_code of this OrderCashTransactions.


        :param order_code: The order_code of this OrderCashTransactions.  # noqa: E501
        :type: str
        """

        self._order_code = order_code

    @property
    def trade_code(self):
        """Gets the trade_code of this OrderCashTransactions.  # noqa: E501


        :return: The trade_code of this OrderCashTransactions.  # noqa: E501
        :rtype: str
        """
        return self._trade_code

    @trade_code.setter
    def trade_code(self, trade_code):
        """Sets the trade_code of this OrderCashTransactions.


        :param trade_code: The trade_code of this OrderCashTransactions.  # noqa: E501
        :type: str
        """

        self._trade_code = trade_code

    @property
    def transaction_code(self):
        """Gets the transaction_code of this OrderCashTransactions.  # noqa: E501


        :return: The transaction_code of this OrderCashTransactions.  # noqa: E501
        :rtype: str
        """
        return self._transaction_code

    @transaction_code.setter
    def transaction_code(self, transaction_code):
        """Sets the transaction_code of this OrderCashTransactions.


        :param transaction_code: The transaction_code of this OrderCashTransactions.  # noqa: E501
        :type: str
        """

        self._transaction_code = transaction_code

    @property
    def transaction_time(self):
        """Gets the transaction_time of this OrderCashTransactions.  # noqa: E501


        :return: The transaction_time of this OrderCashTransactions.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """Sets the transaction_time of this OrderCashTransactions.


        :param transaction_time: The transaction_time of this OrderCashTransactions.  # noqa: E501
        :type: datetime
        """

        self._transaction_time = transaction_time

    @property
    def type(self):
        """Gets the type of this OrderCashTransactions.  # noqa: E501


        :return: The type of this OrderCashTransactions.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OrderCashTransactions.


        :param type: The type of this OrderCashTransactions.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this OrderCashTransactions.  # noqa: E501


        :return: The value of this OrderCashTransactions.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OrderCashTransactions.


        :param value: The value of this OrderCashTransactions.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def version(self):
        """Gets the version of this OrderCashTransactions.  # noqa: E501


        :return: The version of this OrderCashTransactions.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OrderCashTransactions.


        :param version: The version of this OrderCashTransactions.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(OrderCashTransactions, dict):
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
        if not isinstance(other, OrderCashTransactions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
