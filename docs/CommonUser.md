# CommonUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | BsonObjectID string unique to the User | [optional] 
**username** | **str** | Username of the User | [optional] 
**password** | **str** | Encrypted password of the User | [optional] 
**first_name** | **str** | First Name of the User | [optional] 
**last_name** | **str** | Last Name of the User | [optional] 
**email** | **str** | Email ID of the User | [optional] 
**company_id** | **str** | BsonObjectID string unique to the company | [optional] 
**suspended** | **str** | Indicates if the User has been suspended or not | [optional] 
**ui_setting** | [**CommonUserUISetting**](CommonUserUISetting.md) |  | [optional] 
**group_id** | **str** | BsonObjectID string of the group to which the user belongs | [optional] 
**roles** | [**list[Role]**](Role.md) | Roles assigned to the User | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


