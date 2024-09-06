# MultiFieldReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**twitter** | **str** |  | [optional] 
**linkedin** | **str** |  | [optional] 
**record_id** | **str** |  | [optional] 
**person_id** | **str** |  | [optional] 
**partner_id** | **str** |  | [optional] 
**location** | [**LocationReq**](LocationReq.md) |  | [optional] 
**avatar** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**emails** | **List[str]** |  | [optional] 
**phones** | **List[str]** |  | [optional] 
**profiles** | [**List[SocialProfileReq]**](SocialProfileReq.md) |  | [optional] 
**maids** | **List[str]** |  | [optional] 
**name** | [**PersonNameReq**](PersonNameReq.md) |  | [optional] 
**partner_keys** | **Dict[str, str]** |  | [optional] 
**li_nonid** | **str** |  | [optional] 
**panorama_id** | **str** |  | [optional] 
**placekey** | **str** |  | [optional] 
**generate_pid** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**profile** | [**SocialProfileReq**](SocialProfileReq.md) |  | [optional] 
**maid** | **str** |  | [optional] 

## Example

```python
from fideo_api.models.multi_field_req import MultiFieldReq

# TODO update the JSON string below
json = "{}"
# create an instance of MultiFieldReq from a JSON string
multi_field_req_instance = MultiFieldReq.from_json(json)
# print the JSON string representation of the object
print(MultiFieldReq.to_json())

# convert the object into a dict
multi_field_req_dict = multi_field_req_instance.to_dict()
# create an instance of MultiFieldReq from a dict
multi_field_req_from_dict = MultiFieldReq.from_dict(multi_field_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


