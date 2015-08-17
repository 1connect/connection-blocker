# Geoblocker

Script to limit SSH and other types of connections to specified countries.

## Usage

```
geoblocker.sh {some ip}
```

When country is valid, script returns exit status **0**, otherwise **1**.

## Installation

* Install packages: `geoip-bin`, `geoip-database`.
* Clone project repository into `/root/geoblocker`.
* Add the following line to `/etc/hosts.allow`:
```
ALL: ALL: aclexec /root/geoblocker/geoblocker.sh %a
```

* Then add to `/etc/hosts.deny`:
```
ALL: ALL
```