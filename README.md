# vltrig-proxy

[![GitHub release](https://img.shields.io/github/v/release/HashVault/vltrig-proxy)](https://github.com/HashVault/vltrig-proxy/releases)
[![GitHub downloads](https://img.shields.io/github/downloads/HashVault/vltrig-proxy/total)](https://github.com/HashVault/vltrig-proxy/releases)
[![Discord](https://img.shields.io/discord/440787079950106635?logo=discord)](https://discord.hashvault.pro)
[![GitHub license](https://img.shields.io/github/license/HashVault/vltrig-proxy)](https://github.com/HashVault/vltrig-proxy/blob/master/LICENSE)

A fork of [XMRig Proxy](https://github.com/xmrig/xmrig-proxy) tailored for [HashVault](https://hashvault.pro) mining pools.

> **Anti-censorship first.** Helping miners bypass network restrictions and DNS blocking that prevent access to mining pools. Mining should be accessible to everyone, everywhere.

### Focus Areas

- Anti-censorship features
- Embedded web management UI
- HashVault pool optimizations
- Tracking upstream XMRig Proxy for updates and security fixes

### Not Changing

- Donation mechanics (original XMRig donation is preserved)
- Core proxy functionality

---

## Table of Contents

- [Download](#download)
- [What is a Stratum Proxy?](#what-is-a-stratum-proxy)
- [Building](#building)
- [Web UI](#web-ui)
- [Versioning](#versioning)
- [Upstream XMRig Proxy](#upstream-xmrig-proxy)

---

## Download

Prebuilt binaries are available on the [**Releases**](https://github.com/HashVault/vltrig-proxy/releases) page.

| Platform | Architecture | Notes |
|----------|--------------|-------|
| Linux | x64 | Static binary (musl libc) |
| Windows | x64 | MinGW build |
| macOS | x64 | Intel Macs |
| macOS | ARM64 | Apple Silicon |

---

## What is a Stratum Proxy?

A stratum proxy sits between your miners and the pool, aggregating connections:

```
[Miner 1] --\
[Miner 2] ----> [vltrig-proxy] ----> [Pool]
[Miner N] --/
```

**Benefits:**
- Reduces pool-side connections (100,000 miners -> ~400 pool connections)
- Handles donation traffic efficiently
- Supports both NiceHash and simple modes
- Can manage 100K+ miner connections on minimal hardware

---

## Building

### Dependencies

<details>
<summary><strong>Ubuntu/Debian</strong></summary>

```bash
apt install build-essential cmake libuv1-dev libssl-dev
```

</details>

<details>
<summary><strong>RHEL/CentOS</strong></summary>

```bash
yum install gcc gcc-c++ cmake libuv-devel openssl-devel
```

</details>

<details>
<summary><strong>macOS</strong></summary>

```bash
brew install cmake libuv openssl
```

</details>

### Build Commands

```bash
make release    # Release build
make debug      # Debug build with debug logging
make rebuild    # Clean + release
make clean      # Remove build directory
```

Binary output: `build/vltrig-proxy`

---

## Web UI

vltrig-proxy includes an embedded web management dashboard accessible through the HTTP API.

### Enabling

The Web UI requires the HTTP API to be enabled in your config:

```json
{
    "http": {
        "enabled": true,
        "host": "127.0.0.1",
        "port": 4048,
        "access-token": "your-secret-token",
        "restricted": false
    }
}
```

Set `restricted` to `false` to allow config changes and restart from the UI. When `true`, the UI is read-only.

### Accessing

Open `http://127.0.0.1:4048` in a browser. If an `access-token` is set, the UI will prompt for it on first visit and store it locally.

If TLS is enabled, use `https://` instead. The proxy auto-generates a self-signed certificate if configured cert files are missing.

### Features

- **Dashboard** - live hashrate, upstreams, miner count, share results, connection status
- **Workers** - per-worker hashrate and share statistics with sortable columns
- **Miners** - connected miners list with IP, difficulty, and connection time
- **Config** - quick-settings toggles (mode, workers, difficulty, TLS per bind, verbose) and a full JSON editor with syntax highlighting
- **Restart** - graceful shutdown via the UI (requires a process supervisor like systemd to restart)

### Building Without Web UI

To disable the Web UI at compile time:

```bash
cmake .. -DWITH_WEB_UI=OFF
```

The Web UI requires Python 3 at build time to compress and embed the HTML into the binary.

---

## Versioning

Version format: **`X.Y.Z.P`**

| Part | Description |
|------|-------------|
| `X.Y.Z` | Upstream XMRig Proxy version |
| `.P` | vltrig-proxy patch number (continuous) |

```
XMRig Proxy 6.24.0 -> vltrig-proxy 6.24.0.1 -> 6.24.0.2 -> 6.24.0.3
XMRig Proxy 6.25.0 -> vltrig-proxy 6.25.0.4 -> 6.25.0.5
```

---

## Upstream XMRig Proxy

<details>
<summary><strong>About XMRig Proxy</strong></summary>

[![Github All Releases](https://img.shields.io/github/downloads/xmrig/xmrig-proxy/total.svg)](https://github.com/xmrig/xmrig-proxy/releases)
[![GitHub release](https://img.shields.io/github/release/xmrig/xmrig-proxy/all.svg)](https://github.com/xmrig/xmrig-proxy/releases)
[![GitHub license](https://img.shields.io/github/license/xmrig/xmrig-proxy.svg)](https://github.com/xmrig/xmrig-proxy/blob/master/LICENSE)

XMRig Proxy is an extremely high-performance proxy for the CryptoNote stratum protocol. It can efficiently manage over 100K connections on an inexpensive, low-memory virtual machine.

**Links:**
- [Binary releases](https://github.com/xmrig/xmrig-proxy/releases)
- [Build from source](https://xmrig.com/docs/proxy/build)
- [Documentation](https://xmrig.com/docs/proxy)

**Donations:**
- Default donation 2% can be reduced to 1% or disabled via `donate-level` option
- XMR: `48edfHu7V9Z84YzzMa6fUueoELZ9ZRXq9VetWzYGzKt52XU5xvqgzYnDK9URnRoJMk1j8nLwEVsaSWJ4fhdUyZijBGUicoD`

**Developers:** [xmrig](https://github.com/xmrig), [sech1](https://github.com/SChernykh)

</details>

---

## Contributing

While vltrig-proxy is tailored for HashVault pools, improvements that benefit all users are submitted as pull requests to the upstream [XMRig Proxy](https://github.com/xmrig/xmrig-proxy) project.
