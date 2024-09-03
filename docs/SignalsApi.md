# fideo_api.SignalsApi

All URIs are relative to *https://api.fideo.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**signals_post**](SignalsApi.md#signals_post) | **POST** /signals | 
[**v3_verify_signals_post**](SignalsApi.md#v3_verify_signals_post) | **POST** /v3/verify.signals | 


# **signals_post**
> V3VerifySignalsPost200Response signals_post(v=v, multi_field_req_with_options=multi_field_req_with_options)



### Example

* Bearer Authentication (bearerAuth):

```python
import fideo_api
from fideo_api.models.multi_field_req_with_options import MultiFieldReqWithOptions
from fideo_api.models.v3_verify_signals_post200_response import V3VerifySignalsPost200Response
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
    api_instance = fideo_api.SignalsApi(api_client)
    v = 'v_example' # str |  (optional)
    multi_field_req_with_options = fideo_api.MultiFieldReqWithOptions() # MultiFieldReqWithOptions |  (optional)

    try:
        api_response = api_instance.signals_post(v=v, multi_field_req_with_options=multi_field_req_with_options)
        print("The response of SignalsApi->signals_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignalsApi->signals_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v** | **str**|  | [optional] 
 **multi_field_req_with_options** | [**MultiFieldReqWithOptions**](MultiFieldReqWithOptions.md)|  | [optional] 

### Return type

[**V3VerifySignalsPost200Response**](V3VerifySignalsPost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_verify_signals_post**
> V3VerifySignalsPost200Response v3_verify_signals_post(v=v, multi_field_req_with_options=multi_field_req_with_options)



### Example

* Bearer Authentication (bearerAuth):

```python
import fideo_api
from fideo_api.models.multi_field_req_with_options import MultiFieldReqWithOptions
from fideo_api.models.v3_verify_signals_post200_response import V3VerifySignalsPost200Response
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
    api_instance = fideo_api.SignalsApi(api_client)
    v = 'v_example' # str |  (optional)
    multi_field_req_with_options = fideo_api.MultiFieldReqWithOptions() # MultiFieldReqWithOptions |  (optional)

    try:
        api_response = api_instance.v3_verify_signals_post(v=v, multi_field_req_with_options=multi_field_req_with_options)
        print("The response of SignalsApi->v3_verify_signals_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignalsApi->v3_verify_signals_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v** | **str**|  | [optional] 
 **multi_field_req_with_options** | [**MultiFieldReqWithOptions**](MultiFieldReqWithOptions.md)|  | [optional] 

### Return type

[**V3VerifySignalsPost200Response**](V3VerifySignalsPost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

