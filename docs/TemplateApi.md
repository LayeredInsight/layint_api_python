# layint_api.TemplateApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template**](TemplateApi.md#create_template) | **POST** /Templates | Create a template
[**delete_template**](TemplateApi.md#delete_template) | **DELETE** /Templates/{TemplateId} | Delete a template
[**list_all_templates**](TemplateApi.md#list_all_templates) | **GET** /Templates | Get all templates
[**show_template_details**](TemplateApi.md#show_template_details) | **GET** /Templates/{TemplateId} | Get a template


# **create_template**
> Policy create_template(policy=policy)

Create a template

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
api_instance = layint_api.TemplateApi()
policy = layint_api.Policy() # Policy |  (optional)

try: 
    # Create a template
    api_response = api_instance.create_template(policy=policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->create_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**Policy**](Policy.md)|  | [optional] 

### Return type

[**Policy**](Policy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> delete_template(template_id)

Delete a template

### Example 
```python
from __future__ import print_function
import time
import layint_api
from layint_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = layint_api.TemplateApi()
template_id = 'template_id_example' # str | hexadecimal ID of template to delete

try: 
    # Delete a template
    api_instance.delete_template(template_id)
except ApiException as e:
    print("Exception when calling TemplateApi->delete_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| hexadecimal ID of template to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_templates**
> Policies list_all_templates()

Get all templates

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
api_instance = layint_api.TemplateApi()

try: 
    # Get all templates
    api_response = api_instance.list_all_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->list_all_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Policies**](Policies.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_template_details**
> Policy show_template_details(template_id)

Get a template

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
api_instance = layint_api.TemplateApi()
template_id = 'template_id_example' # str | hexadecimal ID of template to get

try: 
    # Get a template
    api_response = api_instance.show_template_details(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateApi->show_template_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| hexadecimal ID of template to get | 

### Return type

[**Policy**](Policy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

