[comment]: # "Auto-generated SOAR connector documentation"
# Code42

Publisher: Splunk  
Connector Version: 2\.0\.1  
Product Vendor: Code42  
Product Name: Code42  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

This app integrates with Code42 to execute various investigate, correct, generic, and containment actions

[comment]: # ""
[comment]: # "    File: readme.md"
[comment]: # "    Copyright (c) 2018-2021 Splunk Inc."
[comment]: # "    "
[comment]: # "    Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)"
[comment]: # ""
## Playbook Backward Compatibility

-   The below-mentioned actions have been added. Hence, it is requested to the end-user to please
    update their existing playbooks by inserting \| modifying \| deleting the corresponding action
    blocks for this action on the earlier versions of the app.

      

    -   get organization info
    -   add departing employee
    -   remove departing employee

-   The existing action parameters have been modified in the actions given below. Hence, it is
    requested to the end-user to please update their existing playbooks by re-inserting the
    corresponding action blocks or by providing appropriate values to these action parameters to
    ensure the correct functioning of the playbooks created on the earlier versions of the app.

      

    -   run query - The new "max_results" parameter has been added.
    -   hunt file - The new "max_results" parameter has been added.


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Code42 asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**server\_url** |  required  | string | Server URL \(e\.g\. https\://example\.code42\.com\)
**place\_holder** |  optional  | ph | Placeholder
**username** |  required  | string | Username
**password** |  required  | password | Password

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using the supplied configuration  
[list users](#action-list-users) - List all users  
[unblock device](#action-unblock-device) - Unblock a device  
[block device](#action-block-device) - Block a device  
[deactivate device](#action-deactivate-device) - Deactivate a device  
[activate device](#action-activate-device) - Activate a device  
[deauthorize device](#action-deauthorize-device) - Deauthorize a device  
[activate user](#action-activate-user) - Activate a user  
[deactivate user](#action-deactivate-user) - Deactivate a user  
[list devices](#action-list-devices) - List all devices  
[change organization](#action-change-organization) - Move a user to a specific organization  
[list organizations](#action-list-organizations) - List all organizations  
[lock device](#action-lock-device) - Invoke an access lock on a specified device  
[unlock device](#action-unlock-device) - Deactivate an access lock on a specified device  
[get device](#action-get-device) - Get information for a specific device  
[push restore](#action-push-restore) - Push a restore on a device  
[check restore status](#action-check-restore-status) - Check the status of a restore on a device  
[get user](#action-get-user) - Retrieves information for a specific user  
[hunt file](#action-hunt-file) - Hunt file on a forensic search  
[run query](#action-run-query) - Run query on a forensic search  
[get organization info](#action-get-organization-info) - Retrieve Code42 organization info using the v3\_user\_token for the given username & password  
[add departing employee](#action-add-departing-employee) - Add Departing Employee to Code42 Organization  
[remove departing employee](#action-remove-departing-employee) - Remove departing employee from the departing employee list  

## action: 'test connectivity'
Validate the asset configuration for connectivity using the supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'list users'
List all users

Type: **investigate**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data\.\*\.active | boolean | 
action\_result\.data\.\*\.blocked | boolean | 
action\_result\.data\.\*\.creationDate | string | 
action\_result\.data\.\*\.email | string |  `email` 
action\_result\.data\.\*\.emailPromo | boolean | 
action\_result\.data\.\*\.firstName | string | 
action\_result\.data\.\*\.invited | boolean | 
action\_result\.data\.\*\.lastName | string | 
action\_result\.data\.\*\.licenses | string | 
action\_result\.data\.\*\.localAuthenticationOnly | boolean | 
action\_result\.data\.\*\.modificationDate | string | 
action\_result\.data\.\*\.notes | string | 
action\_result\.data\.\*\.orgId | numeric |  `code42 org id` 
action\_result\.data\.\*\.orgName | string |  `code42 org name` 
action\_result\.data\.\*\.orgType | string | 
action\_result\.data\.\*\.orgUid | string | 
action\_result\.data\.\*\.passwordReset | boolean | 
action\_result\.data\.\*\.quotaInBytes | numeric | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.userExtRef | string | 
action\_result\.data\.\*\.userId | numeric |  `code42 user id` 
action\_result\.data\.\*\.userUid | string | 
action\_result\.data\.\*\.username | string |  `user name` 
action\_result\.data\.\*\.usernameIsAnEmail | boolean | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.total\_users | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'unblock device'
Unblock a device

Type: **correct**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**device\_id** |  required  | ID of the device to unblock | numeric |  `code42 device id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.device\_id | numeric |  `code42 device id` 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'block device'
Block a device

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**device\_id** |  required  | ID of the device to block | numeric |  `code42 device id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.device\_id | numeric |  `code42 device id` 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'deactivate device'
Deactivate a device

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**device\_id** |  required  | ID of the device to deactivate | numeric |  `code42 device id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.device\_id | numeric |  `code42 device id` 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'activate device'
Activate a device

Type: **correct**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**device\_id** |  required  | ID of the device to activate | numeric |  `code42 device id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.device\_id | numeric |  `code42 device id` 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'deauthorize device'
Deauthorize a device

Type: **contain**  
Read only: **False**

The current user is signed out of the Code42 app\. The Code42 service stops backing up, and users cannot access the Code42 app to restore data or change settings without signing in again\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**device\_id** |  required  | ID of the device to deauthorize | numeric |  `code42 device id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.device\_id | numeric |  `code42 device id` 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'activate user'
Activate a user

Type: **correct**  
Read only: **False**

For the 'unblock\_user' true value the user status will be changed to 'Activated' and 'Unblocked' and for the false value, the user status will only be changed to 'Activated'\. <b>Note\:</b> If the user is already active then it will ignore the 'unblock\_user' parameter\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**user** |  required  | ID or Username of the user to activate | string |  `code42 user id`  `user name` 
**unblock\_user** |  optional  | Unblock the user upon activation \(Default\: false\) | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.unblock\_user | boolean | 
action\_result\.parameter\.user | string |  `code42 user id`  `user name` 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'deactivate user'
Deactivate a user

Type: **contain**  
Read only: **False**

For the 'block\_user' true value the user status will be changed to 'Deactivated' and 'Blocked' and for the false value, the user status will only be changed to 'Deactivated'\. <b>Note\:</b> If the user is already deactive then it will ignore the 'block\_user' parameter\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**user** |  required  | ID or Username of the user to deactivate | string |  `code42 user id`  `user name` 
**block\_user** |  optional  | Block the user upon deactivation \(Default\: false\) | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.block\_user | boolean | 
action\_result\.parameter\.user | string |  `code42 user id`  `user name` 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list devices'
List all devices

Type: **investigate**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data\.\*\.osHostname | string |  `host name` 
action\_result\.data\.\*\.active | boolean | 
action\_result\.data\.\*\.address | string | 
action\_result\.data\.\*\.alertState | numeric | 
action\_result\.data\.\*\.alertStates | string | 
action\_result\.data\.\*\.blocked | boolean | 
action\_result\.data\.\*\.buildVersion | numeric | 
action\_result\.data\.\*\.computerExtRef | string | 
action\_result\.data\.\*\.computerId | numeric |  `code42 device id` 
action\_result\.data\.\*\.creationDate | string | 
action\_result\.data\.\*\.guid | string |  `code42 device guid` 
action\_result\.data\.\*\.javaVersion | string | 
action\_result\.data\.\*\.lastConnected | string | 
action\_result\.data\.\*\.loginDate | string | 
action\_result\.data\.\*\.modelInfo | string | 
action\_result\.data\.\*\.modificationDate | string | 
action\_result\.data\.\*\.name | string |  `host name` 
action\_result\.data\.\*\.notes | string | 
action\_result\.data\.\*\.orgId | numeric |  `code42 org id` 
action\_result\.data\.\*\.orgUid | string | 
action\_result\.data\.\*\.osArch | string | 
action\_result\.data\.\*\.osName | string | 
action\_result\.data\.\*\.osVersion | string | 
action\_result\.data\.\*\.parentComputerGuid | string | 
action\_result\.data\.\*\.parentComputerId | numeric |  `code42 device id` 
action\_result\.data\.\*\.productVersion | string | 
action\_result\.data\.\*\.remoteAddress | string |  `ip` 
action\_result\.data\.\*\.service | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.timeZone | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.userId | numeric |  `code42 user id` 
action\_result\.data\.\*\.userUid | string | 
action\_result\.data\.\*\.version | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.total\_devices | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'change organization'
Move a user to a specific organization

Type: **generic**  
Read only: **False**

<b>Note\:</b> For the similar value of organization ID and name, organization ID will be considered upon name value\. For instance, if the ID is 8062 and the organization name is also 8062 then action will be executed upon ID value\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**organization** |  required  | ID or Name of the organization | string |  `code42 org id`  `code42 org name` 
**user** |  required  | ID or Username of the user to move | string |  `code42 user id`  `user name` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.organization | string |  `code42 org id`  `code42 org name` 
action\_result\.parameter\.user | string |  `code42 user id`  `user name` 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list organizations'
List all organizations

Type: **investigate**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data\.\*\.active | boolean | 
action\_result\.data\.\*\.alertCounts\.backupCriticalCount | numeric | 
action\_result\.data\.\*\.alertCounts\.backupWarningCount | numeric | 
action\_result\.data\.\*\.alertCounts\.destinations\.72\.backupCriticalCount | numeric | 
action\_result\.data\.\*\.alertCounts\.destinations\.72\.backupWarningCount | numeric | 
action\_result\.data\.\*\.archiveSizes\.\*\.archiveSize | numeric | 
action\_result\.data\.\*\.archiveSizes\.\*\.targetComputerGuid | string | 
action\_result\.data\.\*\.backupComputerCount | numeric | 
action\_result\.data\.\*\.backupDeviceCount | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.archiveBytes | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.archiveBytesDeltaMonth | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.backupSessionCount | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.billableBytes | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.selectedBytes | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.selectedFiles | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.targetComputerGuid | string | 
action\_result\.data\.\*\.backupUsage\.\*\.todoFiles | numeric | 
action\_result\.data\.\*\.blocked | boolean | 
action\_result\.data\.\*\.classification | string | 
action\_result\.data\.\*\.coldBytes | numeric | 
action\_result\.data\.\*\.computerCount | numeric | 
action\_result\.data\.\*\.orgGuid | string | 
action\_result\.data\.\*\.parentOrgGuid | string | 
action\_result\.data\.\*\.configInheritanceCounts\.allDeviceCount | numeric | 
action\_result\.data\.\*\.configInheritanceCounts\.allOrgCount | numeric | 
action\_result\.data\.\*\.configInheritanceCounts\.inheritedDeviceCount | numeric | 
action\_result\.data\.\*\.configInheritanceCounts\.inheritedOrgCount | numeric | 
action\_result\.data\.\*\.creationDate | string | 
action\_result\.data\.\*\.customConfig | boolean | 
action\_result\.data\.\*\.deactivationDate | string | 
action\_result\.data\.\*\.deviceDefaults | string | 
action\_result\.data\.\*\.externalId | string | 
action\_result\.data\.\*\.hierarchyCounts\.allDeviceCount | numeric | 
action\_result\.data\.\*\.hierarchyCounts\.allOrgCount | numeric | 
action\_result\.data\.\*\.hierarchyCounts\.inheritedDeviceCount | numeric | 
action\_result\.data\.\*\.hierarchyCounts\.inheritedOrgCount | numeric | 
action\_result\.data\.\*\.licensedUserCount | numeric | 
action\_result\.data\.\*\.modificationDate | string | 
action\_result\.data\.\*\.notes | string | 
action\_result\.data\.\*\.orgCount | numeric | 
action\_result\.data\.\*\.orgExtRef | string | 
action\_result\.data\.\*\.orgId | numeric |  `code42 org id` 
action\_result\.data\.\*\.orgInheritDto\.orgNameProvidingDestinations | string | 
action\_result\.data\.\*\.orgInheritDto\.orgNameProvidingDeviceDefaults | string | 
action\_result\.data\.\*\.orgInheritDto\.orgNameProvidingOrg | string | 
action\_result\.data\.\*\.orgInheritDto\.orgUid | string | 
action\_result\.data\.\*\.orgInheritDto\.orgUidProvidingDestinations | string | 
action\_result\.data\.\*\.orgInheritDto\.orgUidProvidingDeviceDefaults | string | 
action\_result\.data\.\*\.orgInheritDto\.orgUidProvidingOrg | numeric | 
action\_result\.data\.\*\.orgName | string |  `code42 org name` 
action\_result\.data\.\*\.orgUid | string | 
action\_result\.data\.\*\.parentOrgId | numeric |  `code42 org id` 
action\_result\.data\.\*\.parentOrgUid | string | 
action\_result\.data\.\*\.planCount | numeric | 
action\_result\.data\.\*\.registrationKey | string | 
action\_result\.data\.\*\.reporting\.orgManagers\.\*\.firstName | string | 
action\_result\.data\.\*\.reporting\.orgManagers\.\*\.lastName | string | 
action\_result\.data\.\*\.reporting\.orgManagers\.\*\.uid | string | 
action\_result\.data\.\*\.reporting\.orgManagers\.\*\.username | string |  `user name` 
action\_result\.data\.\*\.settings\.alertInDays | numeric | 
action\_result\.data\.\*\.settings\.allDestinations\.\*\.destinationName | string | 
action\_result\.data\.\*\.settings\.allDestinations\.\*\.guid | string | 
action\_result\.data\.\*\.settings\.allDestinations\.\*\.type | string | 
action\_result\.data\.\*\.settings\.allowLocalFolders | boolean | 
action\_result\.data\.\*\.settings\.archiveHoldDays | numeric | 
action\_result\.data\.\*\.settings\.autoOfferSelf | boolean | 
action\_result\.data\.\*\.settings\.defaultRoles | string | 
action\_result\.data\.\*\.settings\.defaultUserMaxBytes | numeric | 
action\_result\.data\.\*\.settings\.defaultUserMobileQuota | numeric | 
action\_result\.data\.\*\.settings\.destinations\.\*\.destinationName | string | 
action\_result\.data\.\*\.settings\.destinations\.\*\.guid | string | 
action\_result\.data\.\*\.settings\.destinations\.\*\.type | string | 
action\_result\.data\.\*\.settings\.isDefaultRolesInherited | boolean | 
action\_result\.data\.\*\.settings\.isNativeClientsEnabled | boolean | 
action\_result\.data\.\*\.settings\.isSimpleOrg | boolean | 
action\_result\.data\.\*\.settings\.isUsingDestinationDefaults | boolean | 
action\_result\.data\.\*\.settings\.isUsingQuotaDefaults | boolean | 
action\_result\.data\.\*\.settings\.isUsingReportingDefaults | boolean | 
action\_result\.data\.\*\.settings\.ldapServerIds | numeric | 
action\_result\.data\.\*\.settings\.maxBytes | numeric | 
action\_result\.data\.\*\.settings\.maxSeats | numeric | 
action\_result\.data\.\*\.settings\.radiusServerIds | numeric | 
action\_result\.data\.\*\.settings\.recipients | string |  `email` 
action\_result\.data\.\*\.settings\.reportLastSent | string | 
action\_result\.data\.\*\.settings\.reportSchedule | string | 
action\_result\.data\.\*\.settings\.securityKeyInherit | boolean | 
action\_result\.data\.\*\.settings\.securityKeyLocked | boolean | 
action\_result\.data\.\*\.settings\.securityKeyType | string | 
action\_result\.data\.\*\.settings\.sendReports | boolean | 
action\_result\.data\.\*\.settings\.ssoIdentityProviderUids | string | 
action\_result\.data\.\*\.settings\.usernameIsAnEmail | boolean | 
action\_result\.data\.\*\.settings\.warnInDays | numeric | 
action\_result\.data\.\*\.settings\.webRestoreAdminLimitMb | numeric | 
action\_result\.data\.\*\.settings\.webRestoreUserLimitMb | numeric | 
action\_result\.data\.\*\.settingsInherited\.alertInDays | numeric | 
action\_result\.data\.\*\.settingsInherited\.allDestinations\.\*\.destinationName | string | 
action\_result\.data\.\*\.settingsInherited\.allDestinations\.\*\.guid | string | 
action\_result\.data\.\*\.settingsInherited\.allDestinations\.\*\.type | string | 
action\_result\.data\.\*\.settingsInherited\.allowLocalFolders | boolean | 
action\_result\.data\.\*\.settingsInherited\.archiveHoldDays | numeric | 
action\_result\.data\.\*\.settingsInherited\.autoOfferSelf | boolean | 
action\_result\.data\.\*\.settingsInherited\.defaultRoles | string | 
action\_result\.data\.\*\.settingsInherited\.defaultUserMaxBytes | numeric | 
action\_result\.data\.\*\.settingsInherited\.defaultUserMobileQuota | numeric | 
action\_result\.data\.\*\.settingsInherited\.destinations\.\*\.destinationName | string | 
action\_result\.data\.\*\.settingsInherited\.destinations\.\*\.guid | string | 
action\_result\.data\.\*\.settingsInherited\.destinations\.\*\.type | string | 
action\_result\.data\.\*\.settingsInherited\.isDefaultRolesInherited | boolean | 
action\_result\.data\.\*\.settingsInherited\.isNativeClientsEnabled | boolean | 
action\_result\.data\.\*\.settingsInherited\.isSimpleOrg | boolean | 
action\_result\.data\.\*\.settingsInherited\.isUsingDestinationDefaults | boolean | 
action\_result\.data\.\*\.settingsInherited\.isUsingQuotaDefaults | boolean | 
action\_result\.data\.\*\.settingsInherited\.isUsingReportingDefaults | boolean | 
action\_result\.data\.\*\.settingsInherited\.ldapServerIds | numeric | 
action\_result\.data\.\*\.settingsInherited\.maxBytes | numeric | 
action\_result\.data\.\*\.settingsInherited\.maxSeats | numeric | 
action\_result\.data\.\*\.settingsInherited\.radiusServerIds | numeric | 
action\_result\.data\.\*\.settingsInherited\.recipients | string |  `email` 
action\_result\.data\.\*\.settingsInherited\.reportLastSent | string | 
action\_result\.data\.\*\.settingsInherited\.reportSchedule | string | 
action\_result\.data\.\*\.settingsInherited\.securityKeyInherit | boolean | 
action\_result\.data\.\*\.settingsInherited\.securityKeyLocked | boolean | 
action\_result\.data\.\*\.settingsInherited\.securityKeyType | string | 
action\_result\.data\.\*\.settingsInherited\.sendReports | boolean | 
action\_result\.data\.\*\.settingsInherited\.ssoIdentityProviderUids | string | 
action\_result\.data\.\*\.settingsInherited\.usernameIsAnEmail | boolean | 
action\_result\.data\.\*\.settingsInherited\.warnInDays | numeric | 
action\_result\.data\.\*\.settingsInherited\.webRestoreAdminLimitMb | numeric | 
action\_result\.data\.\*\.settingsInherited\.webRestoreUserLimitMb | numeric | 
action\_result\.data\.\*\.settingsSummary\.alertInDays | numeric | 
action\_result\.data\.\*\.settingsSummary\.allDestinations\.\*\.destinationName | string | 
action\_result\.data\.\*\.settingsSummary\.allDestinations\.\*\.guid | string | 
action\_result\.data\.\*\.settingsSummary\.allDestinations\.\*\.type | string | 
action\_result\.data\.\*\.settingsSummary\.allowLocalFolders | boolean | 
action\_result\.data\.\*\.settingsSummary\.archiveHoldDays | numeric | 
action\_result\.data\.\*\.settingsSummary\.autoOfferSelf | boolean | 
action\_result\.data\.\*\.settingsSummary\.defaultRoles | string | 
action\_result\.data\.\*\.settingsSummary\.defaultUserMaxBytes | numeric | 
action\_result\.data\.\*\.settingsSummary\.defaultUserMobileQuota | numeric | 
action\_result\.data\.\*\.settingsSummary\.destinations\.\*\.destinationName | string | 
action\_result\.data\.\*\.settingsSummary\.destinations\.\*\.guid | string | 
action\_result\.data\.\*\.settingsSummary\.destinations\.\*\.type | string | 
action\_result\.data\.\*\.settingsSummary\.isDefaultRolesInherited | boolean | 
action\_result\.data\.\*\.settingsSummary\.isNativeClientsEnabled | boolean | 
action\_result\.data\.\*\.settingsSummary\.isSimpleOrg | boolean | 
action\_result\.data\.\*\.settingsSummary\.isUsingDestinationDefaults | boolean | 
action\_result\.data\.\*\.settingsSummary\.isUsingQuotaDefaults | boolean | 
action\_result\.data\.\*\.settingsSummary\.isUsingReportingDefaults | boolean | 
action\_result\.data\.\*\.settingsSummary\.ldapServerIds | numeric | 
action\_result\.data\.\*\.settingsSummary\.maxBytes | numeric | 
action\_result\.data\.\*\.settingsSummary\.maxSeats | numeric | 
action\_result\.data\.\*\.settingsSummary\.radiusServerIds | numeric | 
action\_result\.data\.\*\.settingsSummary\.recipients | string |  `email` 
action\_result\.data\.\*\.settingsSummary\.reportLastSent | string | 
action\_result\.data\.\*\.settingsSummary\.reportSchedule | string | 
action\_result\.data\.\*\.settingsSummary\.securityKeyInherit | boolean | 
action\_result\.data\.\*\.settingsSummary\.securityKeyLocked | boolean | 
action\_result\.data\.\*\.settingsSummary\.securityKeyType | string | 
action\_result\.data\.\*\.settingsSummary\.sendReports | boolean | 
action\_result\.data\.\*\.settingsSummary\.ssoIdentityProviderUids | string | 
action\_result\.data\.\*\.settingsSummary\.usernameIsAnEmail | boolean | 
action\_result\.data\.\*\.settingsSummary\.warnInDays | numeric | 
action\_result\.data\.\*\.settingsSummary\.webRestoreAdminLimitMb | numeric | 
action\_result\.data\.\*\.settingsSummary\.webRestoreUserLimitMb | numeric | 
action\_result\.data\.\*\.shareDeviceCount | numeric | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.userCount | numeric | 
action\_result\.data\.\*\.windowsUsmtFiles\.APP\.filename | string |  `file name` 
action\_result\.data\.\*\.windowsUsmtFiles\.CONFIG\.filename | string |  `file name` 
action\_result\.data\.\*\.windowsUsmtFiles\.CUSTOM\.filename | string |  `file name` 
action\_result\.data\.\*\.windowsUsmtFiles\.DOCS\.filename | string |  `file name` 
action\_result\.data\.\*\.windowsUsmtFiles\.USER\.filename | string |  `file name` 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.total\_organizations | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'lock device'
Invoke an access lock on a specified device

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**device\_id** |  required  | ID of the device to lock | numeric |  `code42 device id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.device\_id | numeric |  `code42 device id` 
action\_result\.data\.\*\.data | string | 
action\_result\.data\.\*\.data\.deviceLockableResult | string | 
action\_result\.data\.\*\.data\.deviceRestarting | boolean | 
action\_result\.data\.\*\.data\.volumeStatuses | string | 
action\_result\.data\.\*\.error | string | 
action\_result\.data\.\*\.warnings | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'unlock device'
Deactivate an access lock on a specified device

Type: **correct**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**device\_id** |  required  | ID of the device to unlock | numeric |  `code42 device id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.device\_id | numeric |  `code42 device id` 
action\_result\.data\.\*\.data\.creationDate | string | 
action\_result\.data\.\*\.data\.deviceGuid | string |  `code42 device guid` 
action\_result\.data\.\*\.data\.isLockEnabled | boolean | 
action\_result\.data\.\*\.data\.isOsVolumeLocked | boolean | 
action\_result\.data\.\*\.data\.lastClientResponseDate | string | 
action\_result\.data\.\*\.data\.lockEnabledDate | string | 
action\_result\.data\.\*\.data\.lockPassphrase | string | 
action\_result\.data\.\*\.data\.lockedVolumeCount | numeric | 
action\_result\.data\.\*\.data\.lockingUserUid | string | 
action\_result\.data\.\*\.data\.modificationDate | string | 
action\_result\.data\.\*\.data\.totalVolumeCount | numeric | 
action\_result\.data\.\*\.data\.unlockDate | string | 
action\_result\.data\.\*\.data\.unlockingUserUid | string | 
action\_result\.data\.\*\.error | string | 
action\_result\.data\.\*\.warnings | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.passphrase | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get device'
Get information for a specific device

Type: **investigate**  
Read only: **True**

The <b>query</b> parameter allows flexible searching on computer name, osHostname, or guid\. One parameter or the other must be used\. If both the parameters are provided, <b>device\_id</b> will be used to fetch the device details\. Please provide at least one of the <b>device\_id</b> or <b>query</b> parameter\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**device\_id** |  optional  | ID of the device | numeric |  `code42 device id` 
**query** |  optional  | Query to match against computer name, osHostname, or guid | string |  `code42 device guid`  `host name` 
**most\_recent\_only** |  optional  | Forces action to return one result, being the most recently connected device | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.device\_id | numeric |  `code42 device id` 
action\_result\.parameter\.most\_recent\_only | boolean | 
action\_result\.parameter\.query | string |  `code42 device guid`  `host name` 
action\_result\.data\.\*\.active | boolean | 
action\_result\.data\.\*\.address | string | 
action\_result\.data\.\*\.alertState | numeric | 
action\_result\.data\.\*\.alertStates | string | 
action\_result\.data\.\*\.backupUsage\.\*\.alertState | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.alertStates | string | 
action\_result\.data\.\*\.backupUsage\.\*\.archiveBytes | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.archiveFormat | string | 
action\_result\.data\.\*\.backupUsage\.\*\.archiveGuid | string | 
action\_result\.data\.\*\.backupUsage\.\*\.billableBytes | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.completionRateAverage | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.creationDate | string | 
action\_result\.data\.\*\.backupUsage\.\*\.isProvider | boolean | 
action\_result\.data\.\*\.backupUsage\.\*\.lastBackup | string | 
action\_result\.data\.\*\.backupUsage\.\*\.lastCompactDate | string | 
action\_result\.data\.\*\.backupUsage\.\*\.lastCompletedBackup | string | 
action\_result\.data\.\*\.backupUsage\.\*\.lastConnected | string | 
action\_result\.data\.\*\.backupUsage\.\*\.lastMaintenanceDate | string | 
action\_result\.data\.\*\.backupUsage\.\*\.modificationDate | string | 
action\_result\.data\.\*\.backupUsage\.\*\.percentComplete | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.selectedBytes | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.selectedFiles | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.sendRateAverage | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.serverGuid | string | 
action\_result\.data\.\*\.backupUsage\.\*\.serverHostName | string |  `url`  `host name` 
action\_result\.data\.\*\.backupUsage\.\*\.serverId | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.serverName | string | 
action\_result\.data\.\*\.backupUsage\.\*\.storePointId | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.storePointName | string | 
action\_result\.data\.\*\.backupUsage\.\*\.targetComputerGuid | string | 
action\_result\.data\.\*\.backupUsage\.\*\.targetComputerId | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.targetComputerName | string | 
action\_result\.data\.\*\.backupUsage\.\*\.targetComputerOsName | string | 
action\_result\.data\.\*\.backupUsage\.\*\.targetComputerParentGuid | string | 
action\_result\.data\.\*\.backupUsage\.\*\.targetComputerParentId | string | 
action\_result\.data\.\*\.backupUsage\.\*\.targetComputerType | string | 
action\_result\.data\.\*\.backupUsage\.\*\.todoBytes | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.todoFiles | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.using | boolean | 
action\_result\.data\.\*\.backupUsage\.\*\.activity\.backingUp | boolean | 
action\_result\.data\.\*\.backupUsage\.\*\.activity\.connected | boolean | 
action\_result\.data\.\*\.backupUsage\.\*\.activity\.restoring | boolean | 
action\_result\.data\.\*\.backupUsage\.\*\.activity\.remainingBytes | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.activity\.remainingFiles | numeric | 
action\_result\.data\.\*\.backupUsage\.\*\.activity\.timeRemainingInMs | numeric | 
action\_result\.data\.\*\.blocked | boolean | 
action\_result\.data\.\*\.buildVersion | numeric | 
action\_result\.data\.\*\.computerExtRef | string | 
action\_result\.data\.\*\.computerId | numeric |  `code42 device id` 
action\_result\.data\.\*\.creationDate | string | 
action\_result\.data\.\*\.guid | string |  `code42 device guid` 
action\_result\.data\.\*\.javaVersion | string | 
action\_result\.data\.\*\.lastConnected | string | 
action\_result\.data\.\*\.loginDate | string | 
action\_result\.data\.\*\.modelInfo | string | 
action\_result\.data\.\*\.modificationDate | string | 
action\_result\.data\.\*\.name | string |  `host name` 
action\_result\.data\.\*\.notes | string | 
action\_result\.data\.\*\.orgId | numeric | 
action\_result\.data\.\*\.orgUid | string | 
action\_result\.data\.\*\.osArch | string | 
action\_result\.data\.\*\.osHostname | string |  `host name` 
action\_result\.data\.\*\.osName | string | 
action\_result\.data\.\*\.osVersion | string | 
action\_result\.data\.\*\.parentComputerGuid | string | 
action\_result\.data\.\*\.parentComputerId | numeric |  `code42 device id` 
action\_result\.data\.\*\.productVersion | string | 
action\_result\.data\.\*\.remoteAddress | string |  `ip` 
action\_result\.data\.\*\.service | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.timeZone | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.userId | numeric | 
action\_result\.data\.\*\.userUid | string | 
action\_result\.data\.\*\.version | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.total\_devices | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'push restore'
Push a restore on a device

Type: **correct**  
Read only: **False**

A user with the Push Restore role is required \(or the SYSADMIN\)\. Please provide at least one of the <b>files</b> or <b>directories</b> parameter\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**src\_device\_guid** |  required  | GUID of the source device | string |  `code42 device guid` 
**accepting\_device\_guid** |  required  | GUID of the destination device | string |  `code42 device guid` 
**target\_node\_guid** |  required  | GUID of the target node \(backup server\) | string |  `code42 device guid` 
**restore\_path** |  required  | Path on accepting device to restore | string |  `file path` 
**files** |  optional  | Comma\-separated list of file paths to restore | string |  `file path` 
**directories** |  optional  | Comma\-separated list of directory paths to restore | string |  `file path` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.accepting\_device\_guid | string |  `code42 device guid` 
action\_result\.parameter\.directories | string |  `file path` 
action\_result\.parameter\.files | string |  `file path` 
action\_result\.parameter\.restore\_path | string |  `file path` 
action\_result\.parameter\.src\_device\_guid | string |  `code42 device guid` 
action\_result\.parameter\.target\_node\_guid | string |  `code42 device guid` 
action\_result\.data\.\*\.acceptingGuid | string |  `code42 device guid` 
action\_result\.data\.\*\.canceled | boolean | 
action\_result\.data\.\*\.done | boolean | 
action\_result\.data\.\*\.originalEndpointPlatform | string | 
action\_result\.data\.\*\.originalEndpointVersion | string | 
action\_result\.data\.\*\.providerDestination | boolean | 
action\_result\.data\.\*\.restoreId | string |  `code42 restore id` 
action\_result\.data\.\*\.web\_restore\_session\_id | string |  `code42 web restore session id` 
action\_result\.data\.\*\.sourceId | string | 
action\_result\.data\.\*\.targetEndpointPlatform | string | 
action\_result\.data\.\*\.targetEndpointVersion | string | 
action\_result\.data\.\*\.userId | numeric | 
action\_result\.data\.\*\.originalEndpointOsName | string | 
action\_result\.data\.\*\.acceptingEndpointOsName | string | 
action\_result\.data\.\*\.originalEndpointOsVersion | string | 
action\_result\.data\.\*\.acceptingEndpointOsVersion | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.total\_events | numeric | 
action\_result\.summary\.restore\_id | string |  `code42 restore id` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'check restore status'
Check the status of a restore on a device

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**restore\_id** |  required  | Unique ID of the restore record | string |  `code42 restore id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.restore\_id | string |  `code42 restore id` 
action\_result\.data\.\*\.archiveGuid | string | 
action\_result\.data\.\*\.byteCount | numeric | 
action\_result\.data\.\*\.canceled | boolean | 
action\_result\.data\.\*\.completedDate | string | 
action\_result\.data\.\*\.acceptingComputerGuid | string |  `code42 device guid` 
action\_result\.data\.\*\.failedChecksumCount | numeric | 
action\_result\.data\.\*\.fileCount | numeric | 
action\_result\.data\.\*\.planUid | string | 
action\_result\.data\.\*\.problemCount | numeric | 
action\_result\.data\.\*\.requestingUserId | numeric | 
action\_result\.data\.\*\.restoreId | string |  `code42 restore id` 
action\_result\.data\.\*\.sourceComputerGuid | string |  `code42 device guid` 
action\_result\.data\.\*\.sourceOrgId | numeric | 
action\_result\.data\.\*\.sourceUserId | numeric | 
action\_result\.data\.\*\.startDate | string | 
action\_result\.data\.\*\.targetComputerGuid | string |  `code42 device guid` 
action\_result\.data\.\*\.type | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.total\_events | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get user'
Retrieves information for a specific user

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**user** |  required  | ID or username of the user to retrieve information | string |  `code42 user id`  `user name` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.user | string |  `code42 user id`  `user name` 
action\_result\.data\.\*\.active | boolean | 
action\_result\.data\.\*\.blocked | boolean | 
action\_result\.data\.\*\.creationDate | string | 
action\_result\.data\.\*\.email | string |  `email` 
action\_result\.data\.\*\.emailPromo | boolean | 
action\_result\.data\.\*\.firstName | string | 
action\_result\.data\.\*\.invited | boolean | 
action\_result\.data\.\*\.lastName | string | 
action\_result\.data\.\*\.licenses | string | 
action\_result\.data\.\*\.localAuthenticationOnly | boolean | 
action\_result\.data\.\*\.modificationDate | string | 
action\_result\.data\.\*\.notes | string | 
action\_result\.data\.\*\.orgId | numeric |  `code42 org id` 
action\_result\.data\.\*\.orgName | string |  `code42 org name` 
action\_result\.data\.\*\.orgType | string | 
action\_result\.data\.\*\.orgUid | string | 
action\_result\.data\.\*\.passwordReset | boolean | 
action\_result\.data\.\*\.quotaInBytes | numeric | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.userExtRef | string | 
action\_result\.data\.\*\.userId | numeric |  `code42 user id` 
action\_result\.data\.\*\.userUid | string | 
action\_result\.data\.\*\.username | string |  `user name`  `email` 
action\_result\.data\.\*\.usernameIsAnEmail | boolean | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.total\_users | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'hunt file'
Hunt file on a forensic search

Type: **investigate**  
Read only: **True**

The 'max\_results' parameter is added to retrieve the provided number of max data\. The default value is 100\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**file\_hash** |  required  | MD5 hash of the file to search | string |  `md5` 
**max\_results** |  optional  | Max results to return \(Default\: 100\) | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.file\_hash | string |  `md5` 
action\_result\.parameter\.max\_results | numeric | 
action\_result\.data\.\*\.actor | string | 
action\_result\.data\.\*\.cloudDriveId | string | 
action\_result\.data\.\*\.cloudUserId | string | 
action\_result\.data\.\*\.createTimestamp | string | 
action\_result\.data\.\*\.deviceStatus | string | 
action\_result\.data\.\*\.deviceUid | string | 
action\_result\.data\.\*\.deviceUserName | string |  `user name` 
action\_result\.data\.\*\.domainName | string |  `domain` 
action\_result\.data\.\*\.eventId | string | 
action\_result\.data\.\*\.eventTimestamp | string | 
action\_result\.data\.\*\.eventType | string | 
action\_result\.data\.\*\.fileName | string |  `file name` 
action\_result\.data\.\*\.fileOwner | string |  `user name` 
action\_result\.data\.\*\.filePath | string |  `file path` 
action\_result\.data\.\*\.fileSize | numeric |  `file size` 
action\_result\.data\.\*\.fileType | string | 
action\_result\.data\.\*\.md5Checksum | string |  `md5` 
action\_result\.data\.\*\.modifyTimestamp | string | 
action\_result\.data\.\*\.osHostName | string |  `host name` 
action\_result\.data\.\*\.parentDriveId | string | 
action\_result\.data\.\*\.privateIpAddresses | string |  `ip` 
action\_result\.data\.\*\.publicIpAddress | string |  `ip`  `ipv6` 
action\_result\.data\.\*\.sha256Checksum | string |  `sha256` 
action\_result\.data\.\*\.shared | string | 
action\_result\.data\.\*\.source | string | 
action\_result\.data\.\*\.url | string |  `url` 
action\_result\.data\.\*\.userUid | string | 
action\_result\.data\.\*\.fileId | string | 
action\_result\.data\.\*\.tabUrl | string | 
action\_result\.data\.\*\.trusted | boolean | 
action\_result\.data\.\*\.emailFrom | string | 
action\_result\.data\.\*\.riskScore | numeric | 
action\_result\.data\.\*\.emailSender | string | 
action\_result\.data\.\*\.printerName | string | 
action\_result\.data\.\*\.processName | string | 
action\_result\.data\.\*\.emailSubject | string | 
action\_result\.data\.\*\.fileCategory | string | 
action\_result\.data\.\*\.printJobName | string | 
action\_result\.data\.\*\.processOwner | string | 
action\_result\.data\.\*\.riskSeverity | string | 
action\_result\.data\.\*\.remoteActivity | string | 
action\_result\.data\.\*\.destinationName | string | 
action\_result\.data\.\*\.emailRecipients | string | 
action\_result\.data\.\*\.mimeTypeByBytes | string | 
action\_result\.data\.\*\.syncDestination | string | 
action\_result\.data\.\*\.mimeTypeMismatch | boolean | 
action\_result\.data\.\*\.insertionTimestamp | string | 
action\_result\.data\.\*\.outsideActiveHours | boolean | 
action\_result\.data\.\*\.removableMediaName | string | 
action\_result\.data\.\*\.destinationCategory | string | 
action\_result\.data\.\*\.emailDlpPolicyNames | string | 
action\_result\.data\.\*\.fileCategoryByBytes | string | 
action\_result\.data\.\*\.mimeTypeByExtension | string | 
action\_result\.data\.\*\.operatingSystemUser | string | 
action\_result\.data\.\*\.detectionSourceAlias | string | 
action\_result\.data\.\*\.removableMediaVendor | string | 
action\_result\.data\.\*\.removableMediaBusType | string | 
action\_result\.data\.\*\.printedFilesBackupPath | string | 
action\_result\.data\.\*\.removableMediaCapacity | string | 
action\_result\.data\.\*\.fileCategoryByExtension | string | 
action\_result\.data\.\*\.removableMediaMediaName | string | 
action\_result\.data\.\*\.removableMediaSerialNumber | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.total\_events | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'run query'
Run query on a forensic search

Type: **investigate**  
Read only: **True**

You can use wildcards \(\*,?\) with parameters <b>file\_name</b> and <b>file\_path</b>\. All query parameters are logical AND with each other\. Parameters <b>start\_time</b> and <b>end\_time</b> are required when parameter <b>query</b> is not provided\.<br>If <b>query</b> parameter is provided, other parameters will be ignored\. Below is an example query for the <b>query</b> parameter\:<br><pre>\{"groups"\: \[\{"filters"\: \[\{"operator"\: "IS", "term"\: "md5Checksum", "value"\: "db349b97c37d22f5ea1d1841e3c89eb4"\}, \{"operator"\: "IS", "term"\: "md5Checksum", "value"\: "84c82835a5d21bbcf75a61706d8ab549"\}, \{"operator"\: "IS", "term"\: "md5Checksum", "value"\: "f351e1fcca0c4ea05fc44d15a17f8b36"\}, \{"operator"\: "IS", "term"\: "md5Checksum", "value"\: "7bf2b57f2a205768755c07f238fb32cc"\}\], "filterClause"\: "OR"\}, \{"filters"\: \[\{"operator"\: "ON\_OR\_AFTER", "term"\: "eventTimestamp", "value"\: "2018\-02\-01T00\:00\:00\.00Z"\}, \{"operator"\: "ON\_OR\_BEFORE", "term"\: "eventTimestamp", "value"\: "2018\-02\-07T00\:00\:00\.00Z"\}\], "filterClause"\: "AND"\}\], "groupClause"\: "AND"\}</pre><br>Please refer to the Forensic file search <a href='https\://support\.code42\.com/Administrator/Cloud/Monitoring\_and\_managing/Code42\_API\_resources/Forensic\_Search\_API'>API documentation</a> for more details on query format\. The 'max\_results' parameter is added to retrieve the provided number of max data\. The default value is 100\. </br><b>Note\:</b> The value of 'pgNum' or 'pgSize' parameter provided in the JSON query parameter will be ignored by default\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**start\_time** |  optional  | Start time in epoch\(in seconds\) | numeric | 
**end\_time** |  optional  | End time in epoch\(in seconds\) | numeric | 
**file\_event** |  optional  | Type of file event | string | 
**file\_hash** |  optional  | MD5 hash of the file to search | string |  `md5` 
**file\_name** |  optional  | File name | string |  `file name` 
**file\_path** |  optional  | File path | string |  `file path` 
**hostname** |  optional  | Hostname | string |  `host name` 
**username** |  optional  | User name | string |  `user name` 
**private\_ip** |  optional  | Private IPv4 or IPv6 address | string |  `ip`  `ipv6` 
**public\_ip** |  optional  | Public IPv4 or IPv6 address | string |  `ip`  `ipv6` 
**max\_results** |  optional  | Max results to return \(Default\: 100\) | numeric | 
**query** |  optional  | Query in JSON format | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.end\_time | numeric | 
action\_result\.parameter\.file\_event | string | 
action\_result\.parameter\.file\_hash | string |  `md5` 
action\_result\.parameter\.file\_name | string |  `file name` 
action\_result\.parameter\.file\_path | string |  `file path` 
action\_result\.parameter\.hostname | string |  `host name` 
action\_result\.parameter\.private\_ip | string |  `ip`  `ipv6` 
action\_result\.parameter\.public\_ip | string |  `ip`  `ipv6` 
action\_result\.parameter\.max\_results | numeric | 
action\_result\.parameter\.query | string | 
action\_result\.parameter\.start\_time | numeric | 
action\_result\.parameter\.username | string |  `user name` 
action\_result\.data\.\*\.actor | string | 
action\_result\.data\.\*\.cloudDriveId | string | 
action\_result\.data\.\*\.cloudUserId | string | 
action\_result\.data\.\*\.createTimestamp | string | 
action\_result\.data\.\*\.deviceStatus | string | 
action\_result\.data\.\*\.deviceUid | string | 
action\_result\.data\.\*\.deviceUserName | string |  `user name` 
action\_result\.data\.\*\.domainName | string |  `domain` 
action\_result\.data\.\*\.eventId | string | 
action\_result\.data\.\*\.eventTimestamp | string | 
action\_result\.data\.\*\.eventType | string | 
action\_result\.data\.\*\.fileName | string |  `file name` 
action\_result\.data\.\*\.fileOwner | string |  `user name` 
action\_result\.data\.\*\.filePath | string |  `file path` 
action\_result\.data\.\*\.fileSize | numeric |  `file size` 
action\_result\.data\.\*\.fileType | string | 
action\_result\.data\.\*\.md5Checksum | string |  `md5` 
action\_result\.data\.\*\.modifyTimestamp | string | 
action\_result\.data\.\*\.osHostName | string |  `host name` 
action\_result\.data\.\*\.parentDriveId | string | 
action\_result\.data\.\*\.privateIpAddresses | string |  `ip`  `ipv6` 
action\_result\.data\.\*\.publicIpAddress | string |  `ip`  `ipv6` 
action\_result\.data\.\*\.sha256Checksum | string |  `sha256` 
action\_result\.data\.\*\.shared | string | 
action\_result\.data\.\*\.source | string | 
action\_result\.data\.\*\.url | string |  `url` 
action\_result\.data\.\*\.userUid | string | 
action\_result\.data\.\*\.fileId | string | 
action\_result\.data\.\*\.tabUrl | string | 
action\_result\.data\.\*\.trusted | boolean | 
action\_result\.data\.\*\.emailFrom | string | 
action\_result\.data\.\*\.riskScore | numeric | 
action\_result\.data\.\*\.emailSender | string | 
action\_result\.data\.\*\.printerName | string | 
action\_result\.data\.\*\.processName | string | 
action\_result\.data\.\*\.emailSubject | string | 
action\_result\.data\.\*\.fileCategory | string | 
action\_result\.data\.\*\.printJobName | string | 
action\_result\.data\.\*\.processOwner | string | 
action\_result\.data\.\*\.riskSeverity | string | 
action\_result\.data\.\*\.remoteActivity | string | 
action\_result\.data\.\*\.destinationName | string | 
action\_result\.data\.\*\.emailRecipients | string | 
action\_result\.data\.\*\.mimeTypeByBytes | string | 
action\_result\.data\.\*\.syncDestination | string | 
action\_result\.data\.\*\.mimeTypeMismatch | boolean | 
action\_result\.data\.\*\.insertionTimestamp | string | 
action\_result\.data\.\*\.outsideActiveHours | boolean | 
action\_result\.data\.\*\.removableMediaName | string | 
action\_result\.data\.\*\.destinationCategory | string | 
action\_result\.data\.\*\.emailDlpPolicyNames | string | 
action\_result\.data\.\*\.fileCategoryByBytes | string | 
action\_result\.data\.\*\.mimeTypeByExtension | string | 
action\_result\.data\.\*\.operatingSystemUser | string | 
action\_result\.data\.\*\.detectionSourceAlias | string | 
action\_result\.data\.\*\.removableMediaVendor | string | 
action\_result\.data\.\*\.removableMediaBusType | string | 
action\_result\.data\.\*\.printedFilesBackupPath | string | 
action\_result\.data\.\*\.removableMediaCapacity | string | 
action\_result\.data\.\*\.fileCategoryByExtension | string | 
action\_result\.data\.\*\.removableMediaMediaName | string | 
action\_result\.data\.\*\.removableMediaSerialNumber | string | 
action\_result\.data\.\*\.tabs\.\*\.url | string | 
action\_result\.data\.\*\.tabs\.\*\.title | string | 
action\_result\.data\.\*\.tabs\.\*\.urlError | string | 
action\_result\.data\.\*\.tabs\.\*\.titleError | string | 
action\_result\.data\.\*\.riskIndicators\.\*\.name | string | 
action\_result\.data\.\*\.riskIndicators\.\*\.weight | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.total\_events | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get organization info'
Retrieve Code42 organization info using the v3\_user\_token for the given username & password

Type: **investigate**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data\.\*\.deploymentModel | string | 
action\_result\.data\.\*\.maintenanceMode | boolean | 
action\_result\.data\.\*\.masterServicesAgreement | string | 
action\_result\.data\.\*\.masterServicesAgreement\.acceptanceRequired | boolean | 
action\_result\.data\.\*\.masterServicesAgreement\.accepted | boolean | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.registrationKey | string | 
action\_result\.data\.\*\.tenantUid | string |  `code42 tenant id` 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'add departing employee'
Add Departing Employee to Code42 Organization

Type: **correct**  
Read only: **False**

Action is divided into mainly two parts\. First, the user profile will be created for the specified user and second is used to add the user profile to the departing employee list\. Also, it will update/add the departure\_notes and cloud\_username details for the already added user profile\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**departing\_employee\_url** |  required  | Base URL for Departing Employee API | string |  `url` 
**tenant\_id** |  required  | Tenant ID for Code42 organization | string |  `code42 tenant id` 
**departing\_user** |  required  | Code42 username of the departing employee | string |  `user name` 
**departure\_notes** |  optional  | Optional notes for departing employee | string | 
**departure\_date** |  optional  | Departure date of departing employee \(Format\: 'YYYY\-MM\-DD'\) | string | 
**cloud\_usernames** |  optional  | Comma\-separated list of cloud aliases | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.departing\_employee\_url | string |  `url` 
action\_result\.parameter\.tenant\_id | string |  `code42 tenant id` 
action\_result\.parameter\.departing\_user | string |  `user name` 
action\_result\.parameter\.departure\_notes | string | 
action\_result\.parameter\.departure\_date | string | 
action\_result\.parameter\.cloud\_usernames | string | 
action\_result\.data\.\*\.userName | string |  `user name` 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.displayName | string | 
action\_result\.data\.\*\.type$ | string | 
action\_result\.data\.\*\.notes | string | 
action\_result\.data\.\*\.caseId | numeric | 
action\_result\.data\.\*\.tenantId | string |  `code42 tenant id` 
action\_result\.data\.\*\.cloudUsernames | string | 
action\_result\.data\.\*\.userId | numeric | 
action\_result\.data\.\*\.departureDate | string | 
action\_result\.data\.\*\.createdAt | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'remove departing employee'
Remove departing employee from the departing employee list

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**departing\_employee\_url** |  required  | Base URL for Departing Employee API | string |  `url` 
**tenant\_id** |  required  | Tenant ID for Code42 organization | string |  `code42 tenant id` 
**departing\_user** |  required  | Code42 username of the departing employee | string |  `user name` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.departing\_employee\_url | string |  `url` 
action\_result\.parameter\.tenant\_id | string |  `code42 tenant id` 
action\_result\.parameter\.departing\_user | string |  `user name` 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 