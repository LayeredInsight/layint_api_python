# layint_api.ImagesApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_image_tags**](ImagesApi.md#add_image_tags) | **POST** /Scan/Images/{imageID} | Add tags to image
[**get_image_compliance**](ImagesApi.md#get_image_compliance) | **GET** /Scan/Images/{imageID}/Compliance | Get compliance report for specified image
[**get_image_licenses**](ImagesApi.md#get_image_licenses) | **GET** /Scan/Images/{imageID}/Licenses | Find software licenses for the components making up the image
[**get_image_log**](ImagesApi.md#get_image_log) | **GET** /Scan/Images/{imageID}/Logs/{logID} | Get a log for an image
[**get_image_logs**](ImagesApi.md#get_image_logs) | **GET** /Scan/Images/{imageID}/Logs | Get logs for an image
[**get_image_scan**](ImagesApi.md#get_image_scan) | **GET** /Scan/Images/{imageID}/Scans/{scanID} | Get scan data for specific scan for specified image
[**get_image_scans**](ImagesApi.md#get_image_scans) | **GET** /Scan/Images/{imageID}/Scans | Get all scan data for specified image
[**image_compliance_history_get2**](ImagesApi.md#image_compliance_history_get2) | **GET** /Scan/Images/{imageID}/ComplianceHistory | Get compliance history for specified image
[**is_image_compliant**](ImagesApi.md#is_image_compliant) | **GET** /Scan/Images/{imageID}/IsCompliant | Determines if specified image is in compliance with policies applied to image


# **add_image_tags**
> add_image_tags(image_id, tag_i_ds)

Add tags to image

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
api_instance = layint_api.ImagesApi()
image_id = 'image_id_example' # str | ImageID to tag
tag_i_ds = layint_api.TagIDs() # TagIDs | Tag IDs to be applied to image

try: 
    # Add tags to image
    api_instance.add_image_tags(image_id, tag_i_ds)
except ApiException as e:
    print("Exception when calling ImagesApi->add_image_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| ImageID to tag | 
 **tag_i_ds** | [**TagIDs**](TagIDs.md)| Tag IDs to be applied to image | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_compliance**
> Compliances get_image_compliance(image_id, run=run, policies=policies)

Get compliance report for specified image

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
api_instance = layint_api.ImagesApi()
image_id = 'image_id_example' # str | ImageID to get compliance data for
run = false # bool | If true, requests running compliance policies specified in \"policies\" parameter (optional) (default to false)
policies = 'policies_example' # str | Comma-separated list of compliance policies to run for this image (optional)

try: 
    # Get compliance report for specified image
    api_response = api_instance.get_image_compliance(image_id, run=run, policies=policies)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_compliance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| ImageID to get compliance data for | 
 **run** | **bool**| If true, requests running compliance policies specified in \&quot;policies\&quot; parameter | [optional] [default to false]
 **policies** | **str**| Comma-separated list of compliance policies to run for this image | [optional] 

### Return type

[**Compliances**](Compliances.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_licenses**
> list[InlineResponse2001] get_image_licenses(image_id)

Find software licenses for the components making up the image

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
api_instance = layint_api.ImagesApi()
image_id = 'image_id_example' # str | 

try: 
    # Find software licenses for the components making up the image
    api_response = api_instance.get_image_licenses(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_licenses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  | 

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_log**
> ImageLog get_image_log(image_id, log_id)

Get a log for an image

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
api_instance = layint_api.ImagesApi()
image_id = 'image_id_example' # str | 
log_id = 'log_id_example' # str | 

try: 
    # Get a log for an image
    api_response = api_instance.get_image_log(image_id, log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  | 
 **log_id** | **str**|  | 

### Return type

[**ImageLog**](ImageLog.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_logs**
> ImageLogs get_image_logs(image_id)

Get logs for an image

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
api_instance = layint_api.ImagesApi()
image_id = 'image_id_example' # str | 

try: 
    # Get logs for an image
    api_response = api_instance.get_image_logs(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**|  | 

### Return type

[**ImageLogs**](ImageLogs.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_scan**
> ScanData get_image_scan(image_id, scan_id)

Get scan data for specific scan for specified image

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
api_instance = layint_api.ImagesApi()
image_id = 'image_id_example' # str | ImageID to get scan data for
scan_id = 'scan_id_example' # str | ID of scan to get data for

try: 
    # Get scan data for specific scan for specified image
    api_response = api_instance.get_image_scan(image_id, scan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| ImageID to get scan data for | 
 **scan_id** | **str**| ID of scan to get data for | 

### Return type

[**ScanData**](ScanData.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_scans**
> ScanDatas get_image_scans(image_id)

Get all scan data for specified image

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
api_instance = layint_api.ImagesApi()
image_id = 'image_id_example' # str | ImageID to get scan data for

try: 
    # Get all scan data for specified image
    api_response = api_instance.get_image_scans(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_image_scans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| ImageID to get scan data for | 

### Return type

[**ScanDatas**](ScanDatas.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_compliance_history_get2**
> ComplianceHistory image_compliance_history_get2(image_id, starting_date, ending_date)

Get compliance history for specified image

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
api_instance = layint_api.ImagesApi()
image_id = 'image_id_example' # str | ImageID to get compliance data for
starting_date = 'starting_date_example' # str | Start date for period of interest
ending_date = 'ending_date_example' # str | End date for period of interest

try: 
    # Get compliance history for specified image
    api_response = api_instance.image_compliance_history_get2(image_id, starting_date, ending_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->image_compliance_history_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| ImageID to get compliance data for | 
 **starting_date** | **str**| Start date for period of interest | 
 **ending_date** | **str**| End date for period of interest | 

### Return type

[**ComplianceHistory**](ComplianceHistory.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_image_compliant**
> ComplianceResult is_image_compliant(image_id)

Determines if specified image is in compliance with policies applied to image

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
api_instance = layint_api.ImagesApi()
image_id = 'image_id_example' # str | ImageID to check compliance of

try: 
    # Determines if specified image is in compliance with policies applied to image
    api_response = api_instance.is_image_compliant(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->is_image_compliant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| ImageID to check compliance of | 

### Return type

[**ComplianceResult**](ComplianceResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

