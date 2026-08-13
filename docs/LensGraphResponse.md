# LensGraphResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | **List[object]** |  | [optional] 
**seed_graph_ids** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from fideo_api.models.lens_graph_response import LensGraphResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LensGraphResponse from a JSON string
lens_graph_response_instance = LensGraphResponse.from_json(json)
# print the JSON string representation of the object
print(LensGraphResponse.to_json())

# convert the object into a dict
lens_graph_response_dict = lens_graph_response_instance.to_dict()
# create an instance of LensGraphResponse from a dict
lens_graph_response_from_dict = LensGraphResponse.from_dict(lens_graph_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


