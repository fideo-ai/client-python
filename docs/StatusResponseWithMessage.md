# StatusResponseWithMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from fideo_api.models.status_response_with_message import StatusResponseWithMessage

# TODO update the JSON string below
json = "{}"
# create an instance of StatusResponseWithMessage from a JSON string
status_response_with_message_instance = StatusResponseWithMessage.from_json(json)
# print the JSON string representation of the object
print(StatusResponseWithMessage.to_json())

# convert the object into a dict
status_response_with_message_dict = status_response_with_message_instance.to_dict()
# create an instance of StatusResponseWithMessage from a dict
status_response_with_message_from_dict = StatusResponseWithMessage.from_dict(status_response_with_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


