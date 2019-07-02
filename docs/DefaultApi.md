# mir100_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actions_action_type_get**](DefaultApi.md#actions_action_type_get) | **GET** /actions/{action_type} | Retrieve the details about the action. It displays the parameters of the action and the limits for the values among others
[**actions_action_type_post**](DefaultApi.md#actions_action_type_post) | **POST** /actions/{action_type} | Add a new action definition with the specified action_type
[**actions_get**](DefaultApi.md#actions_get) | **GET** /actions | Retrieve the list of action definitions
[**area_events_action_definitions_action_type_get**](DefaultApi.md#area_events_action_definitions_action_type_get) | **GET** /area_events/action_definitions/{action_type} | Retrieve the details about the action. It displays the parameters of the action and the limits for the values among others
[**area_events_action_definitions_get**](DefaultApi.md#area_events_action_definitions_get) | **GET** /area_events/action_definitions | Retrieve definitions of area actions and their parameters
[**area_events_definitions_get**](DefaultApi.md#area_events_definitions_get) | **GET** /area_events/definitions | Retrieve definitions of areas and their actions
[**area_events_get**](DefaultApi.md#area_events_get) | **GET** /area_events | Retrieve the list of area events
[**area_events_guid_delete**](DefaultApi.md#area_events_guid_delete) | **DELETE** /area_events/{guid} | Erase the area event with the specified GUID
[**area_events_guid_get**](DefaultApi.md#area_events_guid_get) | **GET** /area_events/{guid} | Retrieve the details about the area event with the specified GUID
[**area_events_guid_put**](DefaultApi.md#area_events_guid_put) | **PUT** /area_events/{guid} | Modify the values of the area event with the specified GUID
[**area_events_post**](DefaultApi.md#area_events_post) | **POST** /area_events | Add a new area event
[**bluetooth_delete**](DefaultApi.md#bluetooth_delete) | **DELETE** /bluetooth | Disconnect the Bluetooth device
[**bluetooth_get**](DefaultApi.md#bluetooth_get) | **GET** /bluetooth | Retrieve the status of the Bluetooth connection
[**bluetooth_post**](DefaultApi.md#bluetooth_post) | **POST** /bluetooth | Connect to the Bluetooth device with the given GUID
[**bluetooth_put**](DefaultApi.md#bluetooth_put) | **PUT** /bluetooth | Modify the outputs of the connected Bluetooth device
[**bluetooth_relays_get**](DefaultApi.md#bluetooth_relays_get) | **GET** /bluetooth_relays | Retrieve the list of configured Bluetooth devices
[**bluetooth_relays_guid_delete**](DefaultApi.md#bluetooth_relays_guid_delete) | **DELETE** /bluetooth_relays/{guid} | Erase the Bluetooth device with the specified GUID
[**bluetooth_relays_guid_get**](DefaultApi.md#bluetooth_relays_guid_get) | **GET** /bluetooth_relays/{guid} | Retrieve the details about the Bluetooth device with the specified GUID
[**bluetooth_relays_guid_put**](DefaultApi.md#bluetooth_relays_guid_put) | **PUT** /bluetooth_relays/{guid} | Modify the values of the Bluetooth device with the specified GUID
[**bluetooth_relays_post**](DefaultApi.md#bluetooth_relays_post) | **POST** /bluetooth_relays | Add a new Bluetooth device
[**bluetooth_scan_get**](DefaultApi.md#bluetooth_scan_get) | **GET** /bluetooth/scan | Start the discovery of Bluetooth devices
[**bluetooth_scan_post**](DefaultApi.md#bluetooth_scan_post) | **POST** /bluetooth/scan | Retrieve the list of discovered devices
[**cart_calibrations_get**](DefaultApi.md#cart_calibrations_get) | **GET** /cart_calibrations | Retrieve the list of cart calibrations
[**cart_calibrations_guid_delete**](DefaultApi.md#cart_calibrations_guid_delete) | **DELETE** /cart_calibrations/{guid} | Erase the cart calibration with the specified GUID
[**cart_calibrations_guid_get**](DefaultApi.md#cart_calibrations_guid_get) | **GET** /cart_calibrations/{guid} | Retrieve the details about the cart calibration with the specified GUID
[**cart_calibrations_guid_put**](DefaultApi.md#cart_calibrations_guid_put) | **PUT** /cart_calibrations/{guid} | Modify the values of the cart calibration with the specified GUID
[**cart_calibrations_post**](DefaultApi.md#cart_calibrations_post) | **POST** /cart_calibrations | Add a new cart calibration
[**cart_types_get**](DefaultApi.md#cart_types_get) | **GET** /cart_types | Retrieve the list of cart types
[**cart_types_guid_delete**](DefaultApi.md#cart_types_guid_delete) | **DELETE** /cart_types/{guid} | Erase the cart type with the specified GUID
[**cart_types_guid_get**](DefaultApi.md#cart_types_guid_get) | **GET** /cart_types/{guid} | Retrieve the details about the cart type with the specified GUID
[**cart_types_guid_put**](DefaultApi.md#cart_types_guid_put) | **PUT** /cart_types/{guid} | Modify the values of the cart type with the specified GUID
[**cart_types_post**](DefaultApi.md#cart_types_post) | **POST** /cart_types | Add a new cart type
[**carts_get**](DefaultApi.md#carts_get) | **GET** /carts | Retrieve the list of carts
[**carts_guid_delete**](DefaultApi.md#carts_guid_delete) | **DELETE** /carts/{guid} | Erase the cart with the specified GUID
[**carts_guid_get**](DefaultApi.md#carts_guid_get) | **GET** /carts/{guid} | Retrieve the details about the cart with the specified GUID
[**carts_guid_put**](DefaultApi.md#carts_guid_put) | **PUT** /carts/{guid} | Modify the values of the cart with the specified GUID
[**carts_post**](DefaultApi.md#carts_post) | **POST** /carts | Add a new cart
[**changes_me_delete**](DefaultApi.md#changes_me_delete) | **DELETE** /changes/me | Deletes all data owned by the current user or users with lower authority
[**changes_me_get**](DefaultApi.md#changes_me_get) | **GET** /changes/me | Makes a list of all data owned by the current user or users with lower authority
[**dashboards_dashboard_id_widgets_get**](DefaultApi.md#dashboards_dashboard_id_widgets_get) | **GET** /dashboards/{dashboard_id}/widgets | Retrieve the list of widgets of the dashboard with the specified dashboard ID
[**dashboards_dashboard_id_widgets_guid_delete**](DefaultApi.md#dashboards_dashboard_id_widgets_guid_delete) | **DELETE** /dashboards/{dashboard_id}/widgets/{guid} | Erase the widget with the specified GUID from the dashboard with the specified dashboard ID
[**dashboards_dashboard_id_widgets_guid_get**](DefaultApi.md#dashboards_dashboard_id_widgets_guid_get) | **GET** /dashboards/{dashboard_id}/widgets/{guid} | Retrieve the details about the widget with the specified GUID in the dashboard with the specified dashboard ID
[**dashboards_dashboard_id_widgets_guid_put**](DefaultApi.md#dashboards_dashboard_id_widgets_guid_put) | **PUT** /dashboards/{dashboard_id}/widgets/{guid} | Modify the values of the widget with the specified GUID in the dashboard with the specified dashboard ID
[**dashboards_dashboard_id_widgets_post**](DefaultApi.md#dashboards_dashboard_id_widgets_post) | **POST** /dashboards/{dashboard_id}/widgets | Add a new widget to the dashboard with the specified dashboard ID
[**dashboards_get**](DefaultApi.md#dashboards_get) | **GET** /dashboards | Retrieve the list of dashboards
[**dashboards_guid_delete**](DefaultApi.md#dashboards_guid_delete) | **DELETE** /dashboards/{guid} | Erase the dashboard with the specified GUID
[**dashboards_guid_get**](DefaultApi.md#dashboards_guid_get) | **GET** /dashboards/{guid} | Retrieve the details of the dashboard with the specified GUID
[**dashboards_guid_put**](DefaultApi.md#dashboards_guid_put) | **PUT** /dashboards/{guid} | Modify the values of the dashboard with the specified GUID
[**dashboards_post**](DefaultApi.md#dashboards_post) | **POST** /dashboards | Add a new dashboard
[**docking_offsets_get**](DefaultApi.md#docking_offsets_get) | **GET** /docking_offsets | Retrieve the list of docking offsets
[**docking_offsets_guid_delete**](DefaultApi.md#docking_offsets_guid_delete) | **DELETE** /docking_offsets/{guid} | Erase the docking offset with the specified GUID
[**docking_offsets_guid_get**](DefaultApi.md#docking_offsets_guid_get) | **GET** /docking_offsets/{guid} | Retrieve the details of the docking offset with the specified GUID
[**docking_offsets_guid_put**](DefaultApi.md#docking_offsets_guid_put) | **PUT** /docking_offsets/{guid} | Modify the values of the docking offset with the specified GUID
[**docking_offsets_post**](DefaultApi.md#docking_offsets_post) | **POST** /docking_offsets | Add a new docking offset. The only positions that can have docking offsets are Charging stations, V markers and VL markers
[**factory_reset_post**](DefaultApi.md#factory_reset_post) | **POST** /factory_reset | Clean and migrate the database. Keep hardware configurations
[**hook_brake_get**](DefaultApi.md#hook_brake_get) | **GET** /hook/brake | Retrieve the state of the Hook brake
[**hook_brake_put**](DefaultApi.md#hook_brake_put) | **PUT** /hook/brake | Activate or release the Hook brake
[**hook_gripper_get**](DefaultApi.md#hook_gripper_get) | **GET** /hook/gripper | Retrieve the state of the Hook gripper
[**hook_gripper_put**](DefaultApi.md#hook_gripper_put) | **PUT** /hook/gripper | Open or close the Hook gripper
[**hook_height_get**](DefaultApi.md#hook_height_get) | **GET** /hook/height | Retrieve the height of the Hook
[**hook_height_put**](DefaultApi.md#hook_height_put) | **PUT** /hook/height | Modify the height of the Hook
[**hook_status_get**](DefaultApi.md#hook_status_get) | **GET** /hook/status | Retrieve the extended status of the Hook
[**hw_export_get**](DefaultApi.md#hw_export_get) | **GET** /hw/export | Download a file containing the hardware configuration of the robot
[**hw_import_post**](DefaultApi.md#hw_import_post) | **POST** /hw/import | Import the hardware configuration contained in the file into the robot
[**io_modules_get**](DefaultApi.md#io_modules_get) | **GET** /io_modules | Retrieve the list of configured IO modules
[**io_modules_guid_delete**](DefaultApi.md#io_modules_guid_delete) | **DELETE** /io_modules/{guid} | Erase the IO device with the specified GUID
[**io_modules_guid_get**](DefaultApi.md#io_modules_guid_get) | **GET** /io_modules/{guid} | Retrieve the details about a IO device with the specified GUID
[**io_modules_guid_put**](DefaultApi.md#io_modules_guid_put) | **PUT** /io_modules/{guid} | Modify the values of the IO device with the specified GUID
[**io_modules_guid_status_delete**](DefaultApi.md#io_modules_guid_status_delete) | **DELETE** /io_modules/{guid}/status | Disconnect from the IO module with the specified GUID
[**io_modules_guid_status_get**](DefaultApi.md#io_modules_guid_status_get) | **GET** /io_modules/{guid}/status | Retrieve the status of the connection to the IO module with the specified GUID
[**io_modules_guid_status_post**](DefaultApi.md#io_modules_guid_status_post) | **POST** /io_modules/{guid}/status | Connect to theIO module with the specified GUID
[**io_modules_guid_status_put**](DefaultApi.md#io_modules_guid_status_put) | **PUT** /io_modules/{guid}/status | Modify the outputs of the connected IO module with specified GUID
[**io_modules_post**](DefaultApi.md#io_modules_post) | **POST** /io_modules | Add a new IO module
[**log_error_reports_delete**](DefaultApi.md#log_error_reports_delete) | **DELETE** /log/error_reports | Erase ALL the error reports
[**log_error_reports_get**](DefaultApi.md#log_error_reports_get) | **GET** /log/error_reports | Retrieve the list of error reports
[**log_error_reports_id_delete**](DefaultApi.md#log_error_reports_id_delete) | **DELETE** /log/error_reports/{id} | Erase the error report with the specified ID
[**log_error_reports_id_download_get**](DefaultApi.md#log_error_reports_id_download_get) | **GET** /log/error_reports/{id}/download | Download the file containing the error report with the specified ID
[**log_error_reports_id_get**](DefaultApi.md#log_error_reports_id_get) | **GET** /log/error_reports/{id} | Retrieve the details about the error report with the specified ID
[**log_error_reports_post**](DefaultApi.md#log_error_reports_post) | **POST** /log/error_reports | Generate a new error report. This will record the 30s previous to this call in a file.
[**maps_get**](DefaultApi.md#maps_get) | **GET** /maps | Retrieve the list of maps
[**maps_guid_delete**](DefaultApi.md#maps_guid_delete) | **DELETE** /maps/{guid} | Erase the map with the specified GUID
[**maps_guid_get**](DefaultApi.md#maps_guid_get) | **GET** /maps/{guid} | Retrieve the details about the map with the specified GUID
[**maps_guid_put**](DefaultApi.md#maps_guid_put) | **PUT** /maps/{guid} | Modify the values of the map with the specified GUID
[**maps_map_id_area_events_get**](DefaultApi.md#maps_map_id_area_events_get) | **GET** /maps/{map_id}/area_events | Retrieve the list of area events that belong to the map with the specified map ID
[**maps_map_id_path_guides_get**](DefaultApi.md#maps_map_id_path_guides_get) | **GET** /maps/{map_id}/path_guides | Retrieve the list of path guides that belong to the map with the specified map ID
[**maps_map_id_paths_get**](DefaultApi.md#maps_map_id_paths_get) | **GET** /maps/{map_id}/paths | Retrieve the list of paths that belong to the map with the specified map ID
[**maps_map_id_positions_get**](DefaultApi.md#maps_map_id_positions_get) | **GET** /maps/{map_id}/positions | Retrieve the list of positions that belong to the map with the specified map ID
[**maps_post**](DefaultApi.md#maps_post) | **POST** /maps | Add a new map
[**mission_groups_get**](DefaultApi.md#mission_groups_get) | **GET** /mission_groups | Retrieve the list of mission groups
[**mission_groups_group_id_missions_get**](DefaultApi.md#mission_groups_group_id_missions_get) | **GET** /mission_groups/{group_id}/missions | Retrieve the list of missions that belong to the group with the specified group ID
[**mission_groups_guid_delete**](DefaultApi.md#mission_groups_guid_delete) | **DELETE** /mission_groups/{guid} | Erase the mission group with the specified GUID
[**mission_groups_guid_get**](DefaultApi.md#mission_groups_guid_get) | **GET** /mission_groups/{guid} | Retrieve the details about the mission group with the specified GUID
[**mission_groups_guid_put**](DefaultApi.md#mission_groups_guid_put) | **PUT** /mission_groups/{guid} | Modify the values of the mission group with the specified GUID
[**mission_groups_mission_group_id_actions_get**](DefaultApi.md#mission_groups_mission_group_id_actions_get) | **GET** /mission_groups/{mission_group_id}/actions | Retrieve the list of action definitions from the mission group with the specified mission group ID
[**mission_groups_post**](DefaultApi.md#mission_groups_post) | **POST** /mission_groups | Add a new mission group
[**mission_queue_delete**](DefaultApi.md#mission_queue_delete) | **DELETE** /mission_queue | Abort all the pending and executing missions from the mission queue
[**mission_queue_get**](DefaultApi.md#mission_queue_get) | **GET** /mission_queue | Retrieve the list of missions in the queue. Finished, failed, pending and executing missions will be displayed here
[**mission_queue_id_delete**](DefaultApi.md#mission_queue_id_delete) | **DELETE** /mission_queue/{id} | Abort the mission with the specified ID in the mission queue
[**mission_queue_id_get**](DefaultApi.md#mission_queue_id_get) | **GET** /mission_queue/{id} | Retrieve the details about the mission with the specified ID in the mission queue
[**mission_queue_id_put**](DefaultApi.md#mission_queue_id_put) | **PUT** /mission_queue/{id} | Modify the values of the mission with the specified ID in the mission queue
[**mission_queue_mission_queue_id_actions_get**](DefaultApi.md#mission_queue_mission_queue_id_actions_get) | **GET** /mission_queue/{mission_queue_id}/actions | Retrieve the list of actions from the mission with the specified ID in the mission queue
[**mission_queue_mission_queue_id_actions_id_get**](DefaultApi.md#mission_queue_mission_queue_id_actions_id_get) | **GET** /mission_queue/{mission_queue_id}/actions/{id} | Retrieve the details about the action with the specified ID from the mission with the specified ID in the mission queue
[**mission_queue_post**](DefaultApi.md#mission_queue_post) | **POST** /mission_queue | Add a new mission to the mission queue. The mission will always go to the end of the queue
[**missions_get**](DefaultApi.md#missions_get) | **GET** /missions | Retrieve the list of missions
[**missions_guid_definition_get**](DefaultApi.md#missions_guid_definition_get) | **GET** /missions/{guid}/definition | Retrieve the mission with the specified GUID as an action definition that can be inserted in another mission
[**missions_guid_delete**](DefaultApi.md#missions_guid_delete) | **DELETE** /missions/{guid} | Erase the mission with the specified GUID
[**missions_guid_get**](DefaultApi.md#missions_guid_get) | **GET** /missions/{guid} | Retrieve the details about the mission with the specified GUID
[**missions_guid_put**](DefaultApi.md#missions_guid_put) | **PUT** /missions/{guid} | Modify the values of the mission with the specified GUID
[**missions_mission_id_actions_get**](DefaultApi.md#missions_mission_id_actions_get) | **GET** /missions/{mission_id}/actions | Retrieve the list of actions that belong to the mission with the specified mission ID
[**missions_mission_id_actions_guid_delete**](DefaultApi.md#missions_mission_id_actions_guid_delete) | **DELETE** /missions/{mission_id}/actions/{guid} | Erase the action with the specified GUID from the mission with the specified mission ID
[**missions_mission_id_actions_guid_get**](DefaultApi.md#missions_mission_id_actions_guid_get) | **GET** /missions/{mission_id}/actions/{guid} | Retrieve the details about the action with the specified GUID that belongs to the mission with the specified mission ID
[**missions_mission_id_actions_guid_put**](DefaultApi.md#missions_mission_id_actions_guid_put) | **PUT** /missions/{mission_id}/actions/{guid} | Modify the values of the action with the specified GUID that belongs to the mission with the specified mission ID
[**missions_mission_id_actions_post**](DefaultApi.md#missions_mission_id_actions_post) | **POST** /missions/{mission_id}/actions | Add a new action to the mission with the specified mission ID
[**missions_post**](DefaultApi.md#missions_post) | **POST** /missions | Add a new mission
[**modbus_get**](DefaultApi.md#modbus_get) | **GET** /modbus | Retrieve the modbus registers linked to actions
[**modbus_id_get**](DefaultApi.md#modbus_id_get) | **GET** /modbus/{id} | Retrieve the modbus registers linked to an action
[**modbus_missions_get**](DefaultApi.md#modbus_missions_get) | **GET** /modbus/missions | Retrieve the list of coils that can trigger a mission
[**modbus_missions_guid_delete**](DefaultApi.md#modbus_missions_guid_delete) | **DELETE** /modbus/missions/{guid} | Delete the specified ID on the the modbus mission table
[**modbus_missions_guid_get**](DefaultApi.md#modbus_missions_guid_get) | **GET** /modbus/missions/{guid} | Retrieve the details about the mission linked with the coil
[**modbus_missions_guid_put**](DefaultApi.md#modbus_missions_guid_put) | **PUT** /modbus/missions/{guid} | Modify the values of the modbus mission with the specified ID
[**modbus_missions_post**](DefaultApi.md#modbus_missions_post) | **POST** /modbus/missions | Create a new link between a coil and a mission
[**path_guides_get**](DefaultApi.md#path_guides_get) | **GET** /path_guides | Retrieve the list of path guides
[**path_guides_guid_delete**](DefaultApi.md#path_guides_guid_delete) | **DELETE** /path_guides/{guid} | Erase the path guide with the specified GUID
[**path_guides_guid_get**](DefaultApi.md#path_guides_guid_get) | **GET** /path_guides/{guid} | Retrieve the path guide with the specified GUID
[**path_guides_guid_put**](DefaultApi.md#path_guides_guid_put) | **PUT** /path_guides/{guid} | Modify the values of the path guide with the specified GUID
[**path_guides_path_guide_guid_options_get**](DefaultApi.md#path_guides_path_guide_guid_options_get) | **GET** /path_guides/{path_guide_guid}/options | Retrieve the list of allowed start/via/goal options for the selected path guide
[**path_guides_path_guide_guid_positions_get**](DefaultApi.md#path_guides_path_guide_guid_positions_get) | **GET** /path_guides/{path_guide_guid}/positions | Retrieve the list of positions for the path guide with the specified GUID
[**path_guides_path_guide_guid_positions_guid_delete**](DefaultApi.md#path_guides_path_guide_guid_positions_guid_delete) | **DELETE** /path_guides/{path_guide_guid}/positions/{guid} | Erase the position with the specified GUID from the path guide with the specified path guide GUID
[**path_guides_path_guide_guid_positions_guid_get**](DefaultApi.md#path_guides_path_guide_guid_positions_guid_get) | **GET** /path_guides/{path_guide_guid}/positions/{guid} | Retrieve the position with the specified GUID from the path guide with the specified path guide GUID
[**path_guides_path_guide_guid_positions_guid_put**](DefaultApi.md#path_guides_path_guide_guid_positions_guid_put) | **PUT** /path_guides/{path_guide_guid}/positions/{guid} | Modify the values of the position with the specified GUID from the path guide with the specified path guide GUID
[**path_guides_path_guide_guid_positions_post**](DefaultApi.md#path_guides_path_guide_guid_positions_post) | **POST** /path_guides/{path_guide_guid}/positions | Add a new position to the path guide with the specified GUID
[**path_guides_positions_get**](DefaultApi.md#path_guides_positions_get) | **GET** /path_guides_positions | Retrieve the list of positions used for path guides
[**path_guides_positions_guid_delete**](DefaultApi.md#path_guides_positions_guid_delete) | **DELETE** /path_guides_positions/{guid} | Erase the path guide position with the specified GUID
[**path_guides_positions_guid_get**](DefaultApi.md#path_guides_positions_guid_get) | **GET** /path_guides_positions/{guid} | Retrieve the position for path guides with the specified GUID
[**path_guides_positions_guid_put**](DefaultApi.md#path_guides_positions_guid_put) | **PUT** /path_guides_positions/{guid} | Modify the values of the position for path guides with the specified GUID
[**path_guides_positions_post**](DefaultApi.md#path_guides_positions_post) | **POST** /path_guides_positions | Add a new position in a path guide
[**path_guides_post**](DefaultApi.md#path_guides_post) | **POST** /path_guides | Add a new path guide
[**path_guides_precalc_get**](DefaultApi.md#path_guides_precalc_get) | **GET** /path_guides_precalc | Retrieve the status of path guides precalculation
[**path_guides_precalc_post**](DefaultApi.md#path_guides_precalc_post) | **POST** /path_guides_precalc | Start/stop precalculation of the specified path guide
[**paths_get**](DefaultApi.md#paths_get) | **GET** /paths | Retrieve the list of paths
[**paths_guid_delete**](DefaultApi.md#paths_guid_delete) | **DELETE** /paths/{guid} | Erase the path with the specified GUID
[**paths_guid_get**](DefaultApi.md#paths_guid_get) | **GET** /paths/{guid} | Retrieve the path with the specified GUID
[**paths_guid_put**](DefaultApi.md#paths_guid_put) | **PUT** /paths/{guid} | Modify the values of the path with the specified GUID
[**paths_post**](DefaultApi.md#paths_post) | **POST** /paths | Add a new path
[**permissions_guid_delete**](DefaultApi.md#permissions_guid_delete) | **DELETE** /permissions/{guid} | Erase the permission with the specified GUID
[**permissions_guid_get**](DefaultApi.md#permissions_guid_get) | **GET** /permissions/{guid} | Retrieve the details about the permission with the specified GUID
[**permissions_guid_put**](DefaultApi.md#permissions_guid_put) | **PUT** /permissions/{guid} | Modify the values of the permission with the specified GUID
[**position_transition_lists_get**](DefaultApi.md#position_transition_lists_get) | **GET** /position_transition_lists | Retrieve the list of position transition lists
[**position_transition_lists_guid_delete**](DefaultApi.md#position_transition_lists_guid_delete) | **DELETE** /position_transition_lists/{guid} | Erase the position transition list with the specified GUID
[**position_transition_lists_guid_get**](DefaultApi.md#position_transition_lists_guid_get) | **GET** /position_transition_lists/{guid} | Retrieve the details about the position transition list with the specified GUID
[**position_transition_lists_guid_put**](DefaultApi.md#position_transition_lists_guid_put) | **PUT** /position_transition_lists/{guid} | Modify the values of the position transition list with the specified GUID
[**position_transition_lists_post**](DefaultApi.md#position_transition_lists_post) | **POST** /position_transition_lists | Add a new position transition list
[**position_types_get**](DefaultApi.md#position_types_get) | **GET** /position_types | Retrieve a list of possible position types
[**position_types_id_get**](DefaultApi.md#position_types_id_get) | **GET** /position_types/{id} | Retrieve the details about the position type with the specified ID
[**positions_get**](DefaultApi.md#positions_get) | **GET** /positions | Retrieve the list of positions
[**positions_guid_delete**](DefaultApi.md#positions_guid_delete) | **DELETE** /positions/{guid} | Erase the position with the specified GUID
[**positions_guid_get**](DefaultApi.md#positions_guid_get) | **GET** /positions/{guid} | Retrieve the details about the position with the specified GUID
[**positions_guid_put**](DefaultApi.md#positions_guid_put) | **PUT** /positions/{guid} | Modify the values of the position with the specified GUID
[**positions_parent_guid_helper_positions_get**](DefaultApi.md#positions_parent_guid_helper_positions_get) | **GET** /positions/{parent_guid}/helper_positions | Retrieve the list of helper positions for the position with the specified parent GUID. Only Charging Stations, V markers, VL markers, Shelf and Trolley positions have helper positions
[**positions_pos_id_docking_offsets_get**](DefaultApi.md#positions_pos_id_docking_offsets_get) | **GET** /positions/{pos_id}/docking_offsets | Retrieve the details of the docking offset of the position with the specified position ID
[**positions_post**](DefaultApi.md#positions_post) | **POST** /positions | Add a new position
[**registers_get**](DefaultApi.md#registers_get) | **GET** /registers | Retrieve the list of PLC registers from the robot. Registers 1 to 100 are integers and registers 101-200 are float
[**registers_id_get**](DefaultApi.md#registers_id_get) | **GET** /registers/{id} | Retrieve the value of the PLC register with the specified ID. Registers 1 to 100 are integers and registers 101-200 are float
[**registers_id_post**](DefaultApi.md#registers_id_post) | **POST** /registers/{id} | Modify the value of the PLC register with the specified ID. Registers 1 to 100 are integers and registers 101-200 are float. Even though this is not a standard use of the POST call it has been included for compatibility purposes
[**registers_id_put**](DefaultApi.md#registers_id_put) | **PUT** /registers/{id} | Modify the value of the PLC register with the specified ID
[**remote_support_get**](DefaultApi.md#remote_support_get) | **GET** /remote_support | Retrieve the status of the remote support connection
[**remote_support_log_get**](DefaultApi.md#remote_support_log_get) | **GET** /remote_support/log | Retrieve the list with the actions performed by the remote support controller
[**remote_support_put**](DefaultApi.md#remote_support_put) | **PUT** /remote_support | Modify the remote support connection timeout
[**robots_post**](DefaultApi.md#robots_post) | **POST** /robots | Add information about other robots in the world. This is used by the Fleet manager to avoid robot collisions
[**service_book_get**](DefaultApi.md#service_book_get) | **GET** /service_book | Retrieve service book entries accessible by user
[**service_book_guid_delete**](DefaultApi.md#service_book_guid_delete) | **DELETE** /service_book/{guid} | Erase the note with the specified GUID
[**service_book_guid_get**](DefaultApi.md#service_book_guid_get) | **GET** /service_book/{guid} | Retrieve note with the GUID
[**service_book_post**](DefaultApi.md#service_book_post) | **POST** /service_book | Add a service book note
[**sessions_get**](DefaultApi.md#sessions_get) | **GET** /sessions | Retrieve the list of sessions
[**sessions_guid_delete**](DefaultApi.md#sessions_guid_delete) | **DELETE** /sessions/{guid} | Erase the session with the specified GUID
[**sessions_guid_export_get**](DefaultApi.md#sessions_guid_export_get) | **GET** /sessions/{guid}/export | Download a file containing the session with the specified GUID
[**sessions_guid_get**](DefaultApi.md#sessions_guid_get) | **GET** /sessions/{guid} | Retrieve the details about the session with the specified GUID
[**sessions_guid_put**](DefaultApi.md#sessions_guid_put) | **PUT** /sessions/{guid} | Modify the values of the session with the specified GUID
[**sessions_import_delete**](DefaultApi.md#sessions_import_delete) | **DELETE** /sessions/import | Cancel currently running import
[**sessions_import_get**](DefaultApi.md#sessions_import_get) | **GET** /sessions/import | Get progress of the running import
[**sessions_import_post**](DefaultApi.md#sessions_import_post) | **POST** /sessions/import | Import the session contained in the file
[**sessions_post**](DefaultApi.md#sessions_post) | **POST** /sessions | Add a new session
[**sessions_session_id_maps_get**](DefaultApi.md#sessions_session_id_maps_get) | **GET** /sessions/{session_id}/maps | Retrieve the list of maps that belong to the session with the specified session ID
[**sessions_session_id_missions_get**](DefaultApi.md#sessions_session_id_missions_get) | **GET** /sessions/{session_id}/missions | Retrieve the list of missions that belong to the session with the specified session ID
[**sessions_session_id_position_transition_lists_get**](DefaultApi.md#sessions_session_id_position_transition_lists_get) | **GET** /sessions/{session_id}/position_transition_lists | Retrieve the list of position transition lists that belong to the session with the specified session ID
[**setting_groups_get**](DefaultApi.md#setting_groups_get) | **GET** /setting_groups | Retrieve a list with the settings groups
[**setting_groups_id_get**](DefaultApi.md#setting_groups_id_get) | **GET** /setting_groups/{id} | Retrieve the details about the settings group with the specified ID
[**setting_groups_settings_group_id_settings_advanced_get**](DefaultApi.md#setting_groups_settings_group_id_settings_advanced_get) | **GET** /setting_groups/{settings_group_id}/settings/advanced | Retrieve the list of advanced settings from the settings group with the specified settings group ID
[**setting_groups_settings_group_id_settings_get**](DefaultApi.md#setting_groups_settings_group_id_settings_get) | **GET** /setting_groups/{settings_group_id}/settings | Retrieve the list of settings from the settings group with the specified settings group ID
[**settings_advanced_get**](DefaultApi.md#settings_advanced_get) | **GET** /settings/advanced | Retrieve the list with the advanced settings
[**settings_advanced_id_get**](DefaultApi.md#settings_advanced_id_get) | **GET** /settings/advanced/{id} | Retrieve the details of the advanced setting with the specified ID
[**settings_advanced_id_put**](DefaultApi.md#settings_advanced_id_put) | **PUT** /settings/advanced/{id} | Modify the values of the advanced setting with the specified ID
[**settings_get**](DefaultApi.md#settings_get) | **GET** /settings | Retrieve a list with the settings
[**settings_id_get**](DefaultApi.md#settings_id_get) | **GET** /settings/{id} | Retrieve the details of the setting with the specified ID
[**settings_id_put**](DefaultApi.md#settings_id_put) | **PUT** /settings/{id} | Modify the values of the setting with the specified ID
[**shelf_types_get**](DefaultApi.md#shelf_types_get) | **GET** /shelf_types | Retrieve the list of shelf types
[**shelf_types_guid_delete**](DefaultApi.md#shelf_types_guid_delete) | **DELETE** /shelf_types/{guid} | Erase the shelf type with the specified GUID
[**shelf_types_guid_get**](DefaultApi.md#shelf_types_guid_get) | **GET** /shelf_types/{guid} | Retrieve the details about the shelf type with the specified GUID
[**shelf_types_guid_put**](DefaultApi.md#shelf_types_guid_put) | **PUT** /shelf_types/{guid} | Modify the values of the shelf type with the specified GUID
[**shelf_types_post**](DefaultApi.md#shelf_types_post) | **POST** /shelf_types | Add a new shelf type
[**software_backups_get**](DefaultApi.md#software_backups_get) | **GET** /software/backups | Retrieve the list with all the software backups
[**software_backups_guid_delete**](DefaultApi.md#software_backups_guid_delete) | **DELETE** /software/backups/{guid} | Erase the software backup with the specified GUID
[**software_backups_guid_get**](DefaultApi.md#software_backups_guid_get) | **GET** /software/backups/{guid} | Retrieve the details about the software backup with the specified GUID
[**software_backups_guid_post**](DefaultApi.md#software_backups_guid_post) | **POST** /software/backups/{guid} | If it exists a software backup with the specified GUID it will restore that backup. Otherwise, it will create a software backup with the specified GUID
[**software_backups_post**](DefaultApi.md#software_backups_post) | **POST** /software/backups | Create a new software backup
[**software_lock_get**](DefaultApi.md#software_lock_get) | **GET** /software/lock | Retrieve the status of the software lock
[**software_lock_put**](DefaultApi.md#software_lock_put) | **PUT** /software/lock | Modify the software lock
[**software_logs_get**](DefaultApi.md#software_logs_get) | **GET** /software/logs | Retrieve the list of software upgrade logs
[**software_logs_guid_get**](DefaultApi.md#software_logs_guid_get) | **GET** /software/logs/{guid} | Retrieve the details about the software upgrade log with the specified GUID
[**software_upgrades_get**](DefaultApi.md#software_upgrades_get) | **GET** /software/upgrades | Retrieve a list of the software upgrade performed
[**software_upgrades_guid_delete**](DefaultApi.md#software_upgrades_guid_delete) | **DELETE** /software/upgrades/{guid} | Erase the upgrade file with the specified GUID
[**software_upgrades_guid_get**](DefaultApi.md#software_upgrades_guid_get) | **GET** /software/upgrades/{guid} | Retrieve the details of the software upgrade with the specified GUID
[**software_upgrades_guid_post**](DefaultApi.md#software_upgrades_guid_post) | **POST** /software/upgrades/{guid} | Upgrade to the version of the upgrade file with the specified GUID
[**software_upgrades_post**](DefaultApi.md#software_upgrades_post) | **POST** /software/upgrades | Upgrade with the provided upgrade file
[**sounds_get**](DefaultApi.md#sounds_get) | **GET** /sounds | Retrieve the list of sounds
[**sounds_guid_delete**](DefaultApi.md#sounds_guid_delete) | **DELETE** /sounds/{guid} | Erase the sound with the specified GUID
[**sounds_guid_get**](DefaultApi.md#sounds_guid_get) | **GET** /sounds/{guid} | Retrieve the details about the sound with the specified GUID
[**sounds_guid_put**](DefaultApi.md#sounds_guid_put) | **PUT** /sounds/{guid} | Modify the values of the sound with the specified GUID
[**sounds_guid_stream_get**](DefaultApi.md#sounds_guid_stream_get) | **GET** /sounds/{guid}/stream | Download the sound file of the sound with the specified GUID
[**sounds_post**](DefaultApi.md#sounds_post) | **POST** /sounds | Add a new sound
[**statistics_distance_get**](DefaultApi.md#statistics_distance_get) | **GET** /statistics/distance | Retrieve the list with the distance driven by the robot at different dates and times
[**status_get**](DefaultApi.md#status_get) | **GET** /status | Retrieve the status
[**status_put**](DefaultApi.md#status_put) | **PUT** /status | Modify the status
[**system_info_get**](DefaultApi.md#system_info_get) | **GET** /system/info | Retrieve the information about the system. It contains different information like serial numbers of hardware components, MAC addresses of network cards, etc…
[**user_groups_get**](DefaultApi.md#user_groups_get) | **GET** /user_groups | Retrieve the list of user groups
[**user_groups_guid_delete**](DefaultApi.md#user_groups_guid_delete) | **DELETE** /user_groups/{guid} | Erase the user group with the specified GUID
[**user_groups_guid_get**](DefaultApi.md#user_groups_guid_get) | **GET** /user_groups/{guid} | Retrieve the details about the user group with the specified GUID
[**user_groups_guid_put**](DefaultApi.md#user_groups_guid_put) | **PUT** /user_groups/{guid} | Modify the values of the user group with the specified GUID
[**user_groups_post**](DefaultApi.md#user_groups_post) | **POST** /user_groups | Add a new user group
[**user_groups_user_group_guid_permissions_get**](DefaultApi.md#user_groups_user_group_guid_permissions_get) | **GET** /user_groups/{user_group_guid}/permissions | Retrieve the list of permissions of the user group with the specified group GUID
[**user_groups_user_group_guid_permissions_post**](DefaultApi.md#user_groups_user_group_guid_permissions_post) | **POST** /user_groups/{user_group_guid}/permissions | Add a new permission to the group with the specified group GUID
[**users_auth_delete**](DefaultApi.md#users_auth_delete) | **DELETE** /users/auth | Logout user
[**users_auth_post**](DefaultApi.md#users_auth_post) | **POST** /users/auth | Login with user credentials
[**users_get**](DefaultApi.md#users_get) | **GET** /users | Retrieve the list of users
[**users_guid_delete**](DefaultApi.md#users_guid_delete) | **DELETE** /users/{guid} | Erase the user with the specified GUID
[**users_guid_get**](DefaultApi.md#users_guid_get) | **GET** /users/{guid} | Retrieve the details about the user with the specified GUID
[**users_guid_put**](DefaultApi.md#users_guid_put) | **PUT** /users/{guid} | Modify the values of the user with the specified GUID
[**users_me_get**](DefaultApi.md#users_me_get) | **GET** /users/me | Retrieve the details about the user currently authorized in the API
[**users_me_permissions_get**](DefaultApi.md#users_me_permissions_get) | **GET** /users/me/permissions | Retrieve the permission of the user currently authorized in the API
[**users_me_put**](DefaultApi.md#users_me_put) | **PUT** /users/me | Modify the values of the user currently authorized in the API
[**users_post**](DefaultApi.md#users_post) | **POST** /users | Add a new user
[**wifi_connections_get**](DefaultApi.md#wifi_connections_get) | **GET** /wifi/connections | Retrieve the list of WiFi networks already configured
[**wifi_connections_post**](DefaultApi.md#wifi_connections_post) | **POST** /wifi/connections | Add a new WiFi network configuration
[**wifi_connections_uuid_delete**](DefaultApi.md#wifi_connections_uuid_delete) | **DELETE** /wifi/connections/{uuid} | Erase the WiFi network configuration with the specified UUID
[**wifi_connections_uuid_get**](DefaultApi.md#wifi_connections_uuid_get) | **GET** /wifi/connections/{uuid} | Retrieve the details about the WiFi network configuration with the specified UUID
[**wifi_connections_uuid_post**](DefaultApi.md#wifi_connections_uuid_post) | **POST** /wifi/connections/{uuid} | Connect to the network with the specified UUID
[**wifi_get**](DefaultApi.md#wifi_get) | **GET** /wifi | Retrieve the URLs to the 3 WiFi related endpoints
[**wifi_networks_get**](DefaultApi.md#wifi_networks_get) | **GET** /wifi/networks | Retrieve the list of WiFi networks available for the robot to connect
[**wifi_networks_guid_get**](DefaultApi.md#wifi_networks_guid_get) | **GET** /wifi/networks/{guid} | Retrieve the details about the WiFi network with the specified GUID
[**world_model_get**](DefaultApi.md#world_model_get) | **GET** /world_model | Retrieve the information about the needed resources from the robot
[**world_model_post**](DefaultApi.md#world_model_post) | **POST** /world_model | Upload the world model with the existing robots, resources and positions and their respective locks

# **actions_action_type_get**
> GetActionDefinition actions_action_type_get(action_type, accept_language=accept_language)

Retrieve the details about the action. It displays the parameters of the action and the limits for the values among others

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
action_type = 'action_type_example' # str | The action_type to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the action. It displays the parameters of the action and the limits for the values among others
    api_response = api_instance.actions_action_type_get(action_type, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_action_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_type** | **str**| The action_type to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetActionDefinition**](GetActionDefinition.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_action_type_post**
> GetActionDefinition actions_action_type_post(body, action_type, accept_language=accept_language)

Add a new action definition with the specified action_type

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostActionDefinition() # PostActionDefinition | The details of the action_definition
action_type = 'action_type_example' # str | The action_type to add the new resource to
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new action definition with the specified action_type
    api_response = api_instance.actions_action_type_post(body, action_type, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_action_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostActionDefinition**](PostActionDefinition.md)| The details of the action_definition | 
 **action_type** | **str**| The action_type to add the new resource to | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetActionDefinition**](GetActionDefinition.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_get**
> GetActionDefinitions actions_get(accept_language=accept_language)

Retrieve the list of action definitions

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of action definitions
    api_response = api_instance.actions_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetActionDefinitions**](GetActionDefinitions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **area_events_action_definitions_action_type_get**
> GetAreaActionDefinition area_events_action_definitions_action_type_get(action_type, accept_language=accept_language)

Retrieve the details about the action. It displays the parameters of the action and the limits for the values among others

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
action_type = 'action_type_example' # str | The action_type to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the action. It displays the parameters of the action and the limits for the values among others
    api_response = api_instance.area_events_action_definitions_action_type_get(action_type, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->area_events_action_definitions_action_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_type** | **str**| The action_type to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetAreaActionDefinition**](GetAreaActionDefinition.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **area_events_action_definitions_get**
> GetAreaActionDefinitions area_events_action_definitions_get(accept_language=accept_language)

Retrieve definitions of area actions and their parameters

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve definitions of area actions and their parameters
    api_response = api_instance.area_events_action_definitions_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->area_events_action_definitions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetAreaActionDefinitions**](GetAreaActionDefinitions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **area_events_definitions_get**
> GetAreaEventsDefinitions area_events_definitions_get(accept_language=accept_language)

Retrieve definitions of areas and their actions

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve definitions of areas and their actions
    api_response = api_instance.area_events_definitions_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->area_events_definitions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetAreaEventsDefinitions**](GetAreaEventsDefinitions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **area_events_get**
> list[GetAreaEvents] area_events_get(accept_language=accept_language)

Retrieve the list of area events

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of area events
    api_response = api_instance.area_events_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->area_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetAreaEvents]**](GetAreaEvents.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **area_events_guid_delete**
> area_events_guid_delete(guid, accept_language=accept_language)

Erase the area event with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the area event with the specified GUID
    api_instance.area_events_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->area_events_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **area_events_guid_get**
> GetAreaEvent area_events_guid_get(guid, accept_language=accept_language)

Retrieve the details about the area event with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the area event with the specified GUID
    api_response = api_instance.area_events_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->area_events_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetAreaEvent**](GetAreaEvent.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **area_events_guid_put**
> GetAreaEvent area_events_guid_put(body, guid, accept_language=accept_language)

Modify the values of the area event with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutAreaEvent() # PutAreaEvent | The new values of the area_event
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the area event with the specified GUID
    api_response = api_instance.area_events_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->area_events_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutAreaEvent**](PutAreaEvent.md)| The new values of the area_event | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetAreaEvent**](GetAreaEvent.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **area_events_post**
> GetAreaEvents area_events_post(body, accept_language=accept_language)

Add a new area event

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostAreaEvents() # PostAreaEvents | The details of the area_events
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new area event
    api_response = api_instance.area_events_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->area_events_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostAreaEvents**](PostAreaEvents.md)| The details of the area_events | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetAreaEvents**](GetAreaEvents.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bluetooth_delete**
> bluetooth_delete(accept_language=accept_language)

Disconnect the Bluetooth device

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Disconnect the Bluetooth device
    api_instance.bluetooth_delete(accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->bluetooth_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bluetooth_get**
> GetBluetoothStatus bluetooth_get(accept_language=accept_language)

Retrieve the status of the Bluetooth connection

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the status of the Bluetooth connection
    api_response = api_instance.bluetooth_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bluetooth_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetBluetoothStatus**](GetBluetoothStatus.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bluetooth_post**
> GetBluetoothStatus bluetooth_post(body, accept_language=accept_language)

Connect to the Bluetooth device with the given GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostBluetoothStatus() # PostBluetoothStatus | The details of the bluetooth_status
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Connect to the Bluetooth device with the given GUID
    api_response = api_instance.bluetooth_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bluetooth_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostBluetoothStatus**](PostBluetoothStatus.md)| The details of the bluetooth_status | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetBluetoothStatus**](GetBluetoothStatus.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bluetooth_put**
> GetBluetoothStatus bluetooth_put(body, accept_language=accept_language)

Modify the outputs of the connected Bluetooth device

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutBluetoothStatus() # PutBluetoothStatus | The new values of the bluetooth_status
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the outputs of the connected Bluetooth device
    api_response = api_instance.bluetooth_put(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bluetooth_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutBluetoothStatus**](PutBluetoothStatus.md)| The new values of the bluetooth_status | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetBluetoothStatus**](GetBluetoothStatus.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bluetooth_relays_get**
> list[GetBluetoothRelays] bluetooth_relays_get(accept_language=accept_language)

Retrieve the list of configured Bluetooth devices

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of configured Bluetooth devices
    api_response = api_instance.bluetooth_relays_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bluetooth_relays_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetBluetoothRelays]**](GetBluetoothRelays.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bluetooth_relays_guid_delete**
> bluetooth_relays_guid_delete(guid, accept_language=accept_language)

Erase the Bluetooth device with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the Bluetooth device with the specified GUID
    api_instance.bluetooth_relays_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->bluetooth_relays_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bluetooth_relays_guid_get**
> GetBluetoothRelay bluetooth_relays_guid_get(guid, accept_language=accept_language)

Retrieve the details about the Bluetooth device with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the Bluetooth device with the specified GUID
    api_response = api_instance.bluetooth_relays_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bluetooth_relays_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetBluetoothRelay**](GetBluetoothRelay.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bluetooth_relays_guid_put**
> GetBluetoothRelay bluetooth_relays_guid_put(body, guid, accept_language=accept_language)

Modify the values of the Bluetooth device with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutBluetoothRelay() # PutBluetoothRelay | The new values of the bluetooth_relay
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the Bluetooth device with the specified GUID
    api_response = api_instance.bluetooth_relays_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bluetooth_relays_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutBluetoothRelay**](PutBluetoothRelay.md)| The new values of the bluetooth_relay | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetBluetoothRelay**](GetBluetoothRelay.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bluetooth_relays_post**
> GetBluetoothRelays bluetooth_relays_post(body, accept_language=accept_language)

Add a new Bluetooth device

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostBluetoothRelays() # PostBluetoothRelays | The details of the bluetooth_relays
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new Bluetooth device
    api_response = api_instance.bluetooth_relays_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bluetooth_relays_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostBluetoothRelays**](PostBluetoothRelays.md)| The details of the bluetooth_relays | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetBluetoothRelays**](GetBluetoothRelays.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bluetooth_scan_get**
> list[GetBluetooth] bluetooth_scan_get(accept_language=accept_language)

Start the discovery of Bluetooth devices

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Start the discovery of Bluetooth devices
    api_response = api_instance.bluetooth_scan_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bluetooth_scan_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetBluetooth]**](GetBluetooth.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bluetooth_scan_post**
> GetBluetooth bluetooth_scan_post(accept_language=accept_language)

Retrieve the list of discovered devices

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of discovered devices
    api_response = api_instance.bluetooth_scan_post(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bluetooth_scan_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetBluetooth**](GetBluetooth.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_calibrations_get**
> list[GetCartCalibrations] cart_calibrations_get(accept_language=accept_language)

Retrieve the list of cart calibrations

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of cart calibrations
    api_response = api_instance.cart_calibrations_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cart_calibrations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetCartCalibrations]**](GetCartCalibrations.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_calibrations_guid_delete**
> cart_calibrations_guid_delete(guid, accept_language=accept_language)

Erase the cart calibration with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the cart calibration with the specified GUID
    api_instance.cart_calibrations_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->cart_calibrations_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_calibrations_guid_get**
> GetCartCalibration cart_calibrations_guid_get(guid, accept_language=accept_language)

Retrieve the details about the cart calibration with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the cart calibration with the specified GUID
    api_response = api_instance.cart_calibrations_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cart_calibrations_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetCartCalibration**](GetCartCalibration.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_calibrations_guid_put**
> GetCartCalibration cart_calibrations_guid_put(body, guid, accept_language=accept_language)

Modify the values of the cart calibration with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutCartCalibration() # PutCartCalibration | The new values of the cart_calibration
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the cart calibration with the specified GUID
    api_response = api_instance.cart_calibrations_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cart_calibrations_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutCartCalibration**](PutCartCalibration.md)| The new values of the cart_calibration | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetCartCalibration**](GetCartCalibration.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_calibrations_post**
> GetCartCalibrations cart_calibrations_post(body, accept_language=accept_language)

Add a new cart calibration

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostCartCalibrations() # PostCartCalibrations | The details of the cart_calibrations
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new cart calibration
    api_response = api_instance.cart_calibrations_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cart_calibrations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCartCalibrations**](PostCartCalibrations.md)| The details of the cart_calibrations | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetCartCalibrations**](GetCartCalibrations.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_types_get**
> list[GetCartTypes] cart_types_get(accept_language=accept_language)

Retrieve the list of cart types

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of cart types
    api_response = api_instance.cart_types_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cart_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetCartTypes]**](GetCartTypes.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_types_guid_delete**
> cart_types_guid_delete(guid, accept_language=accept_language)

Erase the cart type with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the cart type with the specified GUID
    api_instance.cart_types_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->cart_types_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_types_guid_get**
> GetCartType cart_types_guid_get(guid, accept_language=accept_language)

Retrieve the details about the cart type with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the cart type with the specified GUID
    api_response = api_instance.cart_types_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cart_types_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetCartType**](GetCartType.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_types_guid_put**
> GetCartType cart_types_guid_put(body, guid, accept_language=accept_language)

Modify the values of the cart type with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutCartType() # PutCartType | The new values of the cart_type
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the cart type with the specified GUID
    api_response = api_instance.cart_types_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cart_types_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutCartType**](PutCartType.md)| The new values of the cart_type | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetCartType**](GetCartType.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cart_types_post**
> GetCartTypes cart_types_post(body, accept_language=accept_language)

Add a new cart type

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostCartTypes() # PostCartTypes | The details of the cart_types
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new cart type
    api_response = api_instance.cart_types_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cart_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCartTypes**](PostCartTypes.md)| The details of the cart_types | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetCartTypes**](GetCartTypes.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **carts_get**
> list[GetCarts] carts_get(accept_language=accept_language)

Retrieve the list of carts

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of carts
    api_response = api_instance.carts_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->carts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetCarts]**](GetCarts.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **carts_guid_delete**
> carts_guid_delete(guid, accept_language=accept_language)

Erase the cart with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the cart with the specified GUID
    api_instance.carts_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->carts_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **carts_guid_get**
> GetCart carts_guid_get(guid, accept_language=accept_language)

Retrieve the details about the cart with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the cart with the specified GUID
    api_response = api_instance.carts_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->carts_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetCart**](GetCart.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **carts_guid_put**
> GetCart carts_guid_put(body, guid, accept_language=accept_language)

Modify the values of the cart with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutCart() # PutCart | The new values of the cart
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the cart with the specified GUID
    api_response = api_instance.carts_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->carts_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutCart**](PutCart.md)| The new values of the cart | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetCart**](GetCart.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **carts_post**
> GetCarts carts_post(body, accept_language=accept_language)

Add a new cart

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostCarts() # PostCarts | The details of the carts
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new cart
    api_response = api_instance.carts_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->carts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCarts**](PostCarts.md)| The details of the carts | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetCarts**](GetCarts.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **changes_me_delete**
> changes_me_delete(accept_language=accept_language)

Deletes all data owned by the current user or users with lower authority

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Deletes all data owned by the current user or users with lower authority
    api_instance.changes_me_delete(accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->changes_me_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **changes_me_get**
> GetChangesMe changes_me_get(accept_language=accept_language)

Makes a list of all data owned by the current user or users with lower authority

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Makes a list of all data owned by the current user or users with lower authority
    api_response = api_instance.changes_me_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->changes_me_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetChangesMe**](GetChangesMe.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_dashboard_id_widgets_get**
> list[GetDashboardWidgets] dashboards_dashboard_id_widgets_get(dashboard_id, accept_language=accept_language)

Retrieve the list of widgets of the dashboard with the specified dashboard ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | The dashboard_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of widgets of the dashboard with the specified dashboard ID
    api_response = api_instance.dashboards_dashboard_id_widgets_get(dashboard_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dashboards_dashboard_id_widgets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| The dashboard_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetDashboardWidgets]**](GetDashboardWidgets.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_dashboard_id_widgets_guid_delete**
> dashboards_dashboard_id_widgets_guid_delete(dashboard_id, guid, accept_language=accept_language)

Erase the widget with the specified GUID from the dashboard with the specified dashboard ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | The dashboard_id to delete
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the widget with the specified GUID from the dashboard with the specified dashboard ID
    api_instance.dashboards_dashboard_id_widgets_guid_delete(dashboard_id, guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->dashboards_dashboard_id_widgets_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| The dashboard_id to delete | 
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_dashboard_id_widgets_guid_get**
> GetDashboardWidget dashboards_dashboard_id_widgets_guid_get(dashboard_id, guid, accept_language=accept_language)

Retrieve the details about the widget with the specified GUID in the dashboard with the specified dashboard ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
dashboard_id = 'dashboard_id_example' # str | The dashboard_id to search for
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the widget with the specified GUID in the dashboard with the specified dashboard ID
    api_response = api_instance.dashboards_dashboard_id_widgets_guid_get(dashboard_id, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dashboards_dashboard_id_widgets_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**| The dashboard_id to search for | 
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetDashboardWidget**](GetDashboardWidget.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_dashboard_id_widgets_guid_put**
> GetDashboardWidget dashboards_dashboard_id_widgets_guid_put(body, dashboard_id, guid, accept_language=accept_language)

Modify the values of the widget with the specified GUID in the dashboard with the specified dashboard ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutDashboardWidget() # PutDashboardWidget | The new values of the dashboard_widget
dashboard_id = 'dashboard_id_example' # str | The dashboard_id to modify
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the widget with the specified GUID in the dashboard with the specified dashboard ID
    api_response = api_instance.dashboards_dashboard_id_widgets_guid_put(body, dashboard_id, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dashboards_dashboard_id_widgets_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutDashboardWidget**](PutDashboardWidget.md)| The new values of the dashboard_widget | 
 **dashboard_id** | **str**| The dashboard_id to modify | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetDashboardWidget**](GetDashboardWidget.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_dashboard_id_widgets_post**
> GetDashboardWidgets dashboards_dashboard_id_widgets_post(body, dashboard_id, accept_language=accept_language)

Add a new widget to the dashboard with the specified dashboard ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostDashboardWidgets() # PostDashboardWidgets | The details of the dashboard_widgets
dashboard_id = 'dashboard_id_example' # str | The dashboard_id to add the new resource to
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new widget to the dashboard with the specified dashboard ID
    api_response = api_instance.dashboards_dashboard_id_widgets_post(body, dashboard_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dashboards_dashboard_id_widgets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostDashboardWidgets**](PostDashboardWidgets.md)| The details of the dashboard_widgets | 
 **dashboard_id** | **str**| The dashboard_id to add the new resource to | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetDashboardWidgets**](GetDashboardWidgets.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_get**
> list[GetDashboards] dashboards_get(accept_language=accept_language)

Retrieve the list of dashboards

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of dashboards
    api_response = api_instance.dashboards_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dashboards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetDashboards]**](GetDashboards.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_guid_delete**
> dashboards_guid_delete(guid, accept_language=accept_language)

Erase the dashboard with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the dashboard with the specified GUID
    api_instance.dashboards_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->dashboards_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_guid_get**
> GetDashboard dashboards_guid_get(guid, accept_language=accept_language)

Retrieve the details of the dashboard with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details of the dashboard with the specified GUID
    api_response = api_instance.dashboards_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dashboards_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetDashboard**](GetDashboard.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_guid_put**
> GetDashboard dashboards_guid_put(body, guid, accept_language=accept_language)

Modify the values of the dashboard with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutDashboard() # PutDashboard | The new values of the dashboard
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the dashboard with the specified GUID
    api_response = api_instance.dashboards_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dashboards_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutDashboard**](PutDashboard.md)| The new values of the dashboard | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetDashboard**](GetDashboard.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_post**
> GetDashboards dashboards_post(body, accept_language=accept_language)

Add a new dashboard

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostDashboards() # PostDashboards | The details of the dashboards
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new dashboard
    api_response = api_instance.dashboards_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->dashboards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostDashboards**](PostDashboards.md)| The details of the dashboards | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetDashboards**](GetDashboards.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docking_offsets_get**
> list[GetDockingOffsets] docking_offsets_get(accept_language=accept_language)

Retrieve the list of docking offsets

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of docking offsets
    api_response = api_instance.docking_offsets_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->docking_offsets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetDockingOffsets]**](GetDockingOffsets.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docking_offsets_guid_delete**
> docking_offsets_guid_delete(guid, accept_language=accept_language)

Erase the docking offset with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the docking offset with the specified GUID
    api_instance.docking_offsets_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->docking_offsets_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docking_offsets_guid_get**
> GetDockingOffset docking_offsets_guid_get(guid, accept_language=accept_language)

Retrieve the details of the docking offset with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details of the docking offset with the specified GUID
    api_response = api_instance.docking_offsets_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->docking_offsets_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetDockingOffset**](GetDockingOffset.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docking_offsets_guid_put**
> GetDockingOffset docking_offsets_guid_put(body, guid, accept_language=accept_language)

Modify the values of the docking offset with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutDockingOffset() # PutDockingOffset | The new values of the docking_offset
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the docking offset with the specified GUID
    api_response = api_instance.docking_offsets_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->docking_offsets_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutDockingOffset**](PutDockingOffset.md)| The new values of the docking_offset | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetDockingOffset**](GetDockingOffset.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docking_offsets_post**
> GetDockingOffsets docking_offsets_post(body, accept_language=accept_language)

Add a new docking offset. The only positions that can have docking offsets are Charging stations, V markers and VL markers

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostDockingOffsets() # PostDockingOffsets | The details of the docking_offsets
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new docking offset. The only positions that can have docking offsets are Charging stations, V markers and VL markers
    api_response = api_instance.docking_offsets_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->docking_offsets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostDockingOffsets**](PostDockingOffsets.md)| The details of the docking_offsets | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetDockingOffsets**](GetDockingOffsets.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **factory_reset_post**
> GetFactoryReset factory_reset_post(body, accept_language=accept_language)

Clean and migrate the database. Keep hardware configurations

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostFactoryReset() # PostFactoryReset | The details of the factory_reset
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Clean and migrate the database. Keep hardware configurations
    api_response = api_instance.factory_reset_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->factory_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostFactoryReset**](PostFactoryReset.md)| The details of the factory_reset | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetFactoryReset**](GetFactoryReset.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hook_brake_get**
> GetHookBrake hook_brake_get(accept_language=accept_language)

Retrieve the state of the Hook brake

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the state of the Hook brake
    api_response = api_instance.hook_brake_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hook_brake_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetHookBrake**](GetHookBrake.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hook_brake_put**
> GetHookBrake hook_brake_put(body, accept_language=accept_language)

Activate or release the Hook brake

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutHookBrake() # PutHookBrake | The new values of the hook_brake
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Activate or release the Hook brake
    api_response = api_instance.hook_brake_put(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hook_brake_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutHookBrake**](PutHookBrake.md)| The new values of the hook_brake | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetHookBrake**](GetHookBrake.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hook_gripper_get**
> GetHookGripper hook_gripper_get(accept_language=accept_language)

Retrieve the state of the Hook gripper

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the state of the Hook gripper
    api_response = api_instance.hook_gripper_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hook_gripper_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetHookGripper**](GetHookGripper.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hook_gripper_put**
> GetHookGripper hook_gripper_put(body, accept_language=accept_language)

Open or close the Hook gripper

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutHookGripper() # PutHookGripper | The new values of the hook_gripper
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Open or close the Hook gripper
    api_response = api_instance.hook_gripper_put(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hook_gripper_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutHookGripper**](PutHookGripper.md)| The new values of the hook_gripper | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetHookGripper**](GetHookGripper.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hook_height_get**
> GetHookHeight hook_height_get(accept_language=accept_language)

Retrieve the height of the Hook

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the height of the Hook
    api_response = api_instance.hook_height_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hook_height_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetHookHeight**](GetHookHeight.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hook_height_put**
> GetHookHeight hook_height_put(body, accept_language=accept_language)

Modify the height of the Hook

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutHookHeight() # PutHookHeight | The new values of the hook_height
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the height of the Hook
    api_response = api_instance.hook_height_put(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hook_height_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutHookHeight**](PutHookHeight.md)| The new values of the hook_height | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetHookHeight**](GetHookHeight.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hook_status_get**
> GetHook hook_status_get(accept_language=accept_language)

Retrieve the extended status of the Hook

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the extended status of the Hook
    api_response = api_instance.hook_status_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hook_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetHook**](GetHook.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hw_export_get**
> GetHwConfigExport hw_export_get(accept_language=accept_language)

Download a file containing the hardware configuration of the robot

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Download a file containing the hardware configuration of the robot
    api_response = api_instance.hw_export_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hw_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetHwConfigExport**](GetHwConfigExport.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hw_import_post**
> GetHwConfigImport hw_import_post(body, accept_language=accept_language)

Import the hardware configuration contained in the file into the robot

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostHwConfigImport() # PostHwConfigImport | The details of the hw_config_import
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Import the hardware configuration contained in the file into the robot
    api_response = api_instance.hw_import_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hw_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostHwConfigImport**](PostHwConfigImport.md)| The details of the hw_config_import | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetHwConfigImport**](GetHwConfigImport.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_get**
> list[GetIoModules] io_modules_get(accept_language=accept_language)

Retrieve the list of configured IO modules

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of configured IO modules
    api_response = api_instance.io_modules_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->io_modules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetIoModules]**](GetIoModules.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_guid_delete**
> io_modules_guid_delete(guid, accept_language=accept_language)

Erase the IO device with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the IO device with the specified GUID
    api_instance.io_modules_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->io_modules_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_guid_get**
> GetIoModule io_modules_guid_get(guid, accept_language=accept_language)

Retrieve the details about a IO device with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about a IO device with the specified GUID
    api_response = api_instance.io_modules_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->io_modules_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetIoModule**](GetIoModule.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_guid_put**
> GetIoModule io_modules_guid_put(body, guid, accept_language=accept_language)

Modify the values of the IO device with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutIoModule() # PutIoModule | The new values of the io_module
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the IO device with the specified GUID
    api_response = api_instance.io_modules_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->io_modules_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutIoModule**](PutIoModule.md)| The new values of the io_module | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetIoModule**](GetIoModule.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_guid_status_delete**
> io_modules_guid_status_delete(guid, accept_language=accept_language)

Disconnect from the IO module with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Disconnect from the IO module with the specified GUID
    api_instance.io_modules_guid_status_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->io_modules_guid_status_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_guid_status_get**
> GetIoModuleStatus io_modules_guid_status_get(guid, accept_language=accept_language)

Retrieve the status of the connection to the IO module with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the status of the connection to the IO module with the specified GUID
    api_response = api_instance.io_modules_guid_status_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->io_modules_guid_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetIoModuleStatus**](GetIoModuleStatus.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_guid_status_post**
> GetIoModuleStatus io_modules_guid_status_post(body, guid, accept_language=accept_language)

Connect to theIO module with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = NULL # object | The details of the io_module_status
guid = 'guid_example' # str | The guid to add the new resource to
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Connect to theIO module with the specified GUID
    api_response = api_instance.io_modules_guid_status_post(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->io_modules_guid_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The details of the io_module_status | 
 **guid** | **str**| The guid to add the new resource to | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetIoModuleStatus**](GetIoModuleStatus.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_guid_status_put**
> GetIoModuleStatus io_modules_guid_status_put(body, guid, accept_language=accept_language)

Modify the outputs of the connected IO module with specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutIoModuleStatus() # PutIoModuleStatus | The new values of the io_module_status
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the outputs of the connected IO module with specified GUID
    api_response = api_instance.io_modules_guid_status_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->io_modules_guid_status_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutIoModuleStatus**](PutIoModuleStatus.md)| The new values of the io_module_status | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetIoModuleStatus**](GetIoModuleStatus.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **io_modules_post**
> GetIoModules io_modules_post(body, accept_language=accept_language)

Add a new IO module

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostIoModules() # PostIoModules | The details of the io_modules
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new IO module
    api_response = api_instance.io_modules_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->io_modules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostIoModules**](PostIoModules.md)| The details of the io_modules | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetIoModules**](GetIoModules.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_error_reports_delete**
> log_error_reports_delete(accept_language=accept_language)

Erase ALL the error reports

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase ALL the error reports
    api_instance.log_error_reports_delete(accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->log_error_reports_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_error_reports_get**
> GetErrorReports log_error_reports_get(accept_language=accept_language)

Retrieve the list of error reports

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of error reports
    api_response = api_instance.log_error_reports_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->log_error_reports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetErrorReports**](GetErrorReports.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_error_reports_id_delete**
> log_error_reports_id_delete(id, accept_language=accept_language)

Erase the error report with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
id = 56 # int | The id to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the error report with the specified ID
    api_instance.log_error_reports_id_delete(id, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->log_error_reports_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_error_reports_id_download_get**
> GetErrorReportDownload log_error_reports_id_download_get(id, accept_language=accept_language)

Download the file containing the error report with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
id = 56 # int | The id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Download the file containing the error report with the specified ID
    api_response = api_instance.log_error_reports_id_download_get(id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->log_error_reports_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetErrorReportDownload**](GetErrorReportDownload.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_error_reports_id_get**
> GetErrorReport log_error_reports_id_get(id, accept_language=accept_language)

Retrieve the details about the error report with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
id = 56 # int | The id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the error report with the specified ID
    api_response = api_instance.log_error_reports_id_get(id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->log_error_reports_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetErrorReport**](GetErrorReport.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_error_reports_post**
> GetErrorReports log_error_reports_post(body, accept_language=accept_language)

Generate a new error report. This will record the 30s previous to this call in a file.

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostErrorReports() # PostErrorReports | The details of the error_reports
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Generate a new error report. This will record the 30s previous to this call in a file.
    api_response = api_instance.log_error_reports_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->log_error_reports_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostErrorReports**](PostErrorReports.md)| The details of the error_reports | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetErrorReports**](GetErrorReports.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_get**
> list[GetMaps] maps_get(accept_language=accept_language)

Retrieve the list of maps

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of maps
    api_response = api_instance.maps_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->maps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetMaps]**](GetMaps.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_guid_delete**
> maps_guid_delete(guid, accept_language=accept_language)

Erase the map with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the map with the specified GUID
    api_instance.maps_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->maps_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_guid_get**
> GetMap maps_guid_get(guid, accept_language=accept_language)

Retrieve the details about the map with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the map with the specified GUID
    api_response = api_instance.maps_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->maps_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMap**](GetMap.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_guid_put**
> GetMap maps_guid_put(body, guid, accept_language=accept_language)

Modify the values of the map with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutMap() # PutMap | The new values of the map
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the map with the specified GUID
    api_response = api_instance.maps_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->maps_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutMap**](PutMap.md)| The new values of the map | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMap**](GetMap.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_map_id_area_events_get**
> list[GetMapAreaEvent] maps_map_id_area_events_get(map_id, accept_language=accept_language)

Retrieve the list of area events that belong to the map with the specified map ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
map_id = 'map_id_example' # str | The map_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of area events that belong to the map with the specified map ID
    api_response = api_instance.maps_map_id_area_events_get(map_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->maps_map_id_area_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The map_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetMapAreaEvent]**](GetMapAreaEvent.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_map_id_path_guides_get**
> list[GetMapPathGuides] maps_map_id_path_guides_get(map_id, accept_language=accept_language)

Retrieve the list of path guides that belong to the map with the specified map ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
map_id = 'map_id_example' # str | The map_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of path guides that belong to the map with the specified map ID
    api_response = api_instance.maps_map_id_path_guides_get(map_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->maps_map_id_path_guides_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The map_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetMapPathGuides]**](GetMapPathGuides.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_map_id_paths_get**
> list[GetMapPaths] maps_map_id_paths_get(map_id, accept_language=accept_language)

Retrieve the list of paths that belong to the map with the specified map ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
map_id = 'map_id_example' # str | The map_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of paths that belong to the map with the specified map ID
    api_response = api_instance.maps_map_id_paths_get(map_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->maps_map_id_paths_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The map_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetMapPaths]**](GetMapPaths.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_map_id_positions_get**
> list[GetMapPositions] maps_map_id_positions_get(map_id, accept_language=accept_language)

Retrieve the list of positions that belong to the map with the specified map ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
map_id = 'map_id_example' # str | The map_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of positions that belong to the map with the specified map ID
    api_response = api_instance.maps_map_id_positions_get(map_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->maps_map_id_positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The map_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetMapPositions]**](GetMapPositions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maps_post**
> GetMaps maps_post(body, accept_language=accept_language)

Add a new map

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostMaps() # PostMaps | The details of the maps
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new map
    api_response = api_instance.maps_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->maps_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostMaps**](PostMaps.md)| The details of the maps | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMaps**](GetMaps.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_groups_get**
> list[GetMissionGroups] mission_groups_get(accept_language=accept_language)

Retrieve the list of mission groups

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of mission groups
    api_response = api_instance.mission_groups_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetMissionGroups]**](GetMissionGroups.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_groups_group_id_missions_get**
> list[GetGroupMissions] mission_groups_group_id_missions_get(group_id, accept_language=accept_language)

Retrieve the list of missions that belong to the group with the specified group ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
group_id = 'group_id_example' # str | The group_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of missions that belong to the group with the specified group ID
    api_response = api_instance.mission_groups_group_id_missions_get(group_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_groups_group_id_missions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The group_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetGroupMissions]**](GetGroupMissions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_groups_guid_delete**
> mission_groups_guid_delete(guid, accept_language=accept_language)

Erase the mission group with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the mission group with the specified GUID
    api_instance.mission_groups_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_groups_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_groups_guid_get**
> GetMissionGroup mission_groups_guid_get(guid, accept_language=accept_language)

Retrieve the details about the mission group with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the mission group with the specified GUID
    api_response = api_instance.mission_groups_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_groups_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMissionGroup**](GetMissionGroup.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_groups_guid_put**
> GetMissionGroup mission_groups_guid_put(body, guid, accept_language=accept_language)

Modify the values of the mission group with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutMissionGroup() # PutMissionGroup | The new values of the mission_group
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the mission group with the specified GUID
    api_response = api_instance.mission_groups_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_groups_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutMissionGroup**](PutMissionGroup.md)| The new values of the mission_group | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMissionGroup**](GetMissionGroup.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_groups_mission_group_id_actions_get**
> GetGroupActionDefinition mission_groups_mission_group_id_actions_get(mission_group_id, accept_language=accept_language)

Retrieve the list of action definitions from the mission group with the specified mission group ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
mission_group_id = 'mission_group_id_example' # str | The mission_group_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of action definitions from the mission group with the specified mission group ID
    api_response = api_instance.mission_groups_mission_group_id_actions_get(mission_group_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_groups_mission_group_id_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_group_id** | **str**| The mission_group_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetGroupActionDefinition**](GetGroupActionDefinition.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_groups_post**
> GetMissionGroups mission_groups_post(body, accept_language=accept_language)

Add a new mission group

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostMissionGroups() # PostMissionGroups | The details of the mission_groups
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new mission group
    api_response = api_instance.mission_groups_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostMissionGroups**](PostMissionGroups.md)| The details of the mission_groups | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMissionGroups**](GetMissionGroups.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_queue_delete**
> mission_queue_delete(accept_language=accept_language)

Abort all the pending and executing missions from the mission queue

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Abort all the pending and executing missions from the mission queue
    api_instance.mission_queue_delete(accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_queue_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_queue_get**
> list[GetMissionQueues] mission_queue_get(accept_language=accept_language)

Retrieve the list of missions in the queue. Finished, failed, pending and executing missions will be displayed here

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of missions in the queue. Finished, failed, pending and executing missions will be displayed here
    api_response = api_instance.mission_queue_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_queue_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetMissionQueues]**](GetMissionQueues.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_queue_id_delete**
> mission_queue_id_delete(id, accept_language=accept_language)

Abort the mission with the specified ID in the mission queue

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
id = 56 # int | The id to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Abort the mission with the specified ID in the mission queue
    api_instance.mission_queue_id_delete(id, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_queue_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_queue_id_get**
> GetMissionQueue mission_queue_id_get(id, accept_language=accept_language)

Retrieve the details about the mission with the specified ID in the mission queue

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
id = 56 # int | The id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the mission with the specified ID in the mission queue
    api_response = api_instance.mission_queue_id_get(id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_queue_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMissionQueue**](GetMissionQueue.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_queue_id_put**
> GetMissionQueue mission_queue_id_put(body, id, accept_language=accept_language)

Modify the values of the mission with the specified ID in the mission queue

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutMissionQueue() # PutMissionQueue | The new values of the mission_queue
id = 56 # int | The id to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the mission with the specified ID in the mission queue
    api_response = api_instance.mission_queue_id_put(body, id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_queue_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutMissionQueue**](PutMissionQueue.md)| The new values of the mission_queue | 
 **id** | **int**| The id to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMissionQueue**](GetMissionQueue.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_queue_mission_queue_id_actions_get**
> GetMissionQueueActions mission_queue_mission_queue_id_actions_get(mission_queue_id, accept_language=accept_language)

Retrieve the list of actions from the mission with the specified ID in the mission queue

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
mission_queue_id = 56 # int | The mission_queue_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of actions from the mission with the specified ID in the mission queue
    api_response = api_instance.mission_queue_mission_queue_id_actions_get(mission_queue_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_queue_mission_queue_id_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_queue_id** | **int**| The mission_queue_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMissionQueueActions**](GetMissionQueueActions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_queue_mission_queue_id_actions_id_get**
> GetMissionQueueAction mission_queue_mission_queue_id_actions_id_get(id, mission_queue_id, accept_language=accept_language)

Retrieve the details about the action with the specified ID from the mission with the specified ID in the mission queue

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
id = 56 # int | The id to search for
mission_queue_id = 56 # int | The mission_queue_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the action with the specified ID from the mission with the specified ID in the mission queue
    api_response = api_instance.mission_queue_mission_queue_id_actions_id_get(id, mission_queue_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_queue_mission_queue_id_actions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id to search for | 
 **mission_queue_id** | **int**| The mission_queue_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMissionQueueAction**](GetMissionQueueAction.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mission_queue_post**
> GetMissionQueues mission_queue_post(body, accept_language=accept_language)

Add a new mission to the mission queue. The mission will always go to the end of the queue

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostMissionQueues() # PostMissionQueues | The details of the mission_queues
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new mission to the mission queue. The mission will always go to the end of the queue
    api_response = api_instance.mission_queue_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->mission_queue_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostMissionQueues**](PostMissionQueues.md)| The details of the mission_queues | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMissionQueues**](GetMissionQueues.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_get**
> list[GetMissions] missions_get(accept_language=accept_language)

Retrieve the list of missions

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of missions
    api_response = api_instance.missions_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->missions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetMissions]**](GetMissions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_guid_definition_get**
> list[GetMissionDefinition] missions_guid_definition_get(guid, accept_language=accept_language)

Retrieve the mission with the specified GUID as an action definition that can be inserted in another mission

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the mission with the specified GUID as an action definition that can be inserted in another mission
    api_response = api_instance.missions_guid_definition_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->missions_guid_definition_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetMissionDefinition]**](GetMissionDefinition.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_guid_delete**
> missions_guid_delete(guid, accept_language=accept_language)

Erase the mission with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the mission with the specified GUID
    api_instance.missions_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->missions_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_guid_get**
> GetMission missions_guid_get(guid, accept_language=accept_language)

Retrieve the details about the mission with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the mission with the specified GUID
    api_response = api_instance.missions_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->missions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMission**](GetMission.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_guid_put**
> GetMission missions_guid_put(body, guid, accept_language=accept_language)

Modify the values of the mission with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutMission() # PutMission | The new values of the mission
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the mission with the specified GUID
    api_response = api_instance.missions_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->missions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutMission**](PutMission.md)| The new values of the mission | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMission**](GetMission.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_mission_id_actions_get**
> list[GetMissionActions] missions_mission_id_actions_get(mission_id, accept_language=accept_language)

Retrieve the list of actions that belong to the mission with the specified mission ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
mission_id = 'mission_id_example' # str | The mission_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of actions that belong to the mission with the specified mission ID
    api_response = api_instance.missions_mission_id_actions_get(mission_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->missions_mission_id_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission_id** | **str**| The mission_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetMissionActions]**](GetMissionActions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_mission_id_actions_guid_delete**
> missions_mission_id_actions_guid_delete(guid, mission_id, accept_language=accept_language)

Erase the action with the specified GUID from the mission with the specified mission ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
mission_id = 'mission_id_example' # str | The mission_id to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the action with the specified GUID from the mission with the specified mission ID
    api_instance.missions_mission_id_actions_guid_delete(guid, mission_id, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->missions_mission_id_actions_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **mission_id** | **str**| The mission_id to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_mission_id_actions_guid_get**
> GetMissionAction missions_mission_id_actions_guid_get(guid, mission_id, accept_language=accept_language)

Retrieve the details about the action with the specified GUID that belongs to the mission with the specified mission ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
mission_id = 'mission_id_example' # str | The mission_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the action with the specified GUID that belongs to the mission with the specified mission ID
    api_response = api_instance.missions_mission_id_actions_guid_get(guid, mission_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->missions_mission_id_actions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **mission_id** | **str**| The mission_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMissionAction**](GetMissionAction.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_mission_id_actions_guid_put**
> GetMissionAction missions_mission_id_actions_guid_put(body, guid, mission_id, accept_language=accept_language)

Modify the values of the action with the specified GUID that belongs to the mission with the specified mission ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutMissionAction() # PutMissionAction | The new values of the mission_action
guid = 'guid_example' # str | The guid to modify
mission_id = 'mission_id_example' # str | The mission_id to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the action with the specified GUID that belongs to the mission with the specified mission ID
    api_response = api_instance.missions_mission_id_actions_guid_put(body, guid, mission_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->missions_mission_id_actions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutMissionAction**](PutMissionAction.md)| The new values of the mission_action | 
 **guid** | **str**| The guid to modify | 
 **mission_id** | **str**| The mission_id to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMissionAction**](GetMissionAction.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_mission_id_actions_post**
> GetMissionActions missions_mission_id_actions_post(body, mission_id, accept_language=accept_language)

Add a new action to the mission with the specified mission ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostMissionActions() # PostMissionActions | The details of the mission_actions
mission_id = 'mission_id_example' # str | The mission_id to add the new resource to
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new action to the mission with the specified mission ID
    api_response = api_instance.missions_mission_id_actions_post(body, mission_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->missions_mission_id_actions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostMissionActions**](PostMissionActions.md)| The details of the mission_actions | 
 **mission_id** | **str**| The mission_id to add the new resource to | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMissionActions**](GetMissionActions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missions_post**
> GetMissions missions_post(body, accept_language=accept_language)

Add a new mission

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostMissions() # PostMissions | The details of the missions
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new mission
    api_response = api_instance.missions_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->missions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostMissions**](PostMissions.md)| The details of the missions | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMissions**](GetMissions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_get**
> GetModbus modbus_get(accept_language=accept_language)

Retrieve the modbus registers linked to actions

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the modbus registers linked to actions
    api_response = api_instance.modbus_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->modbus_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetModbus**](GetModbus.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_id_get**
> GetModbu modbus_id_get(id, accept_language=accept_language)

Retrieve the modbus registers linked to an action

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
id = 'id_example' # str | The id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the modbus registers linked to an action
    api_response = api_instance.modbus_id_get(id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->modbus_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetModbu**](GetModbu.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_missions_get**
> list[GetModbusMissions] modbus_missions_get(accept_language=accept_language)

Retrieve the list of coils that can trigger a mission

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of coils that can trigger a mission
    api_response = api_instance.modbus_missions_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->modbus_missions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetModbusMissions]**](GetModbusMissions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_missions_guid_delete**
> modbus_missions_guid_delete(guid, accept_language=accept_language)

Delete the specified ID on the the modbus mission table

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Delete the specified ID on the the modbus mission table
    api_instance.modbus_missions_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->modbus_missions_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_missions_guid_get**
> GetModbusMission modbus_missions_guid_get(guid, accept_language=accept_language)

Retrieve the details about the mission linked with the coil

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the mission linked with the coil
    api_response = api_instance.modbus_missions_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->modbus_missions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetModbusMission**](GetModbusMission.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_missions_guid_put**
> GetModbusMission modbus_missions_guid_put(body, guid, accept_language=accept_language)

Modify the values of the modbus mission with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutModbusMission() # PutModbusMission | The new values of the modbus_mission
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the modbus mission with the specified ID
    api_response = api_instance.modbus_missions_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->modbus_missions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutModbusMission**](PutModbusMission.md)| The new values of the modbus_mission | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetModbusMission**](GetModbusMission.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modbus_missions_post**
> GetModbusMissions modbus_missions_post(body, accept_language=accept_language)

Create a new link between a coil and a mission

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostModbusMissions() # PostModbusMissions | The details of the modbus_missions
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Create a new link between a coil and a mission
    api_response = api_instance.modbus_missions_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->modbus_missions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostModbusMissions**](PostModbusMissions.md)| The details of the modbus_missions | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetModbusMissions**](GetModbusMissions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_get**
> list[GetPathGuides] path_guides_get(accept_language=accept_language)

Retrieve the list of path guides

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of path guides
    api_response = api_instance.path_guides_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetPathGuides]**](GetPathGuides.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_guid_delete**
> path_guides_guid_delete(guid, accept_language=accept_language)

Erase the path guide with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the path guide with the specified GUID
    api_instance.path_guides_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_guid_get**
> GetPathGuide path_guides_guid_get(guid, accept_language=accept_language)

Retrieve the path guide with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the path guide with the specified GUID
    api_response = api_instance.path_guides_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPathGuide**](GetPathGuide.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_guid_put**
> GetPathGuide path_guides_guid_put(body, guid, accept_language=accept_language)

Modify the values of the path guide with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutPathGuide() # PutPathGuide | The new values of the path_guide
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the path guide with the specified GUID
    api_response = api_instance.path_guides_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutPathGuide**](PutPathGuide.md)| The new values of the path_guide | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPathGuide**](GetPathGuide.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_path_guide_guid_options_get**
> GetPathGuideOptions path_guides_path_guide_guid_options_get(path_guide_guid, accept_language=accept_language)

Retrieve the list of allowed start/via/goal options for the selected path guide

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of allowed start/via/goal options for the selected path guide
    api_response = api_instance.path_guides_path_guide_guid_options_get(path_guide_guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_path_guide_guid_options_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_guide_guid** | **str**| The path_guide_guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPathGuideOptions**](GetPathGuideOptions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_path_guide_guid_positions_get**
> list[GetPathGuidePositions] path_guides_path_guide_guid_positions_get(path_guide_guid, accept_language=accept_language)

Retrieve the list of positions for the path guide with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of positions for the path guide with the specified GUID
    api_response = api_instance.path_guides_path_guide_guid_positions_get(path_guide_guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_path_guide_guid_positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path_guide_guid** | **str**| The path_guide_guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetPathGuidePositions]**](GetPathGuidePositions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_path_guide_guid_positions_guid_delete**
> path_guides_path_guide_guid_positions_guid_delete(guid, path_guide_guid, accept_language=accept_language)

Erase the position with the specified GUID from the path guide with the specified path guide GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the position with the specified GUID from the path guide with the specified path guide GUID
    api_instance.path_guides_path_guide_guid_positions_guid_delete(guid, path_guide_guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_path_guide_guid_positions_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **path_guide_guid** | **str**| The path_guide_guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_path_guide_guid_positions_guid_get**
> GetPathGuidePosition path_guides_path_guide_guid_positions_guid_get(guid, path_guide_guid, accept_language=accept_language)

Retrieve the position with the specified GUID from the path guide with the specified path guide GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the position with the specified GUID from the path guide with the specified path guide GUID
    api_response = api_instance.path_guides_path_guide_guid_positions_guid_get(guid, path_guide_guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_path_guide_guid_positions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **path_guide_guid** | **str**| The path_guide_guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPathGuidePosition**](GetPathGuidePosition.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_path_guide_guid_positions_guid_put**
> GetPathGuidePosition path_guides_path_guide_guid_positions_guid_put(body, guid, path_guide_guid, accept_language=accept_language)

Modify the values of the position with the specified GUID from the path guide with the specified path guide GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutPathGuidePosition() # PutPathGuidePosition | The new values of the path_guide_position
guid = 'guid_example' # str | The guid to modify
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the position with the specified GUID from the path guide with the specified path guide GUID
    api_response = api_instance.path_guides_path_guide_guid_positions_guid_put(body, guid, path_guide_guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_path_guide_guid_positions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutPathGuidePosition**](PutPathGuidePosition.md)| The new values of the path_guide_position | 
 **guid** | **str**| The guid to modify | 
 **path_guide_guid** | **str**| The path_guide_guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPathGuidePosition**](GetPathGuidePosition.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_path_guide_guid_positions_post**
> GetPathGuidePositions path_guides_path_guide_guid_positions_post(body, path_guide_guid, accept_language=accept_language)

Add a new position to the path guide with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostPathGuidePositions() # PostPathGuidePositions | The details of the path_guide_positions
path_guide_guid = 'path_guide_guid_example' # str | The path_guide_guid to add the new resource to
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new position to the path guide with the specified GUID
    api_response = api_instance.path_guides_path_guide_guid_positions_post(body, path_guide_guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_path_guide_guid_positions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostPathGuidePositions**](PostPathGuidePositions.md)| The details of the path_guide_positions | 
 **path_guide_guid** | **str**| The path_guide_guid to add the new resource to | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPathGuidePositions**](GetPathGuidePositions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_positions_get**
> list[GetPathGuidesPositions] path_guides_positions_get(accept_language=accept_language)

Retrieve the list of positions used for path guides

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of positions used for path guides
    api_response = api_instance.path_guides_positions_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetPathGuidesPositions]**](GetPathGuidesPositions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_positions_guid_delete**
> path_guides_positions_guid_delete(guid, accept_language=accept_language)

Erase the path guide position with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the path guide position with the specified GUID
    api_instance.path_guides_positions_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_positions_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_positions_guid_get**
> GetPathGuidesPosition path_guides_positions_guid_get(guid, accept_language=accept_language)

Retrieve the position for path guides with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the position for path guides with the specified GUID
    api_response = api_instance.path_guides_positions_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_positions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPathGuidesPosition**](GetPathGuidesPosition.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_positions_guid_put**
> GetPathGuidesPosition path_guides_positions_guid_put(body, guid, accept_language=accept_language)

Modify the values of the position for path guides with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutPathGuidesPosition() # PutPathGuidesPosition | The new values of the path_guides_position
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the position for path guides with the specified GUID
    api_response = api_instance.path_guides_positions_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_positions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutPathGuidesPosition**](PutPathGuidesPosition.md)| The new values of the path_guides_position | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPathGuidesPosition**](GetPathGuidesPosition.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_positions_post**
> GetPathGuidesPositions path_guides_positions_post(body, accept_language=accept_language)

Add a new position in a path guide

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostPathGuidesPositions() # PostPathGuidesPositions | The details of the path_guides_positions
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new position in a path guide
    api_response = api_instance.path_guides_positions_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_positions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostPathGuidesPositions**](PostPathGuidesPositions.md)| The details of the path_guides_positions | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPathGuidesPositions**](GetPathGuidesPositions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_post**
> GetPathGuides path_guides_post(body, accept_language=accept_language)

Add a new path guide

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostPathGuides() # PostPathGuides | The details of the path_guides
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new path guide
    api_response = api_instance.path_guides_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostPathGuides**](PostPathGuides.md)| The details of the path_guides | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPathGuides**](GetPathGuides.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_precalc_get**
> GetPathGuidesPrecalc path_guides_precalc_get(accept_language=accept_language)

Retrieve the status of path guides precalculation

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the status of path guides precalculation
    api_response = api_instance.path_guides_precalc_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_precalc_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPathGuidesPrecalc**](GetPathGuidesPrecalc.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **path_guides_precalc_post**
> GetPathGuidesPrecalc path_guides_precalc_post(body, accept_language=accept_language)

Start/stop precalculation of the specified path guide

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostPathGuidesPrecalc() # PostPathGuidesPrecalc | The details of the path_guides_precalc
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Start/stop precalculation of the specified path guide
    api_response = api_instance.path_guides_precalc_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->path_guides_precalc_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostPathGuidesPrecalc**](PostPathGuidesPrecalc.md)| The details of the path_guides_precalc | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPathGuidesPrecalc**](GetPathGuidesPrecalc.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paths_get**
> list[GetPaths] paths_get(accept_language=accept_language)

Retrieve the list of paths

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of paths
    api_response = api_instance.paths_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->paths_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetPaths]**](GetPaths.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paths_guid_delete**
> paths_guid_delete(guid, accept_language=accept_language)

Erase the path with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the path with the specified GUID
    api_instance.paths_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->paths_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paths_guid_get**
> GetPath paths_guid_get(guid, accept_language=accept_language)

Retrieve the path with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the path with the specified GUID
    api_response = api_instance.paths_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->paths_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPath**](GetPath.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paths_guid_put**
> GetPath paths_guid_put(body, guid, accept_language=accept_language)

Modify the values of the path with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutPath() # PutPath | The new values of the path
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the path with the specified GUID
    api_response = api_instance.paths_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->paths_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutPath**](PutPath.md)| The new values of the path | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPath**](GetPath.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paths_post**
> GetPaths paths_post(body, accept_language=accept_language)

Add a new path

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostPaths() # PostPaths | The details of the paths
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new path
    api_response = api_instance.paths_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->paths_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostPaths**](PostPaths.md)| The details of the paths | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPaths**](GetPaths.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_guid_delete**
> permissions_guid_delete(guid, accept_language=accept_language)

Erase the permission with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the permission with the specified GUID
    api_instance.permissions_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->permissions_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_guid_get**
> GetPermission permissions_guid_get(guid, accept_language=accept_language)

Retrieve the details about the permission with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the permission with the specified GUID
    api_response = api_instance.permissions_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->permissions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPermission**](GetPermission.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_guid_put**
> GetPermission permissions_guid_put(guid, accept_language=accept_language)

Modify the values of the permission with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the permission with the specified GUID
    api_response = api_instance.permissions_guid_put(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->permissions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPermission**](GetPermission.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_transition_lists_get**
> GetPositionTransitionLists position_transition_lists_get(accept_language=accept_language)

Retrieve the list of position transition lists

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of position transition lists
    api_response = api_instance.position_transition_lists_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->position_transition_lists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPositionTransitionLists**](GetPositionTransitionLists.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_transition_lists_guid_delete**
> position_transition_lists_guid_delete(guid, accept_language=accept_language)

Erase the position transition list with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the position transition list with the specified GUID
    api_instance.position_transition_lists_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->position_transition_lists_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_transition_lists_guid_get**
> GetPositionTransitionList position_transition_lists_guid_get(guid, accept_language=accept_language)

Retrieve the details about the position transition list with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the position transition list with the specified GUID
    api_response = api_instance.position_transition_lists_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->position_transition_lists_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPositionTransitionList**](GetPositionTransitionList.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_transition_lists_guid_put**
> GetPositionTransitionList position_transition_lists_guid_put(body, guid, accept_language=accept_language)

Modify the values of the position transition list with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutPositionTransitionList() # PutPositionTransitionList | The new values of the position_transition_list
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the position transition list with the specified GUID
    api_response = api_instance.position_transition_lists_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->position_transition_lists_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutPositionTransitionList**](PutPositionTransitionList.md)| The new values of the position_transition_list | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPositionTransitionList**](GetPositionTransitionList.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_transition_lists_post**
> GetPositionTransitionLists position_transition_lists_post(body, accept_language=accept_language)

Add a new position transition list

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostPositionTransitionLists() # PostPositionTransitionLists | The details of the position_transition_lists
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new position transition list
    api_response = api_instance.position_transition_lists_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->position_transition_lists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostPositionTransitionLists**](PostPositionTransitionLists.md)| The details of the position_transition_lists | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPositionTransitionLists**](GetPositionTransitionLists.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_types_get**
> list[GetPositionTypes] position_types_get(accept_language=accept_language)

Retrieve a list of possible position types

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve a list of possible position types
    api_response = api_instance.position_types_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->position_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetPositionTypes]**](GetPositionTypes.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_types_id_get**
> GetPositionType position_types_id_get(id, accept_language=accept_language)

Retrieve the details about the position type with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
id = 56 # int | The id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the position type with the specified ID
    api_response = api_instance.position_types_id_get(id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->position_types_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPositionType**](GetPositionType.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_get**
> list[GetPositions] positions_get(accept_language=accept_language)

Retrieve the list of positions

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of positions
    api_response = api_instance.positions_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetPositions]**](GetPositions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_guid_delete**
> positions_guid_delete(guid, accept_language=accept_language)

Erase the position with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the position with the specified GUID
    api_instance.positions_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->positions_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_guid_get**
> GetPosition positions_guid_get(guid, accept_language=accept_language)

Retrieve the details about the position with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the position with the specified GUID
    api_response = api_instance.positions_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->positions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPosition**](GetPosition.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_guid_put**
> GetPosition positions_guid_put(body, guid, accept_language=accept_language)

Modify the values of the position with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutPosition() # PutPosition | The new values of the position
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the position with the specified GUID
    api_response = api_instance.positions_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->positions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutPosition**](PutPosition.md)| The new values of the position | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPosition**](GetPosition.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_parent_guid_helper_positions_get**
> list[GetHelperPositions] positions_parent_guid_helper_positions_get(parent_guid, accept_language=accept_language)

Retrieve the list of helper positions for the position with the specified parent GUID. Only Charging Stations, V markers, VL markers, Shelf and Trolley positions have helper positions

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
parent_guid = 'parent_guid_example' # str | The parent_guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of helper positions for the position with the specified parent GUID. Only Charging Stations, V markers, VL markers, Shelf and Trolley positions have helper positions
    api_response = api_instance.positions_parent_guid_helper_positions_get(parent_guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->positions_parent_guid_helper_positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_guid** | **str**| The parent_guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetHelperPositions]**](GetHelperPositions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_pos_id_docking_offsets_get**
> list[GetPosDockingOffsets] positions_pos_id_docking_offsets_get(pos_id, accept_language=accept_language)

Retrieve the details of the docking offset of the position with the specified position ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
pos_id = 'pos_id_example' # str | The pos_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details of the docking offset of the position with the specified position ID
    api_response = api_instance.positions_pos_id_docking_offsets_get(pos_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->positions_pos_id_docking_offsets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pos_id** | **str**| The pos_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetPosDockingOffsets]**](GetPosDockingOffsets.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **positions_post**
> GetPositions positions_post(body, accept_language=accept_language)

Add a new position

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostPositions() # PostPositions | The details of the positions
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new position
    api_response = api_instance.positions_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->positions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostPositions**](PostPositions.md)| The details of the positions | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPositions**](GetPositions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registers_get**
> list[GetRegisters] registers_get(accept_language=accept_language)

Retrieve the list of PLC registers from the robot. Registers 1 to 100 are integers and registers 101-200 are float

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of PLC registers from the robot. Registers 1 to 100 are integers and registers 101-200 are float
    api_response = api_instance.registers_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->registers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetRegisters]**](GetRegisters.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registers_id_get**
> GetRegister registers_id_get(id, accept_language=accept_language)

Retrieve the value of the PLC register with the specified ID. Registers 1 to 100 are integers and registers 101-200 are float

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
id = 56 # int | The id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the value of the PLC register with the specified ID. Registers 1 to 100 are integers and registers 101-200 are float
    api_response = api_instance.registers_id_get(id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->registers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetRegister**](GetRegister.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registers_id_post**
> GetRegister registers_id_post(body, id, accept_language=accept_language)

Modify the value of the PLC register with the specified ID. Registers 1 to 100 are integers and registers 101-200 are float. Even though this is not a standard use of the POST call it has been included for compatibility purposes

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostRegister() # PostRegister | The details of the register
id = 56 # int | The id to add the new resource to
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the value of the PLC register with the specified ID. Registers 1 to 100 are integers and registers 101-200 are float. Even though this is not a standard use of the POST call it has been included for compatibility purposes
    api_response = api_instance.registers_id_post(body, id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->registers_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostRegister**](PostRegister.md)| The details of the register | 
 **id** | **int**| The id to add the new resource to | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetRegister**](GetRegister.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registers_id_put**
> GetRegister registers_id_put(body, id, accept_language=accept_language)

Modify the value of the PLC register with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutRegister() # PutRegister | The new values of the register
id = 56 # int | The id to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the value of the PLC register with the specified ID
    api_response = api_instance.registers_id_put(body, id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->registers_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutRegister**](PutRegister.md)| The new values of the register | 
 **id** | **int**| The id to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetRegister**](GetRegister.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_support_get**
> GetRemoteSupport remote_support_get(accept_language=accept_language)

Retrieve the status of the remote support connection

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the status of the remote support connection
    api_response = api_instance.remote_support_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->remote_support_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetRemoteSupport**](GetRemoteSupport.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_support_log_get**
> GetRemoteSupportLog remote_support_log_get(accept_language=accept_language)

Retrieve the list with the actions performed by the remote support controller

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list with the actions performed by the remote support controller
    api_response = api_instance.remote_support_log_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->remote_support_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetRemoteSupportLog**](GetRemoteSupportLog.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_support_put**
> GetRemoteSupport remote_support_put(body, accept_language=accept_language)

Modify the remote support connection timeout

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutRemoteSupport() # PutRemoteSupport | The new values of the remote_support
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the remote support connection timeout
    api_response = api_instance.remote_support_put(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->remote_support_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutRemoteSupport**](PutRemoteSupport.md)| The new values of the remote_support | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetRemoteSupport**](GetRemoteSupport.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **robots_post**
> GetRobots robots_post(body, accept_language=accept_language)

Add information about other robots in the world. This is used by the Fleet manager to avoid robot collisions

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostRobots() # PostRobots | The details of the robots
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add information about other robots in the world. This is used by the Fleet manager to avoid robot collisions
    api_response = api_instance.robots_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->robots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostRobots**](PostRobots.md)| The details of the robots | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetRobots**](GetRobots.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_book_get**
> GetServiceBooks service_book_get(accept_language=accept_language)

Retrieve service book entries accessible by user

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve service book entries accessible by user
    api_response = api_instance.service_book_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->service_book_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetServiceBooks**](GetServiceBooks.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_book_guid_delete**
> service_book_guid_delete(guid, accept_language=accept_language)

Erase the note with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the note with the specified GUID
    api_instance.service_book_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->service_book_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_book_guid_get**
> GetServiceBook service_book_guid_get(guid, accept_language=accept_language)

Retrieve note with the GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve note with the GUID
    api_response = api_instance.service_book_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->service_book_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetServiceBook**](GetServiceBook.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_book_post**
> GetServiceBooks service_book_post(body, accept_language=accept_language)

Add a service book note

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostServiceBooks() # PostServiceBooks | The details of the service_books
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a service book note
    api_response = api_instance.service_book_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->service_book_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostServiceBooks**](PostServiceBooks.md)| The details of the service_books | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetServiceBooks**](GetServiceBooks.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_get**
> list[GetSessions] sessions_get(accept_language=accept_language)

Retrieve the list of sessions

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of sessions
    api_response = api_instance.sessions_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sessions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSessions]**](GetSessions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_guid_delete**
> sessions_guid_delete(guid, accept_language=accept_language)

Erase the session with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the session with the specified GUID
    api_instance.sessions_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->sessions_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_guid_export_get**
> GetSessionExport sessions_guid_export_get(guid, accept_language=accept_language)

Download a file containing the session with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Download a file containing the session with the specified GUID
    api_response = api_instance.sessions_guid_export_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sessions_guid_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSessionExport**](GetSessionExport.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_guid_get**
> GetSession sessions_guid_get(guid, accept_language=accept_language)

Retrieve the details about the session with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the session with the specified GUID
    api_response = api_instance.sessions_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sessions_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSession**](GetSession.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_guid_put**
> GetSession sessions_guid_put(body, guid, accept_language=accept_language)

Modify the values of the session with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutSession() # PutSession | The new values of the session
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the session with the specified GUID
    api_response = api_instance.sessions_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sessions_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSession**](PutSession.md)| The new values of the session | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSession**](GetSession.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_import_delete**
> sessions_import_delete(accept_language=accept_language)

Cancel currently running import

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Cancel currently running import
    api_instance.sessions_import_delete(accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->sessions_import_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_import_get**
> GetSessionImport sessions_import_get(accept_language=accept_language)

Get progress of the running import

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Get progress of the running import
    api_response = api_instance.sessions_import_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sessions_import_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSessionImport**](GetSessionImport.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_import_post**
> GetSessionImport sessions_import_post(body, accept_language=accept_language)

Import the session contained in the file

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostSessionImport() # PostSessionImport | The details of the session_import
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Import the session contained in the file
    api_response = api_instance.sessions_import_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sessions_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSessionImport**](PostSessionImport.md)| The details of the session_import | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSessionImport**](GetSessionImport.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_post**
> GetSessions sessions_post(body, accept_language=accept_language)

Add a new session

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostSessions() # PostSessions | The details of the sessions
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new session
    api_response = api_instance.sessions_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sessions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSessions**](PostSessions.md)| The details of the sessions | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSessions**](GetSessions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_maps_get**
> list[GetSessionMaps] sessions_session_id_maps_get(session_id, accept_language=accept_language)

Retrieve the list of maps that belong to the session with the specified session ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
session_id = 'session_id_example' # str | The session_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of maps that belong to the session with the specified session ID
    api_response = api_instance.sessions_session_id_maps_get(session_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sessions_session_id_maps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSessionMaps]**](GetSessionMaps.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_missions_get**
> list[GetSessionMissions] sessions_session_id_missions_get(session_id, accept_language=accept_language)

Retrieve the list of missions that belong to the session with the specified session ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
session_id = 'session_id_example' # str | The session_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of missions that belong to the session with the specified session ID
    api_response = api_instance.sessions_session_id_missions_get(session_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sessions_session_id_missions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSessionMissions]**](GetSessionMissions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_position_transition_lists_get**
> GetPositionTransitionListFromSession sessions_session_id_position_transition_lists_get(session_id, accept_language=accept_language)

Retrieve the list of position transition lists that belong to the session with the specified session ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
session_id = 'session_id_example' # str | The session_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of position transition lists that belong to the session with the specified session ID
    api_response = api_instance.sessions_session_id_position_transition_lists_get(session_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sessions_session_id_position_transition_lists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The session_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetPositionTransitionListFromSession**](GetPositionTransitionListFromSession.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setting_groups_get**
> list[GetSettingGroups] setting_groups_get(accept_language=accept_language)

Retrieve a list with the settings groups

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve a list with the settings groups
    api_response = api_instance.setting_groups_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->setting_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSettingGroups]**](GetSettingGroups.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setting_groups_id_get**
> GetSettingGroup setting_groups_id_get(id, accept_language=accept_language)

Retrieve the details about the settings group with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
id = 'id_example' # str | The id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the settings group with the specified ID
    api_response = api_instance.setting_groups_id_get(id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->setting_groups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSettingGroup**](GetSettingGroup.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setting_groups_settings_group_id_settings_advanced_get**
> list[GetSettingGroupAdvancedSettings] setting_groups_settings_group_id_settings_advanced_get(settings_group_id, accept_language=accept_language)

Retrieve the list of advanced settings from the settings group with the specified settings group ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
settings_group_id = 56 # int | The settings_group_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of advanced settings from the settings group with the specified settings group ID
    api_response = api_instance.setting_groups_settings_group_id_settings_advanced_get(settings_group_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->setting_groups_settings_group_id_settings_advanced_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_group_id** | **int**| The settings_group_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSettingGroupAdvancedSettings]**](GetSettingGroupAdvancedSettings.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setting_groups_settings_group_id_settings_get**
> list[GetSettingGroupSettings] setting_groups_settings_group_id_settings_get(settings_group_id, accept_language=accept_language)

Retrieve the list of settings from the settings group with the specified settings group ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
settings_group_id = 56 # int | The settings_group_id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of settings from the settings group with the specified settings group ID
    api_response = api_instance.setting_groups_settings_group_id_settings_get(settings_group_id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->setting_groups_settings_group_id_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_group_id** | **int**| The settings_group_id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSettingGroupSettings]**](GetSettingGroupSettings.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_advanced_get**
> list[GetSettingsAdvanced] settings_advanced_get(accept_language=accept_language)

Retrieve the list with the advanced settings

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list with the advanced settings
    api_response = api_instance.settings_advanced_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settings_advanced_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSettingsAdvanced]**](GetSettingsAdvanced.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_advanced_id_get**
> GetSettingAdvanced settings_advanced_id_get(id, accept_language=accept_language)

Retrieve the details of the advanced setting with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
id = 'id_example' # str | The id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details of the advanced setting with the specified ID
    api_response = api_instance.settings_advanced_id_get(id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settings_advanced_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSettingAdvanced**](GetSettingAdvanced.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_advanced_id_put**
> GetSettingAdvanced settings_advanced_id_put(body, id, accept_language=accept_language)

Modify the values of the advanced setting with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutSettingAdvanced() # PutSettingAdvanced | The new values of the setting_advanced
id = 'id_example' # str | The id to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the advanced setting with the specified ID
    api_response = api_instance.settings_advanced_id_put(body, id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settings_advanced_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSettingAdvanced**](PutSettingAdvanced.md)| The new values of the setting_advanced | 
 **id** | **str**| The id to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSettingAdvanced**](GetSettingAdvanced.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_get**
> list[GetSettings] settings_get(accept_language=accept_language)

Retrieve a list with the settings

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve a list with the settings
    api_response = api_instance.settings_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSettings]**](GetSettings.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_id_get**
> GetSetting settings_id_get(id, accept_language=accept_language)

Retrieve the details of the setting with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
id = 'id_example' # str | The id to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details of the setting with the specified ID
    api_response = api_instance.settings_id_get(id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settings_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSetting**](GetSetting.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_id_put**
> GetSetting settings_id_put(body, id, accept_language=accept_language)

Modify the values of the setting with the specified ID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutSetting() # PutSetting | The new values of the setting
id = 'id_example' # str | The id to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the setting with the specified ID
    api_response = api_instance.settings_id_put(body, id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settings_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSetting**](PutSetting.md)| The new values of the setting | 
 **id** | **str**| The id to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSetting**](GetSetting.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shelf_types_get**
> list[GetShelfTypes] shelf_types_get(accept_language=accept_language)

Retrieve the list of shelf types

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of shelf types
    api_response = api_instance.shelf_types_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->shelf_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetShelfTypes]**](GetShelfTypes.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shelf_types_guid_delete**
> shelf_types_guid_delete(guid, accept_language=accept_language)

Erase the shelf type with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the shelf type with the specified GUID
    api_instance.shelf_types_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->shelf_types_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shelf_types_guid_get**
> GetShelfType shelf_types_guid_get(guid, accept_language=accept_language)

Retrieve the details about the shelf type with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the shelf type with the specified GUID
    api_response = api_instance.shelf_types_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->shelf_types_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetShelfType**](GetShelfType.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shelf_types_guid_put**
> GetShelfType shelf_types_guid_put(body, guid, accept_language=accept_language)

Modify the values of the shelf type with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutShelfType() # PutShelfType | The new values of the shelf_type
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the shelf type with the specified GUID
    api_response = api_instance.shelf_types_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->shelf_types_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutShelfType**](PutShelfType.md)| The new values of the shelf_type | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetShelfType**](GetShelfType.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shelf_types_post**
> GetShelfTypes shelf_types_post(body, accept_language=accept_language)

Add a new shelf type

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostShelfTypes() # PostShelfTypes | The details of the shelf_types
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new shelf type
    api_response = api_instance.shelf_types_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->shelf_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostShelfTypes**](PostShelfTypes.md)| The details of the shelf_types | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetShelfTypes**](GetShelfTypes.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_backups_get**
> list[GetSoftwareBackups] software_backups_get(accept_language=accept_language)

Retrieve the list with all the software backups

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list with all the software backups
    api_response = api_instance.software_backups_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->software_backups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSoftwareBackups]**](GetSoftwareBackups.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_backups_guid_delete**
> software_backups_guid_delete(guid, accept_language=accept_language)

Erase the software backup with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the software backup with the specified GUID
    api_instance.software_backups_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->software_backups_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_backups_guid_get**
> GetSoftwareBackup software_backups_guid_get(guid, accept_language=accept_language)

Retrieve the details about the software backup with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the software backup with the specified GUID
    api_response = api_instance.software_backups_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->software_backups_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSoftwareBackup**](GetSoftwareBackup.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_backups_guid_post**
> GetSoftwareBackup software_backups_guid_post(guid, accept_language=accept_language)

If it exists a software backup with the specified GUID it will restore that backup. Otherwise, it will create a software backup with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to add the new resource to
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # If it exists a software backup with the specified GUID it will restore that backup. Otherwise, it will create a software backup with the specified GUID
    api_response = api_instance.software_backups_guid_post(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->software_backups_guid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to add the new resource to | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSoftwareBackup**](GetSoftwareBackup.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_backups_post**
> GetSoftwareBackups software_backups_post(accept_language=accept_language)

Create a new software backup

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Create a new software backup
    api_response = api_instance.software_backups_post(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->software_backups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSoftwareBackups**](GetSoftwareBackups.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_lock_get**
> list[GetSoftwareLockSelf] software_lock_get(accept_language=accept_language)

Retrieve the status of the software lock

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the status of the software lock
    api_response = api_instance.software_lock_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->software_lock_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSoftwareLockSelf]**](GetSoftwareLockSelf.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_lock_put**
> GetSoftwareLockSelf software_lock_put(body, accept_language=accept_language)

Modify the software lock

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutSoftwareLockSelf() # PutSoftwareLockSelf | The new values of the software_lock_self
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the software lock
    api_response = api_instance.software_lock_put(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->software_lock_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSoftwareLockSelf**](PutSoftwareLockSelf.md)| The new values of the software_lock_self | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSoftwareLockSelf**](GetSoftwareLockSelf.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_logs_get**
> list[GetSoftwareLogs] software_logs_get(accept_language=accept_language)

Retrieve the list of software upgrade logs

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of software upgrade logs
    api_response = api_instance.software_logs_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->software_logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSoftwareLogs]**](GetSoftwareLogs.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_logs_guid_get**
> GetSoftwareLog software_logs_guid_get(guid, accept_language=accept_language)

Retrieve the details about the software upgrade log with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the software upgrade log with the specified GUID
    api_response = api_instance.software_logs_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->software_logs_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSoftwareLog**](GetSoftwareLog.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_upgrades_get**
> list[GetSoftwareUpgrades] software_upgrades_get(accept_language=accept_language)

Retrieve a list of the software upgrade performed

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve a list of the software upgrade performed
    api_response = api_instance.software_upgrades_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->software_upgrades_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSoftwareUpgrades]**](GetSoftwareUpgrades.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_upgrades_guid_delete**
> software_upgrades_guid_delete(guid, accept_language=accept_language)

Erase the upgrade file with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the upgrade file with the specified GUID
    api_instance.software_upgrades_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->software_upgrades_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_upgrades_guid_get**
> GetSoftwareUpgrade software_upgrades_guid_get(guid, accept_language=accept_language)

Retrieve the details of the software upgrade with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details of the software upgrade with the specified GUID
    api_response = api_instance.software_upgrades_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->software_upgrades_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSoftwareUpgrade**](GetSoftwareUpgrade.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_upgrades_guid_post**
> GetSoftwareUpgrade software_upgrades_guid_post(guid, accept_language=accept_language)

Upgrade to the version of the upgrade file with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to add the new resource to
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Upgrade to the version of the upgrade file with the specified GUID
    api_response = api_instance.software_upgrades_guid_post(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->software_upgrades_guid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to add the new resource to | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSoftwareUpgrade**](GetSoftwareUpgrade.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_upgrades_post**
> GetSoftwareUpgrades software_upgrades_post(accept_language=accept_language)

Upgrade with the provided upgrade file

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Upgrade with the provided upgrade file
    api_response = api_instance.software_upgrades_post(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->software_upgrades_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSoftwareUpgrades**](GetSoftwareUpgrades.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sounds_get**
> list[GetSounds] sounds_get(accept_language=accept_language)

Retrieve the list of sounds

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of sounds
    api_response = api_instance.sounds_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sounds_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSounds]**](GetSounds.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sounds_guid_delete**
> sounds_guid_delete(guid, accept_language=accept_language)

Erase the sound with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the sound with the specified GUID
    api_instance.sounds_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->sounds_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sounds_guid_get**
> GetSound sounds_guid_get(guid, accept_language=accept_language)

Retrieve the details about the sound with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the sound with the specified GUID
    api_response = api_instance.sounds_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sounds_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSound**](GetSound.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sounds_guid_put**
> GetSound sounds_guid_put(body, guid, accept_language=accept_language)

Modify the values of the sound with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutSound() # PutSound | The new values of the sound
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the sound with the specified GUID
    api_response = api_instance.sounds_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sounds_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutSound**](PutSound.md)| The new values of the sound | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSound**](GetSound.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sounds_guid_stream_get**
> list[GetSoundStream] sounds_guid_stream_get(guid, accept_language=accept_language)

Download the sound file of the sound with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Download the sound file of the sound with the specified GUID
    api_response = api_instance.sounds_guid_stream_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sounds_guid_stream_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetSoundStream]**](GetSoundStream.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sounds_post**
> GetSounds sounds_post(body, accept_language=accept_language)

Add a new sound

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostSounds() # PostSounds | The details of the sounds
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new sound
    api_response = api_instance.sounds_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sounds_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostSounds**](PostSounds.md)| The details of the sounds | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSounds**](GetSounds.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_distance_get**
> GetDistanceStatistics statistics_distance_get(accept_language=accept_language)

Retrieve the list with the distance driven by the robot at different dates and times

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list with the distance driven by the robot at different dates and times
    api_response = api_instance.statistics_distance_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->statistics_distance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetDistanceStatistics**](GetDistanceStatistics.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get**
> GetStatus status_get(accept_language=accept_language)

Retrieve the status

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the status
    api_response = api_instance.status_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetStatus**](GetStatus.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_put**
> GetStatus status_put(body, accept_language=accept_language)

Modify the status

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutStatus() # PutStatus | The new values of the status
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the status
    api_response = api_instance.status_put(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->status_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutStatus**](PutStatus.md)| The new values of the status | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetStatus**](GetStatus.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_info_get**
> GetSystemInfo system_info_get(accept_language=accept_language)

Retrieve the information about the system. It contains different information like serial numbers of hardware components, MAC addresses of network cards, etc…

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the information about the system. It contains different information like serial numbers of hardware components, MAC addresses of network cards, etc…
    api_response = api_instance.system_info_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->system_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetSystemInfo**](GetSystemInfo.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_get**
> list[GetUserGroups] user_groups_get(accept_language=accept_language)

Retrieve the list of user groups

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of user groups
    api_response = api_instance.user_groups_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->user_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetUserGroups]**](GetUserGroups.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_guid_delete**
> user_groups_guid_delete(guid, accept_language=accept_language)

Erase the user group with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the user group with the specified GUID
    api_instance.user_groups_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->user_groups_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_guid_get**
> GetUserGroup user_groups_guid_get(guid, accept_language=accept_language)

Retrieve the details about the user group with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the user group with the specified GUID
    api_response = api_instance.user_groups_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->user_groups_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetUserGroup**](GetUserGroup.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_guid_put**
> GetUserGroup user_groups_guid_put(body, guid, accept_language=accept_language)

Modify the values of the user group with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutUserGroup() # PutUserGroup | The new values of the user_group
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the user group with the specified GUID
    api_response = api_instance.user_groups_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->user_groups_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutUserGroup**](PutUserGroup.md)| The new values of the user_group | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetUserGroup**](GetUserGroup.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_post**
> GetUserGroups user_groups_post(body, accept_language=accept_language)

Add a new user group

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostUserGroups() # PostUserGroups | The details of the user_groups
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new user group
    api_response = api_instance.user_groups_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->user_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostUserGroups**](PostUserGroups.md)| The details of the user_groups | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetUserGroups**](GetUserGroups.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_user_group_guid_permissions_get**
> list[GetUserGroupPermission] user_groups_user_group_guid_permissions_get(user_group_guid, accept_language=accept_language)

Retrieve the list of permissions of the user group with the specified group GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
user_group_guid = 'user_group_guid_example' # str | The user_group_guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of permissions of the user group with the specified group GUID
    api_response = api_instance.user_groups_user_group_guid_permissions_get(user_group_guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->user_groups_user_group_guid_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_guid** | **str**| The user_group_guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetUserGroupPermission]**](GetUserGroupPermission.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_user_group_guid_permissions_post**
> GetUserGroupPermission user_groups_user_group_guid_permissions_post(body, user_group_guid, accept_language=accept_language)

Add a new permission to the group with the specified group GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostUserGroupPermission() # PostUserGroupPermission | The details of the user_group_permission
user_group_guid = 'user_group_guid_example' # str | The user_group_guid to add the new resource to
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new permission to the group with the specified group GUID
    api_response = api_instance.user_groups_user_group_guid_permissions_post(body, user_group_guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->user_groups_user_group_guid_permissions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostUserGroupPermission**](PostUserGroupPermission.md)| The details of the user_group_permission | 
 **user_group_guid** | **str**| The user_group_guid to add the new resource to | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetUserGroupPermission**](GetUserGroupPermission.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_auth_delete**
> users_auth_delete(accept_language=accept_language)

Logout user

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Logout user
    api_instance.users_auth_delete(accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->users_auth_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_auth_post**
> GetUsersAuth users_auth_post(body, accept_language=accept_language)

Login with user credentials

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostUsersAuth() # PostUsersAuth | The details of the users_auth
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Login with user credentials
    api_response = api_instance.users_auth_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_auth_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostUsersAuth**](PostUsersAuth.md)| The details of the users_auth | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetUsersAuth**](GetUsersAuth.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> list[GetUsers] users_get(accept_language=accept_language)

Retrieve the list of users

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of users
    api_response = api_instance.users_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetUsers]**](GetUsers.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_guid_delete**
> users_guid_delete(guid, accept_language=accept_language)

Erase the user with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the user with the specified GUID
    api_instance.users_guid_delete(guid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->users_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_guid_get**
> GetUser users_guid_get(guid, accept_language=accept_language)

Retrieve the details about the user with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the user with the specified GUID
    api_response = api_instance.users_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetUser**](GetUser.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_guid_put**
> GetUser users_guid_put(body, guid, accept_language=accept_language)

Modify the values of the user with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutUser() # PutUser | The new values of the user
guid = 'guid_example' # str | The guid to modify
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the user with the specified GUID
    api_response = api_instance.users_guid_put(body, guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_guid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutUser**](PutUser.md)| The new values of the user | 
 **guid** | **str**| The guid to modify | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetUser**](GetUser.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me_get**
> list[GetMe] users_me_get(accept_language=accept_language)

Retrieve the details about the user currently authorized in the API

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the user currently authorized in the API
    api_response = api_instance.users_me_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_me_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetMe]**](GetMe.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me_permissions_get**
> list[GetUserMePermissions] users_me_permissions_get(accept_language=accept_language)

Retrieve the permission of the user currently authorized in the API

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the permission of the user currently authorized in the API
    api_response = api_instance.users_me_permissions_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_me_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetUserMePermissions]**](GetUserMePermissions.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me_put**
> GetMe users_me_put(body, accept_language=accept_language)

Modify the values of the user currently authorized in the API

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PutMe() # PutMe | The new values of the me
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Modify the values of the user currently authorized in the API
    api_response = api_instance.users_me_put(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_me_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutMe**](PutMe.md)| The new values of the me | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetMe**](GetMe.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> GetUsers users_post(body, accept_language=accept_language)

Add a new user

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostUsers() # PostUsers | The details of the users
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new user
    api_response = api_instance.users_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostUsers**](PostUsers.md)| The details of the users | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetUsers**](GetUsers.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_connections_get**
> list[GetWifiConnections] wifi_connections_get(accept_language=accept_language)

Retrieve the list of WiFi networks already configured

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of WiFi networks already configured
    api_response = api_instance.wifi_connections_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wifi_connections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetWifiConnections]**](GetWifiConnections.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_connections_post**
> GetWifiConnections wifi_connections_post(body, accept_language=accept_language)

Add a new WiFi network configuration

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostWifiConnections() # PostWifiConnections | The details of the wifi_connections
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Add a new WiFi network configuration
    api_response = api_instance.wifi_connections_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wifi_connections_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostWifiConnections**](PostWifiConnections.md)| The details of the wifi_connections | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetWifiConnections**](GetWifiConnections.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_connections_uuid_delete**
> wifi_connections_uuid_delete(uuid, accept_language=accept_language)

Erase the WiFi network configuration with the specified UUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
uuid = 'uuid_example' # str | The uuid to delete
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Erase the WiFi network configuration with the specified UUID
    api_instance.wifi_connections_uuid_delete(uuid, accept_language=accept_language)
except ApiException as e:
    print("Exception when calling DefaultApi->wifi_connections_uuid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid to delete | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

void (empty response body)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_connections_uuid_get**
> GetWifiConnection wifi_connections_uuid_get(uuid, accept_language=accept_language)

Retrieve the details about the WiFi network configuration with the specified UUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
uuid = 'uuid_example' # str | The uuid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the WiFi network configuration with the specified UUID
    api_response = api_instance.wifi_connections_uuid_get(uuid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wifi_connections_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The uuid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetWifiConnection**](GetWifiConnection.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_connections_uuid_post**
> GetWifiConnection wifi_connections_uuid_post(body, uuid, accept_language=accept_language)

Connect to the network with the specified UUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostWifiConnection() # PostWifiConnection | The details of the wifi_connection
uuid = 'uuid_example' # str | The uuid to add the new resource to
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Connect to the network with the specified UUID
    api_response = api_instance.wifi_connections_uuid_post(body, uuid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wifi_connections_uuid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostWifiConnection**](PostWifiConnection.md)| The details of the wifi_connection | 
 **uuid** | **str**| The uuid to add the new resource to | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetWifiConnection**](GetWifiConnection.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_get**
> GetWifi wifi_get(accept_language=accept_language)

Retrieve the URLs to the 3 WiFi related endpoints

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the URLs to the 3 WiFi related endpoints
    api_response = api_instance.wifi_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wifi_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetWifi**](GetWifi.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_networks_get**
> list[GetWifiNetworks] wifi_networks_get(accept_language=accept_language)

Retrieve the list of WiFi networks available for the robot to connect

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the list of WiFi networks available for the robot to connect
    api_response = api_instance.wifi_networks_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wifi_networks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**list[GetWifiNetworks]**](GetWifiNetworks.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wifi_networks_guid_get**
> GetWifiNetwork wifi_networks_guid_get(guid, accept_language=accept_language)

Retrieve the details about the WiFi network with the specified GUID

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
guid = 'guid_example' # str | The guid to search for
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the details about the WiFi network with the specified GUID
    api_response = api_instance.wifi_networks_guid_get(guid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wifi_networks_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The guid to search for | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetWifiNetwork**](GetWifiNetwork.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **world_model_get**
> GetWorldModel world_model_get(accept_language=accept_language)

Retrieve the information about the needed resources from the robot

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Retrieve the information about the needed resources from the robot
    api_response = api_instance.world_model_get(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->world_model_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetWorldModel**](GetWorldModel.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **world_model_post**
> GetWorldModel world_model_post(body, accept_language=accept_language)

Upload the world model with the existing robots, resources and positions and their respective locks

### Example
```python
from __future__ import print_function
import time
import mir100_client
from mir100_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: mir
configuration = mir100_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mir100_client.DefaultApi(mir100_client.ApiClient(configuration))
body = mir100_client.PostWorldModel() # PostWorldModel | The details of the world_model
accept_language = 'accept_language_example' # str | Language header (optional)

try:
    # Upload the world model with the existing robots, resources and positions and their respective locks
    api_response = api_instance.world_model_post(body, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->world_model_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostWorldModel**](PostWorldModel.md)| The details of the world_model | 
 **accept_language** | **str**| Language header | [optional] 

### Return type

[**GetWorldModel**](GetWorldModel.md)

### Authorization

[mir](../README.md#mir)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

