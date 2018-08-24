# layint_api.LicenseApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**license_get**](LicenseApi.md#license_get) | **GET** /License | Get application license information
[**update_license**](LicenseApi.md#update_license) | **POST** /License | Add or update application license


# **license_get**
> License license_get()

Get application license information

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
api_instance = layint_api.LicenseApi()

try: 
    # Get application license information
    api_response = api_instance.license_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->license_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**License**](License.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_license**
> License update_license(license_request)

Add or update application license

Add or update license

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
api_instance = layint_api.LicenseApi()
license_request = layint_api.LicenseRequest() # LicenseRequest | 

try: 
    # Add or update application license
    api_response = api_instance.update_license(license_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->update_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_request** | [**LicenseRequest**](LicenseRequest.md)|  | 

### Return type

[**License**](License.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

