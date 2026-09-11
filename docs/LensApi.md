# fideo_api.LensApi

All URIs are relative to *https://api.fideo.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lens_graph**](LensApi.md#lens_graph) | **POST** /v3/lens.graph | Query the Lens graph


# **lens_graph**
> LensGraphResponse lens_graph(lens_graph_request=lens_graph_request)

Query the Lens graph

Query raw or expanded Lens graph edges. Product and datapack entitlements are derived from the account contract, not from the request body.

### Example

* Bearer Authentication (bearerAuth):

```python
import fideo_api
from fideo_api.models.lens_graph_request import LensGraphRequest
from fideo_api.models.lens_graph_response import LensGraphResponse
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
    api_instance = fideo_api.LensApi(api_client)
    lens_graph_request = fideo_api.LensGraphRequest() # LensGraphRequest |  (optional)

    try:
        # Query the Lens graph
        api_response = await api_instance.lens_graph(lens_graph_request=lens_graph_request)
        print("The response of LensApi->lens_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LensApi->lens_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lens_graph_request** | [**LensGraphRequest**](LensGraphRequest.md)|  | [optional] 

### Return type

[**LensGraphResponse**](LensGraphResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * X-Fideo-Lens-Limit - Contract usage limit for Lens. A value of 0 means unlimited. <br>  * X-Fideo-Lens-Usage - Lens usage after the successful request. <br>  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**429** | Lens usage limit reached |  * X-Fideo-Lens-Limit - Contract usage limit for Lens. <br>  * X-Fideo-Lens-Usage - Lens usage after the successful request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

