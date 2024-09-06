# SignalsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**NameWithAlias**](NameWithAlias.md) |  | [optional] 
**demographics** | [**Demographics**](Demographics.md) |  | [optional] 
**locations** | [**List[Location]**](Location.md) |  | [optional] 
**emails** | [**List[Email]**](Email.md) |  | [optional] 
**phones** | [**List[Phone]**](Phone.md) |  | [optional] 
**person_ids** | **List[str]** |  | [optional] 
**ip_addresses** | [**List[IpAddress]**](IpAddress.md) |  | [optional] 
**message** | **str** |  | [optional] 
**social_profiles** | [**List[SocialProfileDetails]**](SocialProfileDetails.md) |  | [optional] 
**employment** | [**List[Employment]**](Employment.md) |  | [optional] 
**education** | [**List[Education]**](Education.md) |  | [optional] 
**photos** | [**List[Photo]**](Photo.md) |  | [optional] 
**economic** | [**Economic**](Economic.md) |  | [optional] 

## Example

```python
from fideo_api.models.signals_post200_response import SignalsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SignalsPost200Response from a JSON string
signals_post200_response_instance = SignalsPost200Response.from_json(json)
# print the JSON string representation of the object
print(SignalsPost200Response.to_json())

# convert the object into a dict
signals_post200_response_dict = signals_post200_response_instance.to_dict()
# create an instance of SignalsPost200Response from a dict
signals_post200_response_from_dict = SignalsPost200Response.from_dict(signals_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


