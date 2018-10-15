# layint_api.AlertsApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerts_delete**](AlertsApi.md#alerts_delete) | **DELETE** /Alerts | Delete alerts
[**alerts_get**](AlertsApi.md#alerts_get) | **GET** /Alerts | Get alerts


# **alerts_delete**
> alerts_delete(id)

Delete alerts

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
api_instance = layint_api.AlertsApi()
id = 'id_example' # str | Accepts: alert ID or \"all\"

try: 
    # Delete alerts
    api_instance.alerts_delete(id)
except ApiException as e:
    print("Exception when calling AlertsApi->alerts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Accepts: alert ID or \&quot;all\&quot; | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_get**
> Alerts alerts_get(show)

Get alerts

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
api_instance = layint_api.AlertsApi()
show = 'show_example' # str | Accepts: none, \"all\" or \"new\"

try: 
    # Get alerts
    api_response = api_instance.alerts_get(show)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alerts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show** | **str**| Accepts: none, \&quot;all\&quot; or \&quot;new\&quot; | 

### Return type

[**Alerts**](Alerts.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

