# layint_api.NotificationApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_all_notfications**](NotificationApi.md#list_all_notfications) | **GET** /Notifications | Get all notifications
[**show_notification_details**](NotificationApi.md#show_notification_details) | **GET** /Notifications/{NotificationId} | Get notification


# **list_all_notfications**
> Notifications list_all_notfications()

Get all notifications

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
api_instance = layint_api.NotificationApi()

try: 
    # Get all notifications
    api_response = api_instance.list_all_notfications()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->list_all_notfications: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Notifications**](Notifications.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_notification_details**
> Notification show_notification_details(notification_id)

Get notification

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
api_instance = layint_api.NotificationApi()
notification_id = 'notification_id_example' # str | hexadecimal ID of notification to get

try: 
    # Get notification
    api_response = api_instance.show_notification_details(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->show_notification_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| hexadecimal ID of notification to get | 

### Return type

[**Notification**](Notification.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

