# Employment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **bool** |  | [optional] 
**company** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**start** | [**EmploymentDate**](EmploymentDate.md) |  | [optional] 
**end** | [**EmploymentDate**](EmploymentDate.md) |  | [optional] 

## Example

```python
from fideo_api.models.employment import Employment

# TODO update the JSON string below
json = "{}"
# create an instance of Employment from a JSON string
employment_instance = Employment.from_json(json)
# print the JSON string representation of the object
print(Employment.to_json())

# convert the object into a dict
employment_dict = employment_instance.to_dict()
# create an instance of Employment from a dict
employment_from_dict = Employment.from_dict(employment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


