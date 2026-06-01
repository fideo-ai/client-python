# SignalPatternRecencyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour** | [**SignalPatternResponseUnit**](SignalPatternResponseUnit.md) |  | [optional] 
**day** | [**SignalPatternResponseUnit**](SignalPatternResponseUnit.md) |  | [optional] 
**week** | [**SignalPatternResponseUnit**](SignalPatternResponseUnit.md) |  | [optional] 
**month** | [**SignalPatternResponseUnit**](SignalPatternResponseUnit.md) |  | [optional] 
**six_month** | [**SignalPatternResponseUnit**](SignalPatternResponseUnit.md) |  | [optional] 
**year** | [**SignalPatternResponseUnit**](SignalPatternResponseUnit.md) |  | [optional] 

## Example

```python
from fideo_api.models.signal_pattern_recency_response import SignalPatternRecencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SignalPatternRecencyResponse from a JSON string
signal_pattern_recency_response_instance = SignalPatternRecencyResponse.from_json(json)
# print the JSON string representation of the object
print(SignalPatternRecencyResponse.to_json())

# convert the object into a dict
signal_pattern_recency_response_dict = signal_pattern_recency_response_instance.to_dict()
# create an instance of SignalPatternRecencyResponse from a dict
signal_pattern_recency_response_from_dict = SignalPatternRecencyResponse.from_dict(signal_pattern_recency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


