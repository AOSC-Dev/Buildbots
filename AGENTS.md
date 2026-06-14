# AGENTS.md

## What this repo is

SSH configuration distribution for AOSC OS buildbot infrastructure. Not a code repo — contains `ssh_config`, `ssh_known_hosts`, and a helper script. Distributed via CDN at `cdn.jsdelivr.net/gh/AOSC-Dev/Buildbots/`.

## Key files

- `ssh_config` — SSH host definitions for all buildbots across relay variants
- `ssh_known_hosts` — SSH host key fingerprints for all ports
- `contrib/trans.py` — adds `<arch>-` prefixed hostnames based on port ranges (pipe ssh_config via stdin)

## Port-to-architecture mapping

(from `contrib/trans.py`):
- 22001–23000: amd64
- 23001–24000: loongson3
- 24001–25000: arm64
- 25001–26000: ppc64el
- 26001–27000: riscv64
- 27001–28000: loongarch64
- 28001–29000: amd64 (emulation — see `trans.py` comment for the pitfall)

## Relay servers

| Hostname | Route | Use case |
|---|---|---|
| `relay.aosc.io` | MS global, IPv4 | Developers outside China (default) |
| `relay-ipv6.aosc.io` | MS global, IPv6 | Outside China, IPv6-capable |
| `relay-cn.aosc.io` | MS global, IPv4 | Developers in China |
| `relay-cn-ipv6.aosc.io` | MS global, IPv6 | China, IPv6-capable |
| `relay-inet.aosc.io` | Public ISP route | Edge cases (MS global outage) |

Each buildbot has aliases: `<name>`, `<arch>-<name>`, plus `-inet`, `-ipv6`, `-cn`, `-cn-ipv6` suffixed variants per relay.

## CI

- `status.yml` — runs every 5 min, checks buildbot reachability via `ssh-keyscan` on all ports/relays
- `test.yml` — validates `ssh_known_hosts`: scans all ports on relay/relay-inet/relay-cn, plus direct-access hosts (ct2.katyusha.top, home.biscuit.moe, kp920.ip4.run, 211.137.78.121) and repo/github SSH hosts, then diffs against stored file

## Gotchas

- No build, test, lint, or codegen commands — this is a config-only repo
- When adding a new buildbot: add entries in `ssh_config`, `ssh_known_hosts`, and update the port lists in both CI workflow files
- `ssh_known_hosts` must include keys for ALL relay variants (relay, relay-inet, relay-cn, relay-ipv6, relay-cn-ipv6) — the CI test scans all three relay hosts
- Port 28001–29000 is mapped to amd64 but noted as a "pitfall" in `trans.py` — these are emulation machines
