# SignalPatternResponseUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**observations** | **int** | Number of observations | [optional] 
**sources** | **int** | Number of sources | [optional] 
**events** | [**List[SignalPatternResponseUnitCount]**](SignalPatternResponseUnitCount.md) |  | [optional] 

## Example

```python
from fideo_api.models.signal_pattern_response_unit import SignalPatternResponseUnit

# TODO update the JSON string below
json = "{}"
# create an instance of SignalPatternResponseUnit from a JSON string
signal_pattern_response_unit_instance = SignalPatternResponseUnit.from_json(json)
# print the JSON string representation of the object
print(SignalPatternResponseUnit.to_json())

# convert the object into a dict
signal_pattern_response_unit_dict = signal_pattern_response_unit_instance.to_dict()
# create an instance of SignalPatternResponseUnit from a dict
signal_pattern_response_unit_from_dict = SignalPatternResponseUnit.from_dict(signal_pattern_response_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


