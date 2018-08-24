# layint_api.ComplianceApi

All URIs are relative to *http://api-stage.layeredinsight.net/v0.01*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_policy**](ComplianceApi.md#add_policy) | **POST** /Scan/Policies | Add a new policy
[**add_policy_rule**](ComplianceApi.md#add_policy_rule) | **POST** /Scan/Rules | Add a new policy rule
[**delete_policy_rule**](ComplianceApi.md#delete_policy_rule) | **DELETE** /Scan/Rules/{ruleID} | Delete compliance policy rule
[**get_policies**](ComplianceApi.md#get_policies) | **GET** /Scan/Policies | List all compliance policies available to the user
[**get_policy_rule**](ComplianceApi.md#get_policy_rule) | **GET** /Scan/Rules/{ruleID} | Get compliance policy rule
[**get_policy_rules**](ComplianceApi.md#get_policy_rules) | **GET** /Scan/Rules | List all compliance rules available to the user
[**image_compliance_history_get**](ComplianceApi.md#image_compliance_history_get) | **GET** /Scan/ComplianceHistory | Get compliance history over a time period
[**policies_delete**](ComplianceApi.md#policies_delete) | **DELETE** /Scan/Policies/{policyID} | Delete compliance policy
[**policies_get**](ComplianceApi.md#policies_get) | **GET** /Scan/Policies/{policyID} | Get compliance policy
[**policies_post**](ComplianceApi.md#policies_post) | **POST** /Scan/Policies/{policyID} | Update policy
[**update_policy_rule**](ComplianceApi.md#update_policy_rule) | **POST** /Scan/Rules/{ruleID} | Update policy rule


# **add_policy**
> ScanPolicies add_policy(policy)

Add a new policy

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
api_instance = layint_api.ComplianceApi()
policy = layint_api.ScanPolicies() # ScanPolicies | One or more policies to be added

try: 
    # Add a new policy
    api_response = api_instance.add_policy(policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->add_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**ScanPolicies**](ScanPolicies.md)| One or more policies to be added | 

### Return type

[**ScanPolicies**](ScanPolicies.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_policy_rule**
> ScanPolicyRules add_policy_rule(policy_rules)

Add a new policy rule

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
api_instance = layint_api.ComplianceApi()
policy_rules = layint_api.ScanPolicyRules() # ScanPolicyRules | One or more policy rules to be added

try: 
    # Add a new policy rule
    api_response = api_instance.add_policy_rule(policy_rules)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->add_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_rules** | [**ScanPolicyRules**](ScanPolicyRules.md)| One or more policy rules to be added | 

### Return type

[**ScanPolicyRules**](ScanPolicyRules.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_rule**
> delete_policy_rule(rule_id)

Delete compliance policy rule

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
api_instance = layint_api.ComplianceApi()
rule_id = 'rule_id_example' # str | ID of policy rule to delete

try: 
    # Delete compliance policy rule
    api_instance.delete_policy_rule(rule_id)
except ApiException as e:
    print("Exception when calling ComplianceApi->delete_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| ID of policy rule to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies**
> ScanPolicies get_policies()

List all compliance policies available to the user

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
api_instance = layint_api.ComplianceApi()

try: 
    # List all compliance policies available to the user
    api_response = api_instance.get_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->get_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ScanPolicies**](ScanPolicies.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_rule**
> ScanPolicyRule get_policy_rule(rule_id)

Get compliance policy rule

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
api_instance = layint_api.ComplianceApi()
rule_id = 'rule_id_example' # str | ID of policy rule to get

try: 
    # Get compliance policy rule
    api_response = api_instance.get_policy_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->get_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| ID of policy rule to get | 

### Return type

[**ScanPolicyRule**](ScanPolicyRule.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_rules**
> ScanPolicyRules get_policy_rules()

List all compliance rules available to the user

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
api_instance = layint_api.ComplianceApi()

try: 
    # List all compliance rules available to the user
    api_response = api_instance.get_policy_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->get_policy_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ScanPolicyRules**](ScanPolicyRules.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_compliance_history_get**
> ComplianceHistory image_compliance_history_get(starting_date, ending_date)

Get compliance history over a time period

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
api_instance = layint_api.ComplianceApi()
starting_date = 'starting_date_example' # str | Start date for period of interest
ending_date = 'ending_date_example' # str | End date for period of interest

try: 
    # Get compliance history over a time period
    api_response = api_instance.image_compliance_history_get(starting_date, ending_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->image_compliance_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starting_date** | **str**| Start date for period of interest | 
 **ending_date** | **str**| End date for period of interest | 

### Return type

[**ComplianceHistory**](ComplianceHistory.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_delete**
> policies_delete(policy_id)

Delete compliance policy

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
api_instance = layint_api.ComplianceApi()
policy_id = 'policy_id_example' # str | ID of policy to delete

try: 
    # Delete compliance policy
    api_instance.policies_delete(policy_id)
except ApiException as e:
    print("Exception when calling ComplianceApi->policies_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| ID of policy to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_get**
> ScanPolicy policies_get(policy_id)

Get compliance policy

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
api_instance = layint_api.ComplianceApi()
policy_id = 'policy_id_example' # str | ID of policy to get

try: 
    # Get compliance policy
    api_response = api_instance.policies_get(policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->policies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| ID of policy to get | 

### Return type

[**ScanPolicy**](ScanPolicy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_post**
> ScanPolicy policies_post(policy_id, policy)

Update policy

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
api_instance = layint_api.ComplianceApi()
policy_id = 'policy_id_example' # str | ID of policy to get
policy = layint_api.ScanPolicy() # ScanPolicy | Data to update policy with

try: 
    # Update policy
    api_response = api_instance.policies_post(policy_id, policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->policies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**| ID of policy to get | 
 **policy** | [**ScanPolicy**](ScanPolicy.md)| Data to update policy with | 

### Return type

[**ScanPolicy**](ScanPolicy.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_rule**
> ScanPolicyRule update_policy_rule(rule_id, policy_rule)

Update policy rule

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
api_instance = layint_api.ComplianceApi()
rule_id = 'rule_id_example' # str | ID of policy rule to update
policy_rule = layint_api.ScanPolicyRule() # ScanPolicyRule | Data to update policy rule with

try: 
    # Update policy rule
    api_response = api_instance.update_policy_rule(rule_id, policy_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplianceApi->update_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| ID of policy rule to update | 
 **policy_rule** | [**ScanPolicyRule**](ScanPolicyRule.md)| Data to update policy rule with | 

### Return type

[**ScanPolicyRule**](ScanPolicyRule.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

