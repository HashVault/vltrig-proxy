# vltrig-proxy

[![GitHub release](https://img.shields.io/github/v/release/HashVault/vltrig-proxy)](https://github.com/HashVault/vltrig-proxy/releases)
[![GitHub downloads](https://img.shields.io/github/downloads/HashVault/vltrig-proxy/total)](https://github.com/HashVault/vltrig-proxy/releases)
[![GitHub license](https://img.shields.io/github/license/HashVault/vltrig-proxy)](https://github.com/HashVault/vltrig-proxy/blob/master/LICENSE)

A fork of [XMRig Proxy](https://github.com/xmrig/xmrig-proxy) tailored for [HashVault](https://hashvault.pro) mining pools.

> **Anti-censorship first.** Helping miners bypass network restrictions and DNS blocking that prevent access to mining pools. Mining should be accessible to everyone, everywhere.

### Focus Areas

- Anti-censorship features
- UI/UX improvements
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
[Miner 1] ──┐
[Miner 2] ──┼──> [vltrig-proxy] ──> [Pool]
[Miner N] ──┘
```

**Benefits:**
- Reduces pool-side connections (100,000 miners → ~400 pool connections)
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
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
```

Binary output: `build/vltrig-proxy`

---

## Versioning

Version format: **`X.Y.Z.P`**

| Part | Description |
|------|-------------|
| `X.Y.Z` | Upstream XMRig Proxy version |
| `.P` | vltrig-proxy patch number (continuous) |

```
XMRig Proxy 6.24.0 → vltrig-proxy 6.24.0.1 → 6.24.0.2 → 6.24.0.3
XMRig Proxy 6.25.0 → vltrig-proxy 6.25.0.4 → 6.25.0.5
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
