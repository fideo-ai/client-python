# SocialProfileReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**userid** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**service** | **str** |  | [optional] 
**followers** | **int** |  | [optional] 
**following** | **int** |  | [optional] 
**score** | **int** |  | [optional] 

## Example

```python
from fideo_api.models.social_profile_req import SocialProfileReq

# TODO update the JSON string below
json = "{}"
# create an instance of SocialProfileReq from a JSON string
social_profile_req_instance = SocialProfileReq.from_json(json)
# print the JSON string representation of the object
print(SocialProfileReq.to_json())

# convert the object into a dict
social_profile_req_dict = social_profile_req_instance.to_dict()
# create an instance of SocialProfileReq from a dict
social_profile_req_from_dict = SocialProfileReq.from_dict(social_profile_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


