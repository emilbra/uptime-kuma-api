# Changelog

## [0.2.1](https://github.com/emilbra/uptime-kuma-api/compare/v0.2.0...v0.2.1) (2024-11-28)


### Bug Fixes

* property should be called jsonPathOperator, not jsonOperator ([5c22ae7](https://github.com/emilbra/uptime-kuma-api/commit/5c22ae719db8765e8cf108e648175a198b4cdbcc))

## [0.2.0](https://github.com/emilbra/uptime-kuma-api/compare/v0.1.0...v0.2.0) (2024-11-28)


### Features

* added support for jsonOperator value being passed for type json_query ([12d7b10](https://github.com/emilbra/uptime-kuma-api/commit/12d7b10905a9c013c6a373bff4d507daa4489444))

## 0.1.0 (2024-11-26)


### ⚠ BREAKING CHANGES

* 
* Removed `get_heartbeat` method. This method was never intended to retrieve information. Use `get_heartbeats` or `get_important_heartbeats` instead.
* Uptime Kuma versions < 1.21.3 are not supported in uptime-kuma-api 1.x.x
* changed return values of get_heartbeats, get_important_heartbeats, avg_ping, uptime, get_heartbeat, cert_info
* Removed the `wait_timeout` parameter. Use the new `timeout` parameter instead. The `timeout` parameter specifies how many seconds the client should wait for the connection, an expected event or a server response.
* maintenance parameter `timezone` renamed to `timezoneOption`
* monitor `status` type changed from `bool` to `MonitorStatus`
* Python 3.7+ required
* Python 3.7+ required

### Features

* add param `wait_events` ([391e5a3](https://github.com/emilbra/uptime-kuma-api/commit/391e5a3077e0db3071405fb0d8f08376378b9d0a))
* add parameter `wait_timeout` to adjust connection timeout ([e0c4207](https://github.com/emilbra/uptime-kuma-api/commit/e0c42079849f8a0adb0f0d317534a98983e7f908))
* add support for uptime kuma 1.18.1 / 1.18.2 ([fee0a1d](https://github.com/emilbra/uptime-kuma-api/commit/fee0a1dd8e91458fbb05daa149aeead9d544341c))
* add support for uptime kuma 1.18.3 ([c8529d6](https://github.com/emilbra/uptime-kuma-api/commit/c8529d65c3fc90493f793d2f083ede29d4064961))
* add support for uptime kuma 1.19.2 ([d01ff6d](https://github.com/emilbra/uptime-kuma-api/commit/d01ff6d80e19427add2db6e3844237c415e2c2b7))
* add support for uptime kuma 1.19.3 ([982c370](https://github.com/emilbra/uptime-kuma-api/commit/982c37045aafa4f7d7ac14bb3f1a46bd930b2eda))
* add support for uptime kuma 1.19.5 ([3e56459](https://github.com/emilbra/uptime-kuma-api/commit/3e56459fb244e922bbf385a87421856a21daa89a))
* add support for uptime kuma 1.20.0 ([14e9f47](https://github.com/emilbra/uptime-kuma-api/commit/14e9f47406e43878b6d65c3f9f2ef74546a79246))
* add support for uptime kuma 1.21.0 ([42c040f](https://github.com/emilbra/uptime-kuma-api/commit/42c040f4517376396c4eb1346749a521abcd5337))
* add support for uptime kuma 1.21.1 ([2773d02](https://github.com/emilbra/uptime-kuma-api/commit/2773d02ee689f259dce8e1613d413c2e1c9022c3))
* add support for uptime kuma 1.21.2 ([d7f0330](https://github.com/emilbra/uptime-kuma-api/commit/d7f033030e066b7f28060e513ed12c0bd6fcb664))
* add support for uptime kuma 1.21.3 ([8e841cd](https://github.com/emilbra/uptime-kuma-api/commit/8e841cd32449d46ac724a3a55140e1097d4e95ed))
* add support for uptime kuma 1.22.0 and 1.22.1 ([06f1173](https://github.com/emilbra/uptime-kuma-api/commit/06f1173569461867982c62332be7a83d38fcf091))
* add support for uptime kuma 1.23.0 and 1.23.1 ([7902213](https://github.com/emilbra/uptime-kuma-api/commit/7902213ddb3b090b46d5b879df2355352e5929b9))
* added .github folder contents (release please and labeler) and made inital change to api.py ([77681ec](https://github.com/emilbra/uptime-kuma-api/commit/77681ec0c48d27a9b2b3fa12fbb465c80b2d5dfe))
* check for required notification arguments ([#36](https://github.com/emilbra/uptime-kuma-api/issues/36)) ([e7693e6](https://github.com/emilbra/uptime-kuma-api/commit/e7693e608140aa20215d26e98554a01c9138f511))
* drop python 3.6 support ([7ef61f8](https://github.com/emilbra/uptime-kuma-api/commit/7ef61f8ce178fb96f8dc58a4dd241decba3ce775))
* drop python 3.6 support ([50ff8f1](https://github.com/emilbra/uptime-kuma-api/commit/50ff8f1219f155671c440f2182935d10d34ae04c))
* drop support for Uptime Kuma versions &lt; 1.21.3 ([f0c5f2b](https://github.com/emilbra/uptime-kuma-api/commit/f0c5f2ba9db363f1129e7a15f218737245bd4ec7))
* implement `get_monitor_status` helper method ([a9f2b6d](https://github.com/emilbra/uptime-kuma-api/commit/a9f2b6d894503fdcbb402353fb5aa76ec5eeb0df))
* implement context manager for UptimeKumaApi class ([e42f646](https://github.com/emilbra/uptime-kuma-api/commit/e42f6461c09c30e6cdceff10cf197fccdd82a6db))
* implement custom socketio headers ([e1fd3b7](https://github.com/emilbra/uptime-kuma-api/commit/e1fd3b7f03a7e80e9bf234749604c35ec7218203))
* implement timeouts for all methods ([#34](https://github.com/emilbra/uptime-kuma-api/issues/34)) ([9728cfd](https://github.com/emilbra/uptime-kuma-api/commit/9728cfdb3445c030a1a50722639dd056a2b2a802))
* raise exception when deleting an element that does not exist ([#37](https://github.com/emilbra/uptime-kuma-api/issues/37)) ([1359576](https://github.com/emilbra/uptime-kuma-api/commit/1359576413e1041c57e6cdaddb6f24f1e0272fc3))
* replace raw return values with enum values ([84d4009](https://github.com/emilbra/uptime-kuma-api/commit/84d4009d6ae52d7221af714c031ea31a7f116b4f))
* support autoLogin for enabled disableAuth ([661c06b](https://github.com/emilbra/uptime-kuma-api/commit/661c06b15fc54f32184fbf65c5f6ce78b937b359))


### Bug Fixes

* add type to notification provider options ([dac368e](https://github.com/emilbra/uptime-kuma-api/commit/dac368e2a5bd67c1c5dd24dc6ae29bb64e808651))
* added necessary repo secret and removed uneeded step ([83a9245](https://github.com/emilbra/uptime-kuma-api/commit/83a924517a09b630bb3dcb32975ae225db85517d))
* adjust `get_monitor_status` method to previous changes ([ce1cc12](https://github.com/emilbra/uptime-kuma-api/commit/ce1cc1274052d5ac08621199830634153197fb71))
* adjust monitor `status` type to allow all used values ([b87eed2](https://github.com/emilbra/uptime-kuma-api/commit/b87eed2597914aca4e00fe0daf47983e5bc3fe47))
* check only for required notification arguments ([8a0ad53](https://github.com/emilbra/uptime-kuma-api/commit/8a0ad53753034f032f7fff2d08944f448463eb04))
* convert monitor notificationIDList only once ([54d221c](https://github.com/emilbra/uptime-kuma-api/commit/54d221cdfe22b6f31d1729cf2c33886ab15dbf97))
* convert monitor notificationIDList return value ([314f07c](https://github.com/emilbra/uptime-kuma-api/commit/314f07c93d87e04cce9cb947efd19ac01a33dc28))
* convert sendUrl from bool to int ([1810784](https://github.com/emilbra/uptime-kuma-api/commit/18107848f8f069b4f6fbe626f484ea2717a231a2))
* do not wait for events that have already arrived ([be537a1](https://github.com/emilbra/uptime-kuma-api/commit/be537a14d2190c790574cf0bf90f583a6c4fec2e))
* drop first info event without a version ([370b7e3](https://github.com/emilbra/uptime-kuma-api/commit/370b7e3e18e070d4c65557b4c4ee6ddf71024f69)), closes [#55](https://github.com/emilbra/uptime-kuma-api/issues/55)
* generate pushToken on push monitor save ([12cd806](https://github.com/emilbra/uptime-kuma-api/commit/12cd8067e469d83912fd8417ffb768c3d7572887))
* increase event wait time ([0821f38](https://github.com/emilbra/uptime-kuma-api/commit/0821f38faa4f38de9f8fa113265d655ae36eae63))
* memory leak ([#29](https://github.com/emilbra/uptime-kuma-api/issues/29)) ([77630e9](https://github.com/emilbra/uptime-kuma-api/commit/77630e96b7d088c4cc6e04669e302b66d402160f))
* process the `HEARTBEAT` event correctly ([762dd4a](https://github.com/emilbra/uptime-kuma-api/commit/762dd4a657270058d9e3f17097a9b53398336e56))
* remove `name` from maintenance monitors and status pages ([2611b34](https://github.com/emilbra/uptime-kuma-api/commit/2611b344f11d3122b14c06eb0ce430f5a2ec0ae5))
* remove `tags` from monitor input ([de38586](https://github.com/emilbra/uptime-kuma-api/commit/de38586bf5285e73e0570c3adbf2590499237cf6))
* remove required notification provider args check ([52d33d8](https://github.com/emilbra/uptime-kuma-api/commit/52d33d8751c086ca7e98fed6b0782e230259cdc3))
* rstip url globally ([3543f09](https://github.com/emilbra/uptime-kuma-api/commit/3543f09a5fbacb67069639b117680e0e258a9bef))
* set_settings password is only required if disableAuth is enabled ([ebadfb7](https://github.com/emilbra/uptime-kuma-api/commit/ebadfb73e6615a16b8b62a687060546de45a39bb))
* skip condition check for None values ([1e4be04](https://github.com/emilbra/uptime-kuma-api/commit/1e4be04ad7f48ec009a995c13a44b3310e6677cd))
* update event list data after changes ([06fa29c](https://github.com/emilbra/uptime-kuma-api/commit/06fa29cd41b9e766f1449f02dd0916daa646005a))
* validate accepted status codes types ([0d49e97](https://github.com/emilbra/uptime-kuma-api/commit/0d49e97fe5bf347002a690298df87a9af55d98bf)), closes [#42](https://github.com/emilbra/uptime-kuma-api/issues/42)
* ValueError if monitor authMethod is None ([ce6f25d](https://github.com/emilbra/uptime-kuma-api/commit/ce6f25d6048ca3fe8b6716e801c31528db876550))


### Documentation

* add docstrings and sphinx, readthedocs configuration ([ce5ba2d](https://github.com/emilbra/uptime-kuma-api/commit/ce5ba2d943b6d3eebcc0874d7286ac2823cf752d))
* add return types and exceptions ([d68168b](https://github.com/emilbra/uptime-kuma-api/commit/d68168b76976f113cdf281c8522fe968d5cb2ef4))
* complete values for uptime kuma 1.19.2 ([c1d941a](https://github.com/emilbra/uptime-kuma-api/commit/c1d941a200d2d7e01b15f7255a2e03b9a54865d0))
* fix list type hints ([4538901](https://github.com/emilbra/uptime-kuma-api/commit/4538901ceaa5d70216247a7ebb3562eaf612b378))
* replace list[dict] with list type hint and add missing type hints ([9e3cbe7](https://github.com/emilbra/uptime-kuma-api/commit/9e3cbe7d59213761bd9fa4067ea5981d7e9794ff))
* update notification docstring ([24b6d36](https://github.com/emilbra/uptime-kuma-api/commit/24b6d367de6f7fa859ee2b920fa747a2ed46ce7a))
* write param and type in the same line and add optional to type ([748d2b1](https://github.com/emilbra/uptime-kuma-api/commit/748d2b191ae7e43a177c7a1cd632fc000568da6b))

## Changelog

### Release 1.2.1

#### Bugfixes
- drop first info event without a version

### Release 1.2.0

#### Features
- add support for uptime kuma 1.23.0 and 1.23.1

#### Bugfixes
- remove `name` from maintenance monitors and status pages
- rstip url globally
- convert sendUrl from bool to int
- validate accepted status codes types

### Release 1.1.0

#### Features
- add support for uptime kuma 1.22.0 and 1.22.1

### Release 1.0.1

#### Bugfixes
- fix ValueError if monitor authMethod is None

### Release 1.0.0

#### Features
- add `ssl_verify` parameter
- add `wait_events` parameter
- implement context manager for UptimeKumaApi class
- drop Python 3.6 support
- implement `get_monitor_status` helper method
- implement timeouts for all methods (`timeout` parameter)
- add support for uptime kuma 1.21.3
- drop support for Uptime Kuma versions < 1.21.3
- check for required notification arguments
- raise exception when deleting an element that does not exist
- replace raw return values with enum values

#### Bugfixes
- adjust monitor `status` type to allow all used values
- fix memory leak

#### BREAKING CHANGES
- Python 3.7+ required
- maintenance parameter `timezone` renamed to `timezoneOption`
- Removed the `wait_timeout` parameter. Use the new `timeout` parameter instead. The `timeout` parameter specifies how many seconds the client should wait for the connection, an expected event or a server response.
- changed return values of methods `get_heartbeats`, `get_important_heartbeats`, `avg_ping`, `uptime`, `cert_info`
- Uptime Kuma versions < 1.21.3 are not supported in uptime-kuma-api 1.0.0+
- Removed the `get_heartbeat` method. This method was never intended to retrieve information. Use `get_heartbeats` or `get_important_heartbeats` instead.
- Types of return values changed to enum values:
  - monitor: `type` (str -> MonitorType), `status` (bool -> MonitorStatus), `authMethod` (str -> AuthMethod)
  - notification: `type` (str -> NotificationType)
  - docker host: `dockerType` (str -> DockerType)
  - status page: `style` (str -> IncidentStyle)
  - maintenance: `strategy` (str -> MaintenanceStrategy)
  - proxy: `protocol` (str -> ProxyProtocol)

### Release 0.13.0

#### Feature
- add support for uptime kuma 1.21.2
- implement custom socketio headers

#### Bugfix
- do not wait for events that have already arrived

### Release 0.12.0

#### Feature
- add support for uptime kuma 1.21.1

### Release 0.11.0

#### Feature
- add support for uptime kuma 1.21.0

### Release 0.10.0

#### Feature
- add support for uptime kuma 1.20.0

### Release 0.9.0

#### Feature
- add support for uptime kuma 1.19.5

### Release 0.8.0

#### Feature
- add support for uptime kuma 1.19.3

### Release 0.7.1

#### Bugfix
- remove unsupported type hints on old python versions

### Release 0.7.0

#### Feature
- add support for uptime kuma 1.19.2

#### Bugfix
- skip condition check for None values

### Release 0.6.0

#### Feature
- add parameter `wait_timeout` to adjust connection timeout

### Release 0.5.2

#### Bugfix
- add type to notification provider options

### Release 0.5.1

#### Bugfix
- remove required notification provider args check

### Release 0.5.0

#### Feature
- support for uptime kuma 1.18.3

### Release 0.4.0

#### Feature
- support for uptime kuma 1.18.1 / 1.18.2

#### Bugfix
- update event list data after changes

### Release 0.3.0

#### Feature
- support autoLogin for enabled disableAuth

#### Bugfix
- set_settings password is only required if disableAuth is enabled
- increase event wait time to receive the slow statusPageList event

### Release 0.2.2

#### Bugfix
- remove `tags` from monitor input
- convert monitor notificationIDList only once

### Release 0.2.1

#### Bugfix
- generate pushToken on push monitor save
- convert monitor notificationIDList return value

### Release 0.2.0

#### Feature
- support for uptime kuma 1.18.0

#### Bugfix
- convert values on monitor edit

### Release 0.1.1

#### Bugfix
- implement 2FA login
- allow to add monitors to status pages
- do not block certain methods

### Release 0.1.0

- initial release
