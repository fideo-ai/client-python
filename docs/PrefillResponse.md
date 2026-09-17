# PrefillResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **UUID** | UUIDv7 session identifier to send with reviewed identity data. | 
**status** | **str** |  | 
**individual** | [**MultiFieldReqWithOptions**](MultiFieldReqWithOptions.md) | Resolved identity in the same multifield shape accepted by the follow-up Prefill request. The caller may review or edit these values and resubmit them with the returned sessionId. | [optional] 
**evaluation** | [**PrefillEvaluation**](PrefillEvaluation.md) |  | [optional] 

## Example

```python
from fideo_api.models.prefill_response import PrefillResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrefillResponse from a JSON string
prefill_response_instance = PrefillResponse.from_json(json)
# print the JSON string representation of the object
print(PrefillResponse.to_json())

# convert the object into a dict
prefill_response_dict = prefill_response_instance.to_dict()
# create an instance of PrefillResponse from a dict
prefill_response_from_dict = PrefillResponse.from_dict(prefill_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


