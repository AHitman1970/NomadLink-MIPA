# NomadLink-DataBridge (NDB)
**Project:** NomadLink-MIPA / Exoform  
**Author:** Aaron Dean Whitman (2025)  
**Scope:** Seamless phone ↔ laptop link across any network/geo using Yggdrasil IPv6 overlay, with optional Tor/I2P fallbacks and a one-tap switch on Android between **Invizible Pro** (Tor/I2P/DNSCrypt) and **Yggdrasil**.  
**Status:** Design + reference configs + control scripts (cross-platform, open-source only)

---

## 1) Purpose
Provide a resilient, privacy-respecting data bridge so your **phone** and **laptop** remain reachable end-to-end regardless of carrier NAT, Wi-Fi captivity, or location. Core transport is **Yggdrasil (IPv6 overlay, E2E encrypted)**, with an Android toggle to switch between **Yggdrasil** and **Invizible Pro** (Tor/I2P/DNSCrypt stack) for alternate paths.

---

## 2) Architecture (high level)

[Phone: Android]
├── Yggdrasil Android (ygg A) ←─ one-tap toggle ─→ Invizible Pro (Tor/I2P/DNSCrypt)
├── Termux helper scripts ←─ start/stop status hooks
└── Wire/SSH apps use ::/ygg

[Overlay: Yggdrasil IPv6 mesh]
└── Encrypted point-to-point sockets; stable node keys/addresses

[Laptop: Linux]
├── yggdrasil.service (systemd)
├── systemd user services for NDB helpers
└── OpenSSH bound to ygg0 (optional)


---

## 3) Modes
- **Direct (Preferred)**: Phone ↔ Laptop via Yggdrasil (::/7 address space, global overlay).  
- **Fallback A (Privacy/Routing)**: Phone routes via **Invizible Pro** (Tor/I2P). App-level tools continue to work; Ygg can be off.  
- **Fallback B (Carrier/Firewall Hostile)**: Phone on Tor/I2P only, laptop reachable over Tor-enabled apps (no Ygg).

---

## 4) Android one-tap switch (concept)
- Uses **Termux** + optional **Tasker**/**Termux:Widget** to call shell helpers:
  - `ndb_phone_switch.sh ygg` → stops Invizible Pro stack (via intents), starts Yggdrasil.
  - `ndb_phone_switch.sh inviz` → stops Yggdrasil, starts Invizible Pro.
- We do **not** modify proprietary apps. We use **public Android intents** and the Yggdrasil app’s exposed actions (if present) or fallback to `am startservice`/`am start` intents.

> Note: “Invizible Pro” is a third-party Android app bundling Tor, I2P, DNSCrypt. We reference only **public intents/UI automation**; no reverse-engineering here.

---

## 5) Laptop services
- `yggdrasil.service` (systemd) brings up `ygg0` at boot.  
- `ndb_ygg_guard.service` (user service) ensures reachable SSH on the ygg address.  
- Optional `~/.ssh/config` stanza to prefer Yggdrasil when present.

---

## 6) Security posture
- Yggdrasil: key-based node identity, E2E encrypted overlay.  
- SSH: key-only auth; bind/interface restrict to ygg0 if desired.  
- Tor/I2P via Invizible Pro: app-level privacy routes (no changes to those apps).  
- No packet injection, no network exploitation. Strictly user-owned connectivity.

---

## 7) What’s included in this module
- `configs/yggdrasil.conf.template` — reference base for phone/laptop.  
- `systemd/` — laptop unit files (`yggdrasil.service`, `ndb_ygg_guard.service`).  
- `scripts/` — cross-platform helpers:
  - `ndb_switch.sh` (laptop): quick toggle/check.  
  - `ndb_phone_switch.sh` (Android/Termux): one-tap Ygg ↔ Invizible Pro.  
  - `ndb_status.sh` (both): prints state and ygg addresses.
- `NDB_ANDROID_INTENTS.md` — public intent URIs and fallbacks for Yggdrasil + Invizible Pro.

---

## 8) Minimal usage (concept)
1. Install Yggdrasil on laptop; drop in `yggdrasil.conf` from template; enable service.  
2. Install Yggdrasil Android + Termux (and optionally Invizible Pro).  
3. Copy `ndb_phone_switch.sh` into Termux `~/bin`, make executable; add Termux:Widget tile.  
4. Tap **Ygg** tile on phone → phone and laptop get stable ygg addresses → SSH/rsync/whatever over overlay.

---

## 9) Attribution
NomadLink-DataBridge © Aaron Dean Whitman (2025).  
Released under Exoform × Highland Ember open license with attribution.


---

**After you save/exit**, run:

```bash
git add modules/nomadlink_databridge/NOMADLINK_DATABRIDGE.md
git commit -m "feat(ndb): add NomadLink-DataBridge module declaration and design"
git push

