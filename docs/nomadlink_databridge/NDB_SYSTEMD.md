# NomadLink-DataBridge — Laptop + Phone Integration (Single Reference)
Project: NomadLink-MIPA / Exoform  
Author: Aaron Dean Whitman (2025)

This is repository documentation only. Do not run anything yet.  
It embeds all related units and scripts verbatim so you can copy them later.

---

## 1) Purpose
Keep phone ↔ laptop linked over hostile networks using Yggdrasil (IPv6 overlay) with an Android one-tap switch between Yggdrasil and Invizible Pro (Tor/I2P/DNSCrypt).  
This doc centralizes the laptop systemd units, the status helper, and the phone Termux switch script + intents.

---

## 2) Directory map (in this repo)
- systemd/yggdrasil.service — system unit (laptop)  
- systemd/user/ndb_ygg_guard.service — user unit (laptop)  
- scripts/ndb_status.sh — status helper (laptop)  
- scripts/ndb_phone_switch.sh — Termux switch script (phone, stored here as reference)  
- configs/yggdrasil.conf.template — Yggdrasil config template (both)

---

## 3) Laptop: systemd units (embedded copies)

### 3.1 systemd/yggdrasil.service
[Unit]  
Description=Yggdrasil encrypted IPv6 overlay (NomadLink-DataBridge)  
After=network-online.target  
Wants=network-online.target  

[Service]  
Type=simple  
ExecStart=/usr/bin/yggdrasil -useconffile /etc/yggdrasil/yggdrasil.conf  
Restart=on-failure  
RestartSec=3  
NoNewPrivileges=true  
PrivateDevices=true  
ProtectSystem=full  
ProtectHome=true  
ProtectControlGroups=true  
ProtectKernelTunables=true  
ProtectKernelModules=true  
ProtectClock=true  
MemoryDenyWriteExecute=true  
LockPersonality=true  

[Install]  
WantedBy=multi-user.target  

### 3.2 systemd/user/ndb_ygg_guard.service
[Unit]  
Description=NomadLink-DataBridge guard (ensures Yggdrasil overlay presence, prints status)  
After=default.target  

[Service]  
Type=simple  
ExecStart=%h/NomadLink-MIPA/scripts/ndb_status.sh  
Restart=on-failure  
RestartSec=10  

[Install]  
WantedBy=default.target  

### 3.3 scripts/ndb_status.sh
#!/usr/bin/env bash  
# NomadLink-DataBridge status helper (laptop)  
set -e  
iface="${1:-ygg0}"  

if ! ip link show "$iface" >/dev/null 2>&1; then  
  echo "[NDB] Interface $iface not found."  
  exit 1  
fi  

addr=$(ip -6 addr show "$iface" | awk '/inet6/{print $2}' | head -n1)  
echo "[NDB] Interface: $iface"  
echo "[NDB] Address  : ${addr:-none}"  

if [[ -n "$NDB_PING6" ]]; then  
  echo "[NDB] Pinging $NDB_PING6 ..."  
  if ping -6 -c 2 -I "$iface" "$NDB_PING6" >/dev/null 2>&1; then  
    echo "[NDB] Reachable."  
  else  
    echo "[NDB] Not reachable."  
  fi  
else  
  echo "[NDB] (Set NDB_PING6=your_peer_ygg_addr to test reachability)"  
fi  

---

## 4) Phone: Termux switch + public intents

### 4.1 scripts/ndb_phone_switch.sh (store on phone under Termux ~/bin/ when you actually use it)
#!/data/data/com.termux/files/usr/bin/bash  
# One-tap switch between Yggdrasil and Invizible Pro on Android  
MODE="$1"  

start_ygg() {  
  am force-stop pan.alexander.tordnscrypt 2>/dev/null  
  am start -n net.yggdrasil.android/.MainActivity  
  echo "[NDB] Switched to Yggdrasil"  
}  

start_inviz() {  
  am stopservice net.yggdrasil.android/.YggdrasilService 2>/dev/null  
  am start -n pan.alexander.tordnscrypt/.MainActivity  
  echo "[NDB] Switched to Invizible Pro"  
}  

case "$MODE" in  
  ygg)   start_ygg ;;  
  inviz) start_inviz ;;  
  *)  
    echo "Usage: ndb_phone_switch.sh [ygg|inviz]"  
    exit 2  
    ;;  
esac  

Make executable when you deploy on phone:  
chmod +x ~/bin/ndb_phone_switch.sh  

### 4.2 Public Android intents (reference)
Yggdrasil (package may vary):  
- am start -n net.yggdrasil.android/.MainActivity  
- am stopservice net.yggdrasil.android/.YggdrasilService  
- am broadcast -a net.yggdrasil.RELOAD_CONFIG  

Invizible Pro (Tor/I2P/DNSCrypt):  
- am start -n pan.alexander.tordnscrypt/.MainActivity  
- am force-stop pan.alexander.tordnscrypt  

---

## 5) Yggdrasil config template (both) — configs/yggdrasil.conf.template
NomadLink-DataBridge — Yggdrasil Config Template  
PrivateKey: <YOUR_PRIVATE_KEY>  
PublicKey: auto  

Listen:  
  - tcp://0.0.0.0:0  
  - unix:///var/run/yggdrasil.sock  

Peers:  
  - tls://yggdrasil-bootstrap-1.example.org:443  
  - tls://yggdrasil-bootstrap-2.example.org:443  
  # Add your own peer(s) here  

MulticastInterfaces:  
  - Regex: ".*"  
    Beacon: true  
    Listen: true  

AdminListen: unix:///var/run/yggdrasil-admin.sock  

SessionFirewall:  
  Enable: true  
  AllowFrom:  
    - ::/0  

TunnelRouting:  
  Enable: false  

---

## 6) Notes / Safety / Scope
- This page is docs-only for the repository.  
- Units and scripts above are embeds so you can copy them later; they do not auto-run.  
- Overlay is end-to-end encrypted (Yggdrasil). Use SSH keys if you later bind services to ygg0.  

---

## 7) Attribution
NomadLink-DataBridge © Aaron Dean Whitman (2025).  
Released under the Exoform × Highland Ember open license (attribution required).

