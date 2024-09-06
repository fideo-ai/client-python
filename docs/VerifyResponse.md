# VerifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**region_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**continent** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 
**given_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**maid** | **str** |  | [optional] 
**social** | **str** |  | [optional] 
**non_id** | **str** |  | [optional] 
**panorama_id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**birthday** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**risk** | **float** |  | [optional] 
**evidence** | [**Evidence**](Evidence.md) |  | [optional] 
**risk_v2** | **float** |  | [optional] 
**risk_v3** | **float** |  | [optional] 
**score_details** | [**List[ScoreDetails]**](ScoreDetails.md) |  | [optional] 

## Example

```python
from fideo_api.models.verify_response import VerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyResponse from a JSON string
verify_response_instance = VerifyResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyResponse.to_json())

# convert the object into a dict
verify_response_dict = verify_response_instance.to_dict()
# create an instance of VerifyResponse from a dict
verify_response_from_dict = VerifyResponse.from_dict(verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


