# SignalPatternsTimeseriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** | Time interval for timeseries data | 
**count** | **int** | Number of data points to return | 

## Example

```python
from fideo_api.models.signal_patterns_timeseries_request import SignalPatternsTimeseriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignalPatternsTimeseriesRequest from a JSON string
signal_patterns_timeseries_request_instance = SignalPatternsTimeseriesRequest.from_json(json)
# print the JSON string representation of the object
print(SignalPatternsTimeseriesRequest.to_json())

# convert the object into a dict
signal_patterns_timeseries_request_dict = signal_patterns_timeseries_request_instance.to_dict()
# create an instance of SignalPatternsTimeseriesRequest from a dict
signal_patterns_timeseries_request_from_dict = SignalPatternsTimeseriesRequest.from_dict(signal_patterns_timeseries_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


