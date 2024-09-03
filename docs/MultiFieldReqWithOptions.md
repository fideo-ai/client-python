# MultiFieldReqWithOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infer** | **bool** |  | [optional] 
**confidence** | **str** |  | [optional] [default to 'LOW']
**birthday** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**countries** | **List[str]** |  | [optional] 
**excluded_countries** | **List[str]** |  | [optional] 

## Example

```python
from fideo_api.models.multi_field_req_with_options import MultiFieldReqWithOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MultiFieldReqWithOptions from a JSON string
multi_field_req_with_options_instance = MultiFieldReqWithOptions.from_json(json)
# print the JSON string representation of the object
print(MultiFieldReqWithOptions.to_json())

# convert the object into a dict
multi_field_req_with_options_dict = multi_field_req_with_options_instance.to_dict()
# create an instance of MultiFieldReqWithOptions from a dict
multi_field_req_with_options_from_dict = MultiFieldReqWithOptions.from_dict(multi_field_req_with_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


