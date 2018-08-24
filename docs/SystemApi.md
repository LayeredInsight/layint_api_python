# layint_api.SystemApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](SystemApi.md#health_check) | **GET** /HealthStatus | Get system health information
[**system_status_get**](SystemApi.md#system_status_get) | **GET** /SystemStatus | Returns information about components running on the system


# **health_check**
> HealthStatus health_check()

Get system health information

Returns information describing working parts of the system as well as event and error logs

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = layint_api.SystemApi()

try: 
    # Get system health information
    api_response = api_instance.health_check()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->health_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthStatus**](HealthStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_status_get**
> InlineResponse2003 system_status_get()

Returns information about components running on the system

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = layint_api.SystemApi()

try: 
    # Returns information about components running on the system
    api_response = api_instance.system_status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

