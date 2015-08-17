# Geoblocker

Script to limit SSH and other types of connections to specified countries.

## Usage

```
geoblocker.sh {some ip}
```

## Installation

Add the following line to `/etc/hosts.allow`:
```
ALL: ALL: aclexec /root/geoblocker/geoblocker.sh %a
```

Then add to `/etc/hosts.deny`:
```
ALL: ALL
```

