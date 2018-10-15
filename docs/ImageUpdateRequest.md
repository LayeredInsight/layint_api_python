# ImageUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 12 character internal hexadecimal identifier for the image to update | [optional] 
**push_registry** | **str** | 12 character hexadecimal internal identifier to layered insight record defining the push registry for a layered version of this image | [optional] 
**push_name** | **str** | Layered Image name for push registry (-layered tag will still be appended) | [optional] 
**config_id** | **str** | 12 character hexadecimal internal identifier for Runtime configuration for this Container | [optional] 
**policy_id** | **str** | Future enhancement. 12 character hexadecimal internal identifier  for the start up security policy built into the image during  instrumentation. This policy can be disabled with the Policy.Suspend  flag. The image runtime Configuration.PolicyID specifies the security  policy delivered once the Container LI agent establishes communication.  | [optional] 
**tags** | [**list[Tag]**](Tag.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


