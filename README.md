# connection-blocker

Script to limit SSH and other types of connections to specified countries.

## Usage

```
blocker.py {service name} {ip}
```

When country is valid, script returns exit status **0**, otherwise **1**.

## Installation

* Install packages: `geoip-bin`, `geoip-database`, `python-geoip`.
* Clone project repository into `/scripts/geoblocker`.
* Add the following line to `/etc/hosts.allow`:
```
ALL: ALL: aclexec /scripts/geoblocker/geoblocker.py %d %a
```

* Then add to `/etc/hosts.deny`:
```
ALL: ALL
```
