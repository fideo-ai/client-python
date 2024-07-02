# EmploymentDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**month** | **int** |  | [optional] 
**day** | **int** |  | [optional] 

## Example

```python
from fideo_api.models.employment_date import EmploymentDate

# TODO update the JSON string below
json = "{}"
# create an instance of EmploymentDate from a JSON string
employment_date_instance = EmploymentDate.from_json(json)
# print the JSON string representation of the object
print(EmploymentDate.to_json())

# convert the object into a dict
employment_date_dict = employment_date_instance.to_dict()
# create an instance of EmploymentDate from a dict
employment_date_from_dict = EmploymentDate.from_dict(employment_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


