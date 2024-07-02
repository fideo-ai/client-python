# Economic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dwelling_type** | **str** |  | [optional] 
**home_ownership** | **str** |  | [optional] 
**marital_status** | **str** |  | [optional] 
**presence_of_children** | **str** |  | [optional] 
**income** | **str** |  | [optional] 
**net_worth** | **str** |  | [optional] 

## Example

```python
from fideo_api.models.economic import Economic

# TODO update the JSON string below
json = "{}"
# create an instance of Economic from a JSON string
economic_instance = Economic.from_json(json)
# print the JSON string representation of the object
print(Economic.to_json())

# convert the object into a dict
economic_dict = economic_instance.to_dict()
# create an instance of Economic from a dict
economic_from_dict = Economic.from_dict(economic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


