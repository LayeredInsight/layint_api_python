# Registry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 12 character internal hexadecimal identifier for this Registry | [optional] 
**name** | **str** | Name to refer to registry with and display | [optional] 
**user_id** | **str** | User ID of owner of the image | [optional] 
**group_id** | **str** | Group ID of owner of the image | [optional] 
**url** | **str** | URL to registry | [optional] 
**type** | **str** | Type of registry | [optional] 
**username** | **str** | Username credential for docker.io, dtr registries | [optional] 
**password** | **str** | Password credential for docker.io, dtr registries | [optional] 
**access_token** | **str** | Access token credential for Quay registries | [optional] 
**certificate** | **str** | Base64 encoded registry certificate | [optional] 
**tls_verify** | **bool** | Enables server certificate verification | [optional] [default to True]
**insecure_registry** | **bool** | Allows HTTP protocol requests when set insecure | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


