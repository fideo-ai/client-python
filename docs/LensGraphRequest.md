# LensGraphRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Lens graph response mode. | 
**query** | **str** | Comma-separated Lens graph seed query. | 
**hops** | **int** | Requested graph hop count. Defaults to 2 when omitted. | [optional] [default to 2]

## Example

```python
from fideo_api.models.lens_graph_request import LensGraphRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LensGraphRequest from a JSON string
lens_graph_request_instance = LensGraphRequest.from_json(json)
# print the JSON string representation of the object
print(LensGraphRequest.to_json())

# convert the object into a dict
lens_graph_request_dict = lens_graph_request_instance.to_dict()
# create an instance of LensGraphRequest from a dict
lens_graph_request_from_dict = LensGraphRequest.from_dict(lens_graph_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


