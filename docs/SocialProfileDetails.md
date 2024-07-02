# SocialProfileDetails


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

## Example

```python
from fideo_api.models.social_profile_details import SocialProfileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SocialProfileDetails from a JSON string
social_profile_details_instance = SocialProfileDetails.from_json(json)
# print the JSON string representation of the object
print(SocialProfileDetails.to_json())

# convert the object into a dict
social_profile_details_dict = social_profile_details_instance.to_dict()
# create an instance of SocialProfileDetails from a dict
social_profile_details_from_dict = SocialProfileDetails.from_dict(social_profile_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


