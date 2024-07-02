# ScoreDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scorer** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**evidence** | **Dict[str, object]** |  | [optional] 
**weight** | **float** |  | [optional] 

## Example

```python
from fideo_api.models.score_details import ScoreDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreDetails from a JSON string
score_details_instance = ScoreDetails.from_json(json)
# print the JSON string representation of the object
print(ScoreDetails.to_json())

# convert the object into a dict
score_details_dict = score_details_instance.to_dict()
# create an instance of ScoreDetails from a dict
score_details_from_dict = ScoreDetails.from_dict(score_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


