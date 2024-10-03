# Buildbots

[![Status](https://github.com/AOSC-Dev/Buildbots/actions/workflows/status.yml/badge.svg)](https://github.com/AOSC-Dev/Buildbots/actions/workflows/status.yml)
[![Test](https://github.com/AOSC-Dev/Buildbots/actions/workflows/test.yml/badge.svg)](https://github.com/AOSC-Dev/Buildbots/actions/workflows/test.yml)

Collection of buildbot configurations for AOSC OS maintainers. This repo contains [`ssh_config`](https://man.openbsd.org/ssh_config) and [`ssh_known_hosts`](https://man.openbsd.org/sshd.8#SSH_KNOWN_HOSTS_FILE_FORMAT) files of them, for developers' convenience. Repo server's SSH key fingerprints are also included in `ssh_known_hosts`.

There are two relay servers available, one in Washington (WA), one in Shanghai. But there are five IP addresses, each suitable for different network environments. Note that `<text inside angle brackets>` indicates placeholder for which you must supply a value.

- `relay.aosc.io`: IPv4 only, routed via [Microsoft global network](https://learn.microsoft.com/azure/networking/microsoft-global-network), **developers outside of China** should choose this. Connect to this server with `ssh <buildbot>`.
- `relay-ipv6.aosc.io`: IPv6 only, routed via Microsoft global network, **developers outside of China with IPv6** should choose this. Connect to this server with `ssh <buildbot>-ipv6`.
- `relay-cn.aosc.io`: IPv4 only, routed via Microsoft global network, **developers in China** should choose this. Connect to this server with `ssh <buildbot>-cn`.
- `relay-cn-ipv6.aosc.io`: IPv4 only, routed via Microsoft global network, **developers in China with IPv6** should choose this. Connect to this server with `ssh <buildbot>-cn-ipv6`.
- `relay-inet.aosc.io`: IPv4 only, [routed over public Internet (ISP network)](https://learn.microsoft.com/azure/virtual-network/ip-services/routing-preference-overview#routing-over-public-internet-isp-network), **suitable for only specific cases**, such as outage with Microsoft global network. Connect to this server with `ssh <buildbot>-inet`.

Some but not all buildbots are directly accessible from public Internet. These configurations are also included. Works best if the developer is geographically (and digitally) nearby. Connect with `ssh <buildbot>-direct`.

## Installation

### All operating systems, for current user

```bash
curl -LSso $HOME/.ssh/config.d/aosc --create-dirs "https://cdn.jsdelivr.net/gh/AOSC-Dev/Buildbots/ssh_config"
curl -LSso $HOME/.ssh/known_hosts.d/aosc --create-dirs "https://cdn.jsdelivr.net/gh/AOSC-Dev/Buildbots/ssh_known_hosts"
# For UNIX and Unix-like operating systems, set strict permissions on ssh_config file
# chmod 644 $HOME/.ssh/config.d/aosc
```

Then add the following lines to `$HOME/.ssh/config`:

```properties
Host *
  Include config.d/*
```

### UNIX and Unix-like operating systems, for all users

```bash
curl -LSso /etc/ssh/ssh_config.d/aosc --create-dirs "https://cdn.jsdelivr.net/gh/AOSC-Dev/Buildbots/ssh_config"
curl -LSso /etc/ssh/ssh_known_hosts.d/aosc --create-dirs "https://cdn.jsdelivr.net/gh/AOSC-Dev/Buildbots/ssh_known_hosts"
chmod 755 /etc/ssh/ssh_config.d /etc/ssh/ssh_known_hosts.d
```

Then add the following lines to `/etc/ssh/ssh_config`:

```properties
Host *
  Include ssh_config.d/*
```

### Microsoft Windows, for all users

```cmd
curl.exe -LSso C:\ProgramData\ssh\ssh_config.d\aosc --create-dirs "https://cdn.jsdelivr.net/gh/AOSC-Dev/Buildbots/ssh_config"
curl.exe -LSso C:\ProgramData\ssh\ssh_known_hosts.d\aosc --create-dirs "https://cdn.jsdelivr.net/gh/AOSC-Dev/Buildbots/ssh_known_hosts"
```

Then add the following lines to `C:\ProgramData\ssh\ssh_config`:

```properties
Host *
  Include ssh_config.d\*
```
