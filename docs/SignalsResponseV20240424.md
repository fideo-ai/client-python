# SignalsResponseV20240424


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
from fideo_api.models.signals_response_v20240424 import SignalsResponseV20240424

# TODO update the JSON string below
json = "{}"
# create an instance of SignalsResponseV20240424 from a JSON string
signals_response_v20240424_instance = SignalsResponseV20240424.from_json(json)
# print the JSON string representation of the object
print(SignalsResponseV20240424.to_json())

# convert the object into a dict
signals_response_v20240424_dict = signals_response_v20240424_instance.to_dict()
# create an instance of SignalsResponseV20240424 from a dict
signals_response_v20240424_from_dict = SignalsResponseV20240424.from_dict(signals_response_v20240424_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


