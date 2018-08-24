# layint_api.EventApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_event**](EventApi.md#describe_event) | **GET** /Events/{eventID} | Gets description about specific event
[**get_file_accessors**](EventApi.md#get_file_accessors) | **GET** /Events/{eventID}/FileAccessors | Get programs accessing a file
[**get_file_executors**](EventApi.md#get_file_executors) | **GET** /Events/{eventID}/FileExecutors | Get programs executing a file
[**get_source_ip**](EventApi.md#get_source_ip) | **GET** /Events/{eventID}/SourceIP | Get IP address used in event
[**get_source_log**](EventApi.md#get_source_log) | **GET** /Events/{eventID}/SourceLog | Get log that resulted in an event


# **describe_event**
> AlertEvents describe_event(event_id)

Gets description about specific event

Describes an event in a manner that can be understood by humans.

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
api_instance = layint_api.EventApi()
event_id = 'event_id_example' # str | hexadecimal ID of event to get description of

try: 
    # Gets description about specific event
    api_response = api_instance.describe_event(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->describe_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| hexadecimal ID of event to get description of | 

### Return type

[**AlertEvents**](AlertEvents.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_accessors**
> list[str] get_file_accessors(event_id)

Get programs accessing a file

Get a list of programs attempting to access the file in this event

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
api_instance = layint_api.EventApi()
event_id = 'event_id_example' # str | hexadecimal ID of event to get description of

try: 
    # Get programs accessing a file
    api_response = api_instance.get_file_accessors(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_file_accessors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| hexadecimal ID of event to get description of | 

### Return type

**list[str]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_executors**
> list[str] get_file_executors(event_id)

Get programs executing a file

Get a list of programs attempting to execute the file in this event

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
api_instance = layint_api.EventApi()
event_id = 'event_id_example' # str | hexadecimal ID of event to get description of

try: 
    # Get programs executing a file
    api_response = api_instance.get_file_executors(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_file_executors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| hexadecimal ID of event to get description of | 

### Return type

**list[str]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_ip**
> str get_source_ip(event_id)

Get IP address used in event

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
api_instance = layint_api.EventApi()
event_id = 'event_id_example' # str | hexadecimal ID of event to get description of

try: 
    # Get IP address used in event
    api_response = api_instance.get_source_ip(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_source_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| hexadecimal ID of event to get description of | 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_log**
> ContainerLog get_source_log(event_id)

Get log that resulted in an event

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
api_instance = layint_api.EventApi()
event_id = 'event_id_example' # str | hexadecimal ID of event to get description of

try: 
    # Get log that resulted in an event
    api_response = api_instance.get_source_log(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_source_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| hexadecimal ID of event to get description of | 

### Return type

[**ContainerLog**](ContainerLog.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

