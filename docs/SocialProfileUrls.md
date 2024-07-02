# SocialProfileUrls


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**twitter_url** | **str** |  | [optional] 
**linked_in_url** | **str** |  | [optional] 

## Example

```python
from fideo_api.models.social_profile_urls import SocialProfileUrls

# TODO update the JSON string below
json = "{}"
# create an instance of SocialProfileUrls from a JSON string
social_profile_urls_instance = SocialProfileUrls.from_json(json)
# print the JSON string representation of the object
print(SocialProfileUrls.to_json())

# convert the object into a dict
social_profile_urls_dict = social_profile_urls_instance.to_dict()
# create an instance of SocialProfileUrls from a dict
social_profile_urls_from_dict = SocialProfileUrls.from_dict(social_profile_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


