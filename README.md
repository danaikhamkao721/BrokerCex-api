# swagger-client
the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec. There are no TOS at this moment, use at your own risk we take no responsibility

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://broker.cex.io](https://broker.cex.io)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['broAuth'] = 'apiKey, apiSignature'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['broAuth'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MarketApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # getMarketInfo
    api_response = api_instance.get_market_info(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_market_info: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://broker.cex.io/api/public/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*MarketApi* | [**get_market_info**](docs/MarketApi.md#get_market_info) | **GET** /info | getMarketInfo
*MarketApi* | [**get_order_book**](docs/MarketApi.md#get_order_book) | **GET** /orderbook | getOrderBook
*OperationsApi* | [**cancel_order**](docs/OperationsApi.md#cancel_order) | **POST** /operations/cancel-order | cancelOrder
*OperationsApi* | [**cancel_order_group**](docs/OperationsApi.md#cancel_order_group) | **POST** /operations/cancel-order-group | cancelOrderGroup
*OperationsApi* | [**edit_account_order**](docs/OperationsApi.md#edit_account_order) | **POST** /operations/edit-account-order | editOrder
*OperationsApi* | [**get_account_metrics**](docs/OperationsApi.md#get_account_metrics) | **POST** /operations/account-metrics | getAccountMetrics
*OperationsApi* | [**get_market_data**](docs/OperationsApi.md#get_market_data) | **POST** /marketdata | getMarketData
*OperationsApi* | [**get_open_order_list**](docs/OperationsApi.md#get_open_order_list) | **POST** /operations/open-orders-list | getOpenOrderList
*OperationsApi* | [**get_order_history_list**](docs/OperationsApi.md#get_order_history_list) | **POST** /operations/order-history | getOrderHistoryList
*OperationsApi* | [**get_user_info**](docs/OperationsApi.md#get_user_info) | **POST** /operations/user-info | getUserInfo
*OperationsApi* | [**open_account_order**](docs/OperationsApi.md#open_account_order) | **POST** /operations/place-account-order | placeOrder
*OperationsApi* | [**open_account_order_group**](docs/OperationsApi.md#open_account_order_group) | **POST** /operations/place-account-order-group | placeOrderGroup


## Documentation For Models

 - [AccountMetrics](docs/AccountMetrics.md)
 - [AccountMetricsHandlerResponse](docs/AccountMetricsHandlerResponse.md)
 - [AccountMetricsResponse](docs/AccountMetricsResponse.md)
 - [Body](docs/Body.md)
 - [Body1](docs/Body1.md)
 - [Body2](docs/Body2.md)
 - [Body3](docs/Body3.md)
 - [Body4](docs/Body4.md)
 - [Body5](docs/Body5.md)
 - [Body6](docs/Body6.md)
 - [Body7](docs/Body7.md)
 - [CancelOrderGroupHandlerResponse](docs/CancelOrderGroupHandlerResponse.md)
 - [CancelOrderGroupResponse](docs/CancelOrderGroupResponse.md)
 - [CancelOrderGroupResponseOrderResponses](docs/CancelOrderGroupResponseOrderResponses.md)
 - [CancelOrderHandlerResponse](docs/CancelOrderHandlerResponse.md)
 - [CancelOrderResponse](docs/CancelOrderResponse.md)
 - [EditAccountOrderHandlerResponse](docs/EditAccountOrderHandlerResponse.md)
 - [EditOrderResponse](docs/EditOrderResponse.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [MarketDataEvent](docs/MarketDataEvent.md)
 - [MarketDataHandlerResponse](docs/MarketDataHandlerResponse.md)
 - [MarketDataList](docs/MarketDataList.md)
 - [MarketDataType](docs/MarketDataType.md)
 - [MarketPairInfo](docs/MarketPairInfo.md)
 - [MarketdataEventTypes](docs/MarketdataEventTypes.md)
 - [OpenAccountOrderHandlerRequest](docs/OpenAccountOrderHandlerRequest.md)
 - [OpenAccountOrderHandlerResponse](docs/OpenAccountOrderHandlerResponse.md)
 - [OpenOrderGroupHandlerResponse](docs/OpenOrderGroupHandlerResponse.md)
 - [OpenOrderList](docs/OpenOrderList.md)
 - [OpenOrderListHandlerResponse](docs/OpenOrderListHandlerResponse.md)
 - [OpenOrderRequest](docs/OpenOrderRequest.md)
 - [OpenOrderResponse](docs/OpenOrderResponse.md)
 - [Order](docs/Order.md)
 - [OrderCashTransactions](docs/OrderCashTransactions.md)
 - [OrderExecution](docs/OrderExecution.md)
 - [OrderHistoryListHandlerResponse](docs/OrderHistoryListHandlerResponse.md)
 - [OrderHistoryListResponse](docs/OrderHistoryListResponse.md)
 - [OrderLeg](docs/OrderLeg.md)
 - [OrderLinks](docs/OrderLinks.md)
 - [UserAccount](docs/UserAccount.md)
 - [UserInfoDetails](docs/UserInfoDetails.md)
 - [UserInfoHandlerResponse](docs/UserInfoHandlerResponse.md)
 - [UserInfoResponse](docs/UserInfoResponse.md)
 - [UserPosition](docs/UserPosition.md)


## Documentation For Authorization


## apiKey

- **Type**: API key
- **API key parameter name**: broAuth
- **Location**: HTTP header


## Author

support@cexbro.com

