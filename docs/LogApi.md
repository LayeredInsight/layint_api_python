# layint_api.LogApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**array_of_dropped_logs**](LogApi.md#array_of_dropped_logs) | **GET** /LogsDropped | Get histograph of policy hits
[**show_logs**](LogApi.md#show_logs) | **GET** /Logs | Get all logs
[**show_logs_for_container**](LogApi.md#show_logs_for_container) | **GET** /Logs/{ContainerId} | Get container logs


# **array_of_dropped_logs**
> LevelSyscallMetrics array_of_dropped_logs(starting_time, ending_time, seconds_per_interval)

Get histograph of policy hits

Get array with the amount of policy hits within a timeframe

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
api_instance = layint_api.LogApi()
starting_time = 'starting_time_example' # str | Time from when histograph should start
ending_time = 'ending_time_example' # str | Time from when histograph should end
seconds_per_interval = 'seconds_per_interval_example' # str | Histograph resolution

try: 
    # Get histograph of policy hits
    api_response = api_instance.array_of_dropped_logs(starting_time, ending_time, seconds_per_interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogApi->array_of_dropped_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starting_time** | **str**| Time from when histograph should start | 
 **ending_time** | **str**| Time from when histograph should end | 
 **seconds_per_interval** | **str**| Histograph resolution | 

### Return type

[**LevelSyscallMetrics**](LevelSyscallMetrics.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_logs**
> ContainerLogs show_logs()

Get all logs

Get all logs for a user

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = layint_api.LogApi()

try: 
    # Get all logs
    api_response = api_instance.show_logs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogApi->show_logs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ContainerLogs**](ContainerLogs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_logs_for_container**
> ContainerLogs show_logs_for_container(container_id)

Get container logs

Get all logs belonging to a container

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = layint_api.LogApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to get logs from

try: 
    # Get container logs
    api_response = api_instance.show_logs_for_container(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogApi->show_logs_for_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to get logs from | 

### Return type

[**ContainerLogs**](ContainerLogs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

