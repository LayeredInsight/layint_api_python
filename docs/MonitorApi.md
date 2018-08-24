# layint_api.MonitorApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**monitor**](MonitorApi.md#monitor) | **GET** /Monitor/{Minutes} | Get policy hits


# **monitor**
> PolicyHits monitor(minutes)

Get policy hits

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
api_instance = layint_api.MonitorApi()
minutes = 'minutes_example' # str | Time frame in minutes

try: 
    # Get policy hits
    api_response = api_instance.monitor(minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minutes** | **str**| Time frame in minutes | 

### Return type

[**PolicyHits**](PolicyHits.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

