# layint_api.UsersApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](UsersApi.md#add_user) | **POST** /Users | Add User
[**assign_groups_to_user**](UsersApi.md#assign_groups_to_user) | **POST** /Users/{UserID}/Groups | Assign Group
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /Users/{UserID} | Delete the specified user
[**list_user_by_id**](UsersApi.md#list_user_by_id) | **GET** /Users/{UserID} | Get specified UserID
[**list_users**](UsersApi.md#list_users) | **GET** /Users | List Users
[**modify_user**](UsersApi.md#modify_user) | **POST** /Users/{UserID} | Modify User
[**search_user_by_email**](UsersApi.md#search_user_by_email) | **POST** /UsersSearch | Search User
[**suspend_user**](UsersApi.md#suspend_user) | **POST** /Users/{UserID}/Suspend | Suspend User


# **add_user**
> APIResponseUser add_user(common_user=common_user)

Add User

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_api.UsersApi()
common_user = layint_api.CommonUser() # CommonUser |  (optional)

try: 
    # Add User
    api_response = api_instance.add_user(common_user=common_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_user** | [**CommonUser**](CommonUser.md)|  | [optional] 

### Return type

[**APIResponseUser**](APIResponseUser.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_groups_to_user**
> UserGroups assign_groups_to_user(user_id, hold_group=hold_group)

Assign Group

Assigns Group to UserID

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_api.UsersApi()
user_id = 'user_id_example' # str | hexadecimal ID of the User
hold_group = layint_api.HoldGroup() # HoldGroup |  (optional)

try: 
    # Assign Group
    api_response = api_instance.assign_groups_to_user(user_id, hold_group=hold_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->assign_groups_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| hexadecimal ID of the User | 
 **hold_group** | [**HoldGroup**](HoldGroup.md)|  | [optional] 

### Return type

[**UserGroups**](UserGroups.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id)

Delete the specified user

Deletes the specified UserID

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_api.UsersApi()
user_id = 'user_id_example' # str | hexadecimal ID of User

try: 
    # Delete the specified user
    api_instance.delete_user(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| hexadecimal ID of User | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_by_id**
> APIResponseUser list_user_by_id(user_id)

Get specified UserID

Returns details about specified UserID.

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_api.UsersApi()
user_id = 'user_id_example' # str | hexadecimal ID of the User

try: 
    # Get specified UserID
    api_response = api_instance.list_user_by_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| hexadecimal ID of the User | 

### Return type

[**APIResponseUser**](APIResponseUser.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> APIResponseUser list_users()

List Users

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_api.UsersApi()

try: 
    # List Users
    api_response = api_instance.list_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIResponseUser**](APIResponseUser.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_user**
> CommonUser modify_user(user_id, api_response_user=api_response_user)

Modify User

Modifies an existing UserID.

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_api.UsersApi()
user_id = 'user_id_example' # str | hexadecimal ID of the User
api_response_user = layint_api.APIResponseUser() # APIResponseUser |  (optional)

try: 
    # Modify User
    api_response = api_instance.modify_user(user_id, api_response_user=api_response_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->modify_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| hexadecimal ID of the User | 
 **api_response_user** | [**APIResponseUser**](APIResponseUser.md)|  | [optional] 

### Return type

[**CommonUser**](CommonUser.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_user_by_email**
> APIResponseUser search_user_by_email(search_by=search_by)

Search User

Searches User by Email

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_api.UsersApi()
search_by = layint_api.SearchBy() # SearchBy |  (optional)

try: 
    # Search User
    api_response = api_instance.search_user_by_email(search_by=search_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->search_user_by_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by** | [**SearchBy**](SearchBy.md)|  | [optional] 

### Return type

[**APIResponseUser**](APIResponseUser.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_user**
> APIResponseUser suspend_user(user_id)

Suspend User

Suspends UserID

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
layint_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# layint_api.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = layint_api.UsersApi()
user_id = 'user_id_example' # str | hexadecimal ID of the User

try: 
    # Suspend User
    api_response = api_instance.suspend_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->suspend_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| hexadecimal ID of the User | 

### Return type

[**APIResponseUser**](APIResponseUser.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

