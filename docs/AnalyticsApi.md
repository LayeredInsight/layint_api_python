# layint_api.AnalyticsApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cve_search**](AnalyticsApi.md#cve_search) | **POST** /Scan/CveSearch | Searches image scan results for specified CVE ID
[**get_stats**](AnalyticsApi.md#get_stats) | **GET** /Scan/Stats | Gets vulnerability statistics for user&#39;s images
[**package_search**](AnalyticsApi.md#package_search) | **POST** /Scan/PackageSearch | Searches for images with a specified software package
[**stats_history_get**](AnalyticsApi.md#stats_history_get) | **GET** /Scan/StatsHistory | Get vulnerability history over a time period
[**top_cves**](AnalyticsApi.md#top_cves) | **POST** /Scan/TopCves | Returns a list of most common/severe vulnerabilities present in a users images
[**top_vuln_images**](AnalyticsApi.md#top_vuln_images) | **POST** /Scan/TopVulnImages | Returns a list of most vulnerable images


# **cve_search**
> CveSearch cve_search(cve_search_field)

Searches image scan results for specified CVE ID

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
api_instance = layint_api.AnalyticsApi()
cve_search_field = layint_api.CveSearchField() # CveSearchField | 

try: 
    # Searches image scan results for specified CVE ID
    api_response = api_instance.cve_search(cve_search_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->cve_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_search_field** | [**CveSearchField**](CveSearchField.md)|  | 

### Return type

[**CveSearch**](CveSearch.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> VulnerabilityStats get_stats(tags=tags)

Gets vulnerability statistics for user's images

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
api_instance = layint_api.AnalyticsApi()
tags = layint_api.TagNames() # TagNames | Tag name(s) to filter results (optional)

try: 
    # Gets vulnerability statistics for user's images
    api_response = api_instance.get_stats(tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**TagNames**](TagNames.md)| Tag name(s) to filter results | [optional] 

### Return type

[**VulnerabilityStats**](VulnerabilityStats.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **package_search**
> PackageSearchResults package_search(package_search_data=package_search_data)

Searches for images with a specified software package

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
api_instance = layint_api.AnalyticsApi()
package_search_data = layint_api.PackageSearchData() # PackageSearchData |  (optional)

try: 
    # Searches for images with a specified software package
    api_response = api_instance.package_search(package_search_data=package_search_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->package_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_search_data** | [**PackageSearchData**](PackageSearchData.md)|  | [optional] 

### Return type

[**PackageSearchResults**](PackageSearchResults.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_history_get**
> StatsHistory stats_history_get(starting_date, ending_date)

Get vulnerability history over a time period

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
api_instance = layint_api.AnalyticsApi()
starting_date = 'starting_date_example' # str | Start date for period of interest
ending_date = 'ending_date_example' # str | End date for period of interest

try: 
    # Get vulnerability history over a time period
    api_response = api_instance.stats_history_get(starting_date, ending_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->stats_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starting_date** | **str**| Start date for period of interest | 
 **ending_date** | **str**| End date for period of interest | 

### Return type

[**StatsHistory**](StatsHistory.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **top_cves**
> TopCves top_cves(cve_search_data=cve_search_data)

Returns a list of most common/severe vulnerabilities present in a users images

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
api_instance = layint_api.AnalyticsApi()
cve_search_data = layint_api.CveSearchData() # CveSearchData | Number of vulnerable images to return (optional)

try: 
    # Returns a list of most common/severe vulnerabilities present in a users images
    api_response = api_instance.top_cves(cve_search_data=cve_search_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->top_cves: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_search_data** | [**CveSearchData**](CveSearchData.md)| Number of vulnerable images to return | [optional] 

### Return type

[**TopCves**](TopCves.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **top_vuln_images**
> TopVulnerableImages top_vuln_images(vulnerable_image_data=vulnerable_image_data)

Returns a list of most vulnerable images

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
api_instance = layint_api.AnalyticsApi()
vulnerable_image_data = layint_api.VulnerableImageData() # VulnerableImageData |  (optional)

try: 
    # Returns a list of most vulnerable images
    api_response = api_instance.top_vuln_images(vulnerable_image_data=vulnerable_image_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->top_vuln_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vulnerable_image_data** | [**VulnerableImageData**](VulnerableImageData.md)|  | [optional] 

### Return type

[**TopVulnerableImages**](TopVulnerableImages.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

