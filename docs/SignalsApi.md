# fideo_api.SignalsApi

All URIs are relative to *https://api.fullcontact.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_signals_post**](SignalsApi.md#verify_signals_post) | **POST** /verify.signals | 


# **verify_signals_post**
> VerifySignalsPost200Response verify_signals_post(v=v, multi_field_req=multi_field_req)



### Example

* Bearer Authentication (bearerAuth):

```python
import fideo_api
from fideo_api.models.multi_field_req import MultiFieldReq
from fideo_api.models.verify_signals_post200_response import VerifySignalsPost200Response
from fideo_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fullcontact.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = fideo_api.Configuration(
    host = "https://api.fullcontact.com/v3"
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
    multi_field_req = fideo_api.MultiFieldReq() # MultiFieldReq |  (optional)

    try:
        api_response = api_instance.verify_signals_post(v=v, multi_field_req=multi_field_req)
        print("The response of SignalsApi->verify_signals_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignalsApi->verify_signals_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v** | **str**|  | [optional] 
 **multi_field_req** | [**MultiFieldReq**](MultiFieldReq.md)|  | [optional] 

### Return type

[**VerifySignalsPost200Response**](VerifySignalsPost200Response.md)

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

