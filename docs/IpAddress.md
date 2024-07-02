# IpAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_seen_ms** | **int** |  | [optional] 
**last_seen_ms** | **int** |  | [optional] 
**observations** | **int** |  | [optional] 
**confidence** | **float** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from fideo_api.models.ip_address import IpAddress

# TODO update the JSON string below
json = "{}"
# create an instance of IpAddress from a JSON string
ip_address_instance = IpAddress.from_json(json)
# print the JSON string representation of the object
print(IpAddress.to_json())

# convert the object into a dict
ip_address_dict = ip_address_instance.to_dict()
# create an instance of IpAddress from a dict
ip_address_from_dict = IpAddress.from_dict(ip_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


