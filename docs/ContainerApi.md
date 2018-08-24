# layint_api.ContainerApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_configuration_to_container**](ContainerApi.md#assign_configuration_to_container) | **POST** /Containers/{containerID}/Configs/{configID} | Assign configuration to a container
[**build_container_dossier_tempate**](ContainerApi.md#build_container_dossier_tempate) | **GET** /Containers/{containerID}/DossierTemplate | Builds a security policy based on containers behavior
[**delete_container**](ContainerApi.md#delete_container) | **DELETE** /Containers/{containerID} | Delete a container
[**dropped_logs_of_container**](ContainerApi.md#dropped_logs_of_container) | **GET** /Containers/{containerID}/DroppedLogsOfContainer | Generates data used for UI
[**edit_container**](ContainerApi.md#edit_container) | **POST** /Containers/{containerID} | Edit a container
[**five_most_divergent_containers**](ContainerApi.md#five_most_divergent_containers) | **GET** /ContainersFiveMostDivergent | 
[**function_metrics**](ContainerApi.md#function_metrics) | **GET** /Containers/{containerID}/FunctionMetrics | Get occurance of system calls in time
[**functions**](ContainerApi.md#functions) | **GET** /Containers/{containerID}/Functions | Get a list of system calls a container has made
[**get_container_dossier**](ContainerApi.md#get_container_dossier) | **GET** /Containers/{containerID}/Dossier | Gets dossier for container
[**get_container_logs**](ContainerApi.md#get_container_logs) | **GET** /Containers/{containerID}/GetContainerLogs | Gets behavioral logs for container
[**get_containers**](ContainerApi.md#get_containers) | **GET** /Containers | Get containers
[**get_resource_matrics**](ContainerApi.md#get_resource_matrics) | **GET** /Containers/{containerID}/ResourceMetrics | Get current total container resource usage
[**languages**](ContainerApi.md#languages) | **GET** /Containers/{containerID}/Languages | Get information about what languages are running in the container
[**level_syscall_category_metrics**](ContainerApi.md#level_syscall_category_metrics) | **GET** /Containers/{containerID}/LevelSyscallCategoryMetrics | Get histograph information for system calls divided into category groups
[**level_syscall_metrics**](ContainerApi.md#level_syscall_metrics) | **GET** /Containers/{containerID}/LevelSyscallMetrics | Get histograph information for system calls
[**number_of_running_containers**](ContainerApi.md#number_of_running_containers) | **GET** /ContainersRunning | Get number of containers currently running
[**passivate_container**](ContainerApi.md#passivate_container) | **POST** /Containers/{containerID}/Passivate | Toggle the container behavior between passive and active
[**post_behavioral_logging**](ContainerApi.md#post_behavioral_logging) | **POST** /Containers/{containerID}/BehavioralLogging | Toggle behavioral logging on/off
[**show_container_details**](ContainerApi.md#show_container_details) | **GET** /Containers/{containerID} | Get a container
[**singel_syscall**](ContainerApi.md#singel_syscall) | **GET** /Containers/{containerID}/SingleSyscall | Get amount of calls to a system call number in the last 5 seconds
[**toggle_container_sniffer**](ContainerApi.md#toggle_container_sniffer) | **POST** /Containers/{containerID}/ToggleSniffer | Toggles network sniffer


# **assign_configuration_to_container**
> Container assign_configuration_to_container(container_id, config_id)

Assign configuration to a container

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to assign configuration to
config_id = 'config_id_example' # str | hexadecimal ID of configuration

try: 
    # Assign configuration to a container
    api_response = api_instance.assign_configuration_to_container(container_id, config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->assign_configuration_to_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to assign configuration to | 
 **config_id** | **str**| hexadecimal ID of configuration | 

### Return type

[**Container**](Container.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_container_dossier_tempate**
> DossierTemplateResponse build_container_dossier_tempate(container_id, merge_policy_id=merge_policy_id, log_action=log_action)

Builds a security policy based on containers behavior

This call builds a new custom security policy based on the recorded activities of the container.

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to gather dossier for
merge_policy_id = 'merge_policy_id_example' # str | hexadecimal ID of policy to merge gathered dossier rules (optional)
log_action = 'all' # str | action string to match action type in log for gathered dossier rules (optional) (default to all)

try: 
    # Builds a security policy based on containers behavior
    api_response = api_instance.build_container_dossier_tempate(container_id, merge_policy_id=merge_policy_id, log_action=log_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->build_container_dossier_tempate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to gather dossier for | 
 **merge_policy_id** | **str**| hexadecimal ID of policy to merge gathered dossier rules | [optional] 
 **log_action** | **str**| action string to match action type in log for gathered dossier rules | [optional] [default to all]

### Return type

[**DossierTemplateResponse**](DossierTemplateResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_container**
> delete_container(container_id)

Delete a container

Delete a container

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to delete

try: 
    # Delete a container
    api_instance.delete_container(container_id)
except ApiException as e:
    print("Exception when calling ContainerApi->delete_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dropped_logs_of_container**
> DroppedLogsOfContainer dropped_logs_of_container(container_id, starting_time)

Generates data used for UI

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to get data from
starting_time = 'starting_time_example' # str | specify the from what date to get data

try: 
    # Generates data used for UI
    api_response = api_instance.dropped_logs_of_container(container_id, starting_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->dropped_logs_of_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to get data from | 
 **starting_time** | **str**| specify the from what date to get data | 

### Return type

[**DroppedLogsOfContainer**](DroppedLogsOfContainer.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_container**
> Container edit_container(container_id, container=container)

Edit a container

Edit a container

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to get
container = layint_api.Container() # Container |  (optional)

try: 
    # Edit a container
    api_response = api_instance.edit_container(container_id, container=container)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->edit_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to get | 
 **container** | [**Container**](Container.md)|  | [optional] 

### Return type

[**Container**](Container.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **five_most_divergent_containers**
> list[Containers] five_most_divergent_containers()



Return a list with the top five alert triggering containers.

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
api_instance = layint_api.ContainerApi()

try: 
    api_response = api_instance.five_most_divergent_containers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->five_most_divergent_containers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Containers]**](Containers.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **function_metrics**
> ContainerSystemcallMetrics function_metrics(container_id, starting_time, ending_time, seconds_per_interval, system_call=system_call, language=language)

Get occurance of system calls in time

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to get system call matrices from
starting_time = 'starting_time_example' # str | Date from when to get data
ending_time = 'ending_time_example' # str | End date for data to get
seconds_per_interval = 'seconds_per_interval_example' # str | Resolution for output
system_call = 'system_call_example' # str | Specify a system call to get data for (optional)
language = 'language_example' # str | Get calls for a given language (optional)

try: 
    # Get occurance of system calls in time
    api_response = api_instance.function_metrics(container_id, starting_time, ending_time, seconds_per_interval, system_call=system_call, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->function_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to get system call matrices from | 
 **starting_time** | **str**| Date from when to get data | 
 **ending_time** | **str**| End date for data to get | 
 **seconds_per_interval** | **str**| Resolution for output | 
 **system_call** | **str**| Specify a system call to get data for | [optional] 
 **language** | **str**| Get calls for a given language | [optional] 

### Return type

[**ContainerSystemcallMetrics**](ContainerSystemcallMetrics.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **functions**
> ContainerSyscalls functions(container_id, starting_time=starting_time, system_call=system_call, language=language)

Get a list of system calls a container has made

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to get system call from
starting_time = 'starting_time_example' # str | Date from when to get data (optional)
system_call = 'system_call_example' # str | Get a systemcall by number (optional)
language = 'language_example' # str | Get calls for a given language (optional)

try: 
    # Get a list of system calls a container has made
    api_response = api_instance.functions(container_id, starting_time=starting_time, system_call=system_call, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->functions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to get system call from | 
 **starting_time** | **str**| Date from when to get data | [optional] 
 **system_call** | **str**| Get a systemcall by number | [optional] 
 **language** | **str**| Get calls for a given language | [optional] 

### Return type

[**ContainerSyscalls**](ContainerSyscalls.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_dossier**
> Dossier get_container_dossier(container_id)

Gets dossier for container

This call produces a list of all data Witness has learend about the container

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to gather dossier for

try: 
    # Gets dossier for container
    api_response = api_instance.get_container_dossier(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_dossier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to gather dossier for | 

### Return type

[**Dossier**](Dossier.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_logs**
> ContainerLogs get_container_logs(container_id, page_size=page_size, page=page)

Gets behavioral logs for container

This call produces a list of all behavior logs Witness has received for the container

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to gather logs for
page_size = 56 # int | Maximum number of log records to return per \"page\" (think pager in a browser) (optional)
page = 56 # int | Page number of results to return. Results will start with record number (Page * PageSize) (optional)

try: 
    # Gets behavioral logs for container
    api_response = api_instance.get_container_logs(container_id, page_size=page_size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to gather logs for | 
 **page_size** | **int**| Maximum number of log records to return per \&quot;page\&quot; (think pager in a browser) | [optional] 
 **page** | **int**| Page number of results to return. Results will start with record number (Page * PageSize) | [optional] 

### Return type

[**ContainerLogs**](ContainerLogs.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_containers**
> Containers get_containers()

Get containers

Returns a list of containers that are accessible to this user.

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
api_instance = layint_api.ContainerApi()

try: 
    # Get containers
    api_response = api_instance.get_containers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_containers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Containers**](Containers.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_matrics**
> TotStats get_resource_matrics(container_id)

Get current total container resource usage

Return resources currently being used in the running container. Resources includes percentage of total of cpu utilization and memory utilization.

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to get resource usage from

try: 
    # Get current total container resource usage
    api_response = api_instance.get_resource_matrics(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_resource_matrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to get resource usage from | 

### Return type

[**TotStats**](TotStats.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **languages**
> list[str] languages(container_id)

Get information about what languages are running in the container

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to 'passivate'

try: 
    # Get information about what languages are running in the container
    api_response = api_instance.languages(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to &#39;passivate&#39; | 

### Return type

**list[str]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **level_syscall_category_metrics**
> LevelSyscallCategoryMetrics level_syscall_category_metrics(container_id, starting_time)

Get histograph information for system calls divided into category groups

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to get metrics from
starting_time = 'starting_time_example' # str | Time from when histograph should start

try: 
    # Get histograph information for system calls divided into category groups
    api_response = api_instance.level_syscall_category_metrics(container_id, starting_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->level_syscall_category_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to get metrics from | 
 **starting_time** | **str**| Time from when histograph should start | 

### Return type

[**LevelSyscallCategoryMetrics**](LevelSyscallCategoryMetrics.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **level_syscall_metrics**
> LevelSyscallMetrics level_syscall_metrics(container_id, starting_time, systemcall=systemcall, language=language, function_name=function_name)

Get histograph information for system calls

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to get metrics from
starting_time = 'starting_time_example' # str | Time from when histograph should start
systemcall = 'systemcall_example' # str | Get histograph for specific system call number (optional)
language = 'language_example' # str | Get histograph for specific language (optional)
function_name = 'function_name_example' # str | Get histograph for specific system call name (optional)

try: 
    # Get histograph information for system calls
    api_response = api_instance.level_syscall_metrics(container_id, starting_time, systemcall=systemcall, language=language, function_name=function_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->level_syscall_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to get metrics from | 
 **starting_time** | **str**| Time from when histograph should start | 
 **systemcall** | **str**| Get histograph for specific system call number | [optional] 
 **language** | **str**| Get histograph for specific language | [optional] 
 **function_name** | **str**| Get histograph for specific system call name | [optional] 

### Return type

[**LevelSyscallMetrics**](LevelSyscallMetrics.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **number_of_running_containers**
> int number_of_running_containers()

Get number of containers currently running

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
api_instance = layint_api.ContainerApi()

try: 
    # Get number of containers currently running
    api_response = api_instance.number_of_running_containers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->number_of_running_containers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **passivate_container**
> Container passivate_container(container_id)

Toggle the container behavior between passive and active

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to 'passivate'

try: 
    # Toggle the container behavior between passive and active
    api_response = api_instance.passivate_container(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->passivate_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to &#39;passivate&#39; | 

### Return type

[**Container**](Container.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_behavioral_logging**
> BehavioralStatus post_behavioral_logging(container_id)

Toggle behavioral logging on/off

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to toggle

try: 
    # Toggle behavioral logging on/off
    api_response = api_instance.post_behavioral_logging(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->post_behavioral_logging: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to toggle | 

### Return type

[**BehavioralStatus**](BehavioralStatus.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_container_details**
> Container show_container_details(container_id)

Get a container

Get a container

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to get

try: 
    # Get a container
    api_response = api_instance.show_container_details(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->show_container_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to get | 

### Return type

[**Container**](Container.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **singel_syscall**
> int singel_syscall(container_id, system_call)

Get amount of calls to a system call number in the last 5 seconds

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of container to get metrics from
system_call = 'system_call_example' # str | System call number

try: 
    # Get amount of calls to a system call number in the last 5 seconds
    api_response = api_instance.singel_syscall(container_id, system_call)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->singel_syscall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of container to get metrics from | 
 **system_call** | **str**| System call number | 

### Return type

**int**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_container_sniffer**
> Container toggle_container_sniffer(container_id)

Toggles network sniffer

Toggles network sniffer on/off for specified container. This call doesn't take any parameters beside the container ID - each call of the API toggles the sniffer setting between enabled and disabled. Sniffer in a running container will change status within 30 seconds of this API call.

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
api_instance = layint_api.ContainerApi()
container_id = 'container_id_example' # str | hexadecimal ID of registry to return

try: 
    # Toggles network sniffer
    api_response = api_instance.toggle_container_sniffer(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->toggle_container_sniffer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| hexadecimal ID of registry to return | 

### Return type

[**Container**](Container.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

