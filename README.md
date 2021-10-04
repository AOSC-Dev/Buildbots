# Buildbots

[![Status](https://github.com/AOSC-Dev/Buildbots/actions/workflows/status.yml/badge.svg)](https://github.com/AOSC-Dev/Buildbots/actions/workflows/status.yml)

Buildbots that can be used by AOSC developers. This repo contains [`ssh_config`](https://man.openbsd.org/ssh_config) and [`ssh_known_hosts`](https://man.openbsd.org/sshd.8#SSH_KNOWN_HOSTS_FILE_FORMAT) files of them, for developers' convenience. Repo server's SSH key fingerprints are also included in `ssh_known_hosts`.

## Installation

### All operating systems, for current user

```bash
curl -LSso ~/.ssh/config.d/aosc --create-dirs "https://cdn.jsdelivr.net/gh/AOSC-Dev/Buildbots/ssh_config"
curl -LSso ~/.ssh/known_hosts.d/aosc --create-dirs "https://cdn.jsdelivr.net/gh/AOSC-Dev/Buildbots/ssh_known_hosts"
```

Then add the following lines to `~/.ssh/config`:

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
