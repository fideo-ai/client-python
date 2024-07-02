# EducationDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**month** | **int** |  | [optional] 
**day** | **int** |  | [optional] 

## Example

```python
from fideo_api.models.education_date import EducationDate

# TODO update the JSON string below
json = "{}"
# create an instance of EducationDate from a JSON string
education_date_instance = EducationDate.from_json(json)
# print the JSON string representation of the object
print(EducationDate.to_json())

# convert the object into a dict
education_date_dict = education_date_instance.to_dict()
# create an instance of EducationDate from a dict
education_date_from_dict = EducationDate.from_dict(education_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


