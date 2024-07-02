# NameWithAlias


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** |  | [optional] 
**last** | **str** |  | [optional] 
**middle** | **str** |  | [optional] 
**given_name** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 
**aliases** | [**List[Alias]**](Alias.md) |  | [optional] 

## Example

```python
from fideo_api.models.name_with_alias import NameWithAlias

# TODO update the JSON string below
json = "{}"
# create an instance of NameWithAlias from a JSON string
name_with_alias_instance = NameWithAlias.from_json(json)
# print the JSON string representation of the object
print(NameWithAlias.to_json())

# convert the object into a dict
name_with_alias_dict = name_with_alias_instance.to_dict()
# create an instance of NameWithAlias from a dict
name_with_alias_from_dict = NameWithAlias.from_dict(name_with_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


