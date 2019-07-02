# GetMissionQueue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **str** | The list of parameters this mission queue entry accepts | [optional] 
**control_posid** | **str** | Global id of position used during control states | [optional] 
**control_state** | **int** | Mission control state. a value above zero indicates that the robot needs an external input in order to continue | [optional] 
**created_by** | **str** | The url to the description of the type of this element | [optional] 
**created_by_id** | **str** | The global id of the user who created this entry | [optional] 
**description** | **str** | Inerited from mission description, when item was queued | [optional] 
**finished** | **datetime** | The date and time when the mission was finished | [optional] 
**id** | **int** | The id of the mission queue entry | [optional] 
**message** | **str** | The last message produced by the actions in the mission list | [optional] 
**mission** | **str** | The url to the mission that mission that was executed | [optional] 
**mission_id** | **str** | The global id of the mission that was executed | [optional] 
**ordered** | **datetime** | The date end time when the mission was queued | [optional] 
**parameters** | **str** |  | [optional] 
**priority** | **int** | The id of the action | [optional] 
**started** | **datetime** | The date and time when the missin was started | [optional] 
**state** | **str** | The end state after the mission was executed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

