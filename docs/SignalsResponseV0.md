# SignalsResponseV0


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**Name**](Name.md) |  | [optional] 
**demographics** | [**Demographics**](Demographics.md) |  | [optional] 
**locations** | [**List[Location]**](Location.md) |  | [optional] 
**emails** | [**List[Email]**](Email.md) |  | [optional] 
**phones** | [**List[Phone]**](Phone.md) |  | [optional] 
**person_ids** | **List[str]** |  | [optional] 
**ip_addresses** | [**List[IpAddress]**](IpAddress.md) |  | [optional] 
**message** | **str** |  | [optional] 
**social_profiles** | [**SocialProfileUrls**](SocialProfileUrls.md) |  | [optional] 
**employment** | [**Employment**](Employment.md) |  | [optional] 

## Example

```python
from fideo_api.models.signals_response_v0 import SignalsResponseV0

# TODO update the JSON string below
json = "{}"
# create an instance of SignalsResponseV0 from a JSON string
signals_response_v0_instance = SignalsResponseV0.from_json(json)
# print the JSON string representation of the object
print(SignalsResponseV0.to_json())

# convert the object into a dict
signals_response_v0_dict = signals_response_v0_instance.to_dict()
# create an instance of SignalsResponseV0 from a dict
signals_response_v0_from_dict = SignalsResponseV0.from_dict(signals_response_v0_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


