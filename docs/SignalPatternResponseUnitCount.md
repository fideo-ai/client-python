# SignalPatternResponseUnitCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of event | [optional] 
**observations** | **int** | Number of observations | [optional] 
**sources** | **int** | Number of sources | [optional] 

## Example

```python
from fideo_api.models.signal_pattern_response_unit_count import SignalPatternResponseUnitCount

# TODO update the JSON string below
json = "{}"
# create an instance of SignalPatternResponseUnitCount from a JSON string
signal_pattern_response_unit_count_instance = SignalPatternResponseUnitCount.from_json(json)
# print the JSON string representation of the object
print(SignalPatternResponseUnitCount.to_json())

# convert the object into a dict
signal_pattern_response_unit_count_dict = signal_pattern_response_unit_count_instance.to_dict()
# create an instance of SignalPatternResponseUnitCount from a dict
signal_pattern_response_unit_count_from_dict = SignalPatternResponseUnitCount.from_dict(signal_pattern_response_unit_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


