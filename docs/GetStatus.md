# GetStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battery_percentage** | **float** | The current charge percentage of the battery | [optional] 
**battery_time_remaining** | **int** | The approximate time remaining on the battery during normal operation of the robot | [optional] 
**distance_to_next_target** | **float** | The distance to the next target of the robot | [optional] 
**errors** | [**list[Errors]**](Errors.md) | The list of actions executed as part of the mission | [optional] 
**footprint** | **str** | The current footprint of the robot | [optional] 
**hook_status** | [**HookStatus**](HookStatus.md) |  | [optional] 
**joystick_low_speed_mode_enabled** | **bool** |  | [optional] 
**joystick_web_session_id** | **str** | The id of the web user that has control over the joystick | [optional] 
**map_id** | **str** | The id of the current map the robot recides in | [optional] 
**mission_queue_id** | **int** | The id of the current job the robot executes | [optional] 
**mission_queue_url** | **str** | The url to the active mission in queue | [optional] 
**mission_text** | **str** | Status message from mission controller | [optional] 
**mode_id** | **int** | The id of the current mode of the robot | [optional] 
**mode_key_state** | **str** | A textual description of the position of the mode key | [optional] 
**mode_text** | **str** | A textual description of the current state of the robot | [optional] 
**moved** | **float** |  | [optional] 
**position** | [**Position**](Position.md) |  | [optional] 
**robot_model** | **str** | The model of the robot | [optional] 
**robot_name** | **str** | The name of the robot | [optional] 
**safety_system_muted** | **bool** |  | [optional] 
**serial_number** | **str** | The model of the robot | [optional] 
**session_id** | **str** | The id of the session the robot recides in | [optional] 
**state_id** | **int** | The id of the current state of the robot | [optional] 
**state_text** | **str** | A textual description of the current state of the robot | [optional] 
**unloaded_map_changes** | **bool** |  | [optional] 
**uptime** | **int** | The uptime of the robot | [optional] 
**user_prompt** | [**UserPrompt**](UserPrompt.md) |  | [optional] 
**velocity** | [**Velocity**](Velocity.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

