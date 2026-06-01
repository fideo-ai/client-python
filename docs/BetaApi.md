# fideo_api.BetaApi

All URIs are relative to *https://api.fideo.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**beta_signals_patterns_summary_post**](BetaApi.md#beta_signals_patterns_summary_post) | **POST** /beta/signals/patterns/summary | Get signal patterns summary
[**beta_signals_patterns_timeseries_post**](BetaApi.md#beta_signals_patterns_timeseries_post) | **POST** /beta/signals/patterns/timeseries | Get signal patterns timeseries


# **beta_signals_patterns_summary_post**
> SignalPatternRecencyResponse beta_signals_patterns_summary_post(signal_patterns_request=signal_patterns_request)

Get signal patterns summary

Returns summaries of ALL intervals (hour through year) for an email in the request

### Example

* Bearer Authentication (bearerAuth):

```python
import fideo_api
from fideo_api.models.signal_pattern_recency_response import SignalPatternRecencyResponse
from fideo_api.models.signal_patterns_request import SignalPatternsRequest
from fideo_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fideo.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = fideo_api.Configuration(
    host = "https://api.fideo.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = fideo_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fideo_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fideo_api.BetaApi(api_client)
    signal_patterns_request = fideo_api.SignalPatternsRequest() # SignalPatternsRequest |  (optional)

    try:
        # Get signal patterns summary
        api_response = api_instance.beta_signals_patterns_summary_post(signal_patterns_request=signal_patterns_request)
        print("The response of BetaApi->beta_signals_patterns_summary_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaApi->beta_signals_patterns_summary_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signal_patterns_request** | [**SignalPatternsRequest**](SignalPatternsRequest.md)|  | [optional] 

### Return type

[**SignalPatternRecencyResponse**](SignalPatternRecencyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **beta_signals_patterns_timeseries_post**
> Dict[str, SignalPatternResponseUnit] beta_signals_patterns_timeseries_post(signal_patterns_request=signal_patterns_request)

Get signal patterns timeseries

Returns timeseries details for signal patterns

### Example

* Bearer Authentication (bearerAuth):

```python
import fideo_api
from fideo_api.models.signal_pattern_response_unit import SignalPatternResponseUnit
from fideo_api.models.signal_patterns_request import SignalPatternsRequest
from fideo_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fideo.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = fideo_api.Configuration(
    host = "https://api.fideo.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = fideo_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fideo_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fideo_api.BetaApi(api_client)
    signal_patterns_request = fideo_api.SignalPatternsRequest() # SignalPatternsRequest |  (optional)

    try:
        # Get signal patterns timeseries
        api_response = api_instance.beta_signals_patterns_timeseries_post(signal_patterns_request=signal_patterns_request)
        print("The response of BetaApi->beta_signals_patterns_timeseries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaApi->beta_signals_patterns_timeseries_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signal_patterns_request** | [**SignalPatternsRequest**](SignalPatternsRequest.md)|  | [optional] 

### Return type

[**Dict[str, SignalPatternResponseUnit]**](SignalPatternResponseUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

