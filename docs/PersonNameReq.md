# PersonNameReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**given** | **str** |  | [optional] 
**family** | **str** |  | [optional] 
**middle** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**full** | **str** |  | [optional] 

## Example

```python
from fideo_api.models.person_name_req import PersonNameReq

# TODO update the JSON string below
json = "{}"
# create an instance of PersonNameReq from a JSON string
person_name_req_instance = PersonNameReq.from_json(json)
# print the JSON string representation of the object
print(PersonNameReq.to_json())

# convert the object into a dict
person_name_req_dict = person_name_req_instance.to_dict()
# create an instance of PersonNameReq from a dict
person_name_req_from_dict = PersonNameReq.from_dict(person_name_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


