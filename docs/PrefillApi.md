# fideo_api.PrefillApi

All URIs are relative to *https://api.fideo.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prefill**](PrefillApi.md#prefill) | **POST** /prefill | Resolve or evaluate onboarding identity fields


# **prefill**
> PrefillResponse prefill(multi_field_req_with_options)

Resolve or evaluate onboarding identity fields

The customer is responsible for proving phone possession before the initial request.
Omit sessionId to resolve identity fields from a phone. Send the returned sessionId with
reviewed or edited identity fields to receive a Verify evaluation. Recent session IDs are
reused; valid session IDs older than 10 minutes start a new session.

### Example

* Bearer Authentication (bearerAuth):

```python
import fideo_api
from fideo_api.models.multi_field_req_with_options import MultiFieldReqWithOptions
from fideo_api.models.prefill_response import PrefillResponse
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
async with fideo_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fideo_api.PrefillApi(api_client)
    multi_field_req_with_options = fideo_api.MultiFieldReqWithOptions() # MultiFieldReqWithOptions | 

    try:
        # Resolve or evaluate onboarding identity fields
        api_response = await api_instance.prefill(multi_field_req_with_options)
        print("The response of PrefillApi->prefill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrefillApi->prefill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_field_req_with_options** | [**MultiFieldReqWithOptions**](MultiFieldReqWithOptions.md)|  | 

### Return type

[**PrefillResponse**](PrefillResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prefill match, no-match, or reviewed identity evaluation |  * X-Fideo-Limit -  <br>  * X-Fideo-Usage -  <br>  |
**400** | Invalid request or malformed Prefill session ID |  -  |
**403** | Prefill product unavailable |  -  |
**410** | Claimed or deleted data |  -  |
**429** | Prefill trial request limit reached |  * X-Fideo-Limit -  <br>  * X-Fideo-Usage -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

