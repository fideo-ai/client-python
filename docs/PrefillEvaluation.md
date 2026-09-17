# PrefillEvaluation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk** | **float** |  | [optional] 
**checks** | [**List[CheckResult]**](CheckResult.md) |  | [optional] 

## Example

```python
from fideo_api.models.prefill_evaluation import PrefillEvaluation

# TODO update the JSON string below
json = "{}"
# create an instance of PrefillEvaluation from a JSON string
prefill_evaluation_instance = PrefillEvaluation.from_json(json)
# print the JSON string representation of the object
print(PrefillEvaluation.to_json())

# convert the object into a dict
prefill_evaluation_dict = prefill_evaluation_instance.to_dict()
# create an instance of PrefillEvaluation from a dict
prefill_evaluation_from_dict = PrefillEvaluation.from_dict(prefill_evaluation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


