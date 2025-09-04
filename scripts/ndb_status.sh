#!/usr/bin/env bash
# NomadLink-DataBridge status helper (laptop)
# Shows Yggdrasil interface/address and basic reachability.

set -e

iface="${1:-ygg0}"

if ! ip link show "$iface" >/dev/null 2>&1; then
  echo "[NDB] Interface $iface not found."
  exit 1
fi

addr=$(ip -6 addr show "$iface" | awk '/inet6/{print $2}' | head -n1)
echo "[NDB] Interface: $iface"
echo "[NDB] Address  : ${addr:-none}"

# Try to ping a well-known Ygg address if provided via env NDB_PING6
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

exit 0
