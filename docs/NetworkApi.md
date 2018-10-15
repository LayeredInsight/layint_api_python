# layint_api.NetworkApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_map**](NetworkApi.md#network_map) | **GET** /NetworkMap | Get network topology between running containers


# **network_map**
> NetworkMap network_map()

Get network topology between running containers

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
api_instance = layint_api.NetworkApi()

try: 
    # Get network topology between running containers
    api_response = api_instance.network_map()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->network_map: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NetworkMap**](NetworkMap.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

