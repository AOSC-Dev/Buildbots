# Buildbots

Buildbots that can be used by AOSC developers. This repo contains [`ssh_config`](https://man.openbsd.org/ssh_config) and [`ssh_known_hosts`](https://man.openbsd.org/sshd.8#SSH_KNOWN_HOSTS_FILE_FORMAT) files of them, for developers' convenience. Repo server's SSH key fingerprints are also included in `ssh_known_hosts`.

## Usage

Download [ssh_known_hosts](https://cdn.jsdelivr.net/gh/AOSC-Dev/BuildBots/ssh_known_hosts) and [ssh_config](https://cdn.jsdelivr.net/gh/AOSC-Dev/BuildBots/ssh_config) files.

```bash
curl -LSso ~/.ssh/config.d/aosc --create-dirs https://cdn.jsdelivr.net/gh/AOSC-Dev/BuildBots/ssh_config
curl -LSso ~/.ssh/known_hosts.d/aosc --create-dirs https://cdn.jsdelivr.net/gh/AOSC-Dev/BuildBots/ssh_known_hosts
```

Then add the following lines to `~/.ssh/config`:

```properties
Host *
  Include config.d/*
```

You're ready to go!

If you would like to install them globally, run the following with root privileges.

```bash
curl -LSso /etc/ssh/ssh_config.d/aosc --create-dirs https://cdn.jsdelivr.net/gh/AOSC-Dev/BuildBots/ssh_config
curl -LSso /etc/ssh/ssh_known_hosts.d/aosc --create-dirs https://cdn.jsdelivr.net/gh/AOSC-Dev/BuildBots/ssh_known_hosts
```

Then add the following lines to `/etc/ssh/ssh_config`:

```properties
Host *
  Include config.d/*
```
