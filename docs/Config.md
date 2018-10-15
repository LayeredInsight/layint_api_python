# Config

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 12 character internal hexadecimal identifier for this Configuration | [optional] 
**name** | **str** | Name of the configuration | [optional] 
**user_id** | **str** | User ID of owner of the container | [optional] 
**group_id** | **str** | Group ID of owner of the container | [optional] 
**mq** | **str** | Connection string for RabbitMQ system the instrumented container should connect to. Both AMQP and AMQPS are supported. | [optional] 
**policy_id** | **str** | 12 character hexadecimal internal identifier for security policy for this Container | [optional] 
**log_mode** | **int** | Specifies the mode for LI agent(s) to send logs. An integer in decimal representation containing LogMode bit flags to control generated agent configuration.  | Log Mode        | Value | Value Hexadecimal | |-----------------|-------|-------------------| | None            | 0     | 0x0| | PolicyAlert     | 1     | 0x1| | PolicyDeny      | 2     | 0x2| | PolicyAlertDeny | 3     | 0x3 (PolicyAlert \\| PolicyDeny)| | PolicyAllow     | 4     | 0x4| | PolicyAll       | 7     | 0x7 (PolicyAlert \\| PolicyDeny \\| PolicyAllow)| | Behavior        | 8     | 0x8   | | All             | 15    | 0xf (PolicyAll \\| Behavior)|  | [optional] 
**sniffing** | **bool** | When true, enables basic network monitoring for malicious activity and network behavior recording. | [optional] [default to False]
**date_created** | **str** | Timestamp for when object was created | [optional] 
**date_updated** | **str** | Timestamp for when object was last updated | [optional] 
**default** | **bool** | Default configuration for group | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


