# SignalPatternsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address to get signal patterns for | 

## Example

```python
from fideo_api.models.signal_patterns_request import SignalPatternsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignalPatternsRequest from a JSON string
signal_patterns_request_instance = SignalPatternsRequest.from_json(json)
# print the JSON string representation of the object
print(SignalPatternsRequest.to_json())

# convert the object into a dict
signal_patterns_request_dict = signal_patterns_request_instance.to_dict()
# create an instance of SignalPatternsRequest from a dict
signal_patterns_request_from_dict = SignalPatternsRequest.from_dict(signal_patterns_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


