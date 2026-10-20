# Demographics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** |  | [optional] 
**age_range** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**location_general** | **str** |  | [optional] 

## Example

```python
from fideo_api.models.demographics import Demographics

# TODO update the JSON string below
json = "{}"
# create an instance of Demographics from a JSON string
demographics_instance = Demographics.from_json(json)
# print the JSON string representation of the object
print(Demographics.to_json())

# convert the object into a dict
demographics_dict = demographics_instance.to_dict()
# create an instance of Demographics from a dict
demographics_from_dict = Demographics.from_dict(demographics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


