# LocationReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**region_code** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**formatted** | **str** |  | [optional] 
**type** | [**LocationType**](LocationType.md) |  | [optional] 

## Example

```python
from fideo_api.models.location_req import LocationReq

# TODO update the JSON string below
json = "{}"
# create an instance of LocationReq from a JSON string
location_req_instance = LocationReq.from_json(json)
# print the JSON string representation of the object
print(LocationReq.to_json())

# convert the object into a dict
location_req_dict = location_req_instance.to_dict()
# create an instance of LocationReq from a dict
location_req_from_dict = LocationReq.from_dict(location_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


