# layint_api.ClairApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clair_update**](ClairApi.md#clair_update) | **POST** /Scan/ClairUpdate | Notify user(s) of vulnerability update from clair notification
[**get_clair_updates**](ClairApi.md#get_clair_updates) | **GET** /Scan/Updates | Returns date/time estimation when clair updates will be done


# **clair_update**
> str clair_update(clair_update_request)

Notify user(s) of vulnerability update from clair notification

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = layint_api.ClairApi()
clair_update_request = layint_api.ClairUpdateRequest() # ClairUpdateRequest | 

try: 
    # Notify user(s) of vulnerability update from clair notification
    api_response = api_instance.clair_update(clair_update_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClairApi->clair_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clair_update_request** | [**ClairUpdateRequest**](ClairUpdateRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clair_updates**
> InlineResponse2002 get_clair_updates()

Returns date/time estimation when clair updates will be done

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = layint_api.ClairApi()

try: 
    # Returns date/time estimation when clair updates will be done
    api_response = api_instance.get_clair_updates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClairApi->get_clair_updates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

