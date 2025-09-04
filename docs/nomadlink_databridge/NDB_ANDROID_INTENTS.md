# NomadLink-DataBridge — Android Intents Reference  
**Author:** Aaron Dean Whitman (2025)  
**Project:** NomadLink-MIPA / Exoform  

---

## Purpose
Define **public Android intents and helper commands** for switching between **Yggdrasil** and **Invizible Pro** on an Android phone.  
This enables a one-tap toggle (via Termux + Termux:Widget or Tasker) to change active overlay network.

---

## 1. Yggdrasil Android App
- Package name: `net.yggdrasil.android` (varies by build)  
- Common start intent:  
  am start -n net.yggdrasil.android/.MainActivity  
- Stop service (if exposed):  
  am stopservice net.yggdrasil.android/.YggdrasilService  
- Config reload (if supported):  
  am broadcast -a net.yggdrasil.RELOAD_CONFIG  

---

## 2. Invizible Pro (Tor/I2P/DNSCrypt)
- Package name: `pan.alexander.tordnscrypt`  
- Start all services:  
  am start -n pan.alexander.tordnscrypt/.MainActivity  
- Stop all services:  
  am force-stop pan.alexander.tordnscrypt  
- Optional individual toggles (Tor, I2P, DNSCrypt) may be available via sub-activities.  

---

## 3. Helper script (Termux)
Sample `ndb_phone_switch.sh` logic:

#!/data/data/com.termux/files/usr/bin/bash
MODE="$1"

if [ "$MODE" = "ygg" ]; then
  am force-stop pan.alexander.tordnscrypt
  am start -n net.yggdrasil.android/.MainActivity
  echo "Switched to Yggdrasil"
elif [ "$MODE" = "inviz" ]; then
  am stopservice net.yggdrasil.android/.YggdrasilService
  am start -n pan.alexander.tordnscrypt/.MainActivity
  echo "Switched to Invizible Pro"
else
  echo "Usage: ndb_phone_switch.sh [ygg|inviz]"
fi

Make it executable in Termux:  
chmod +x ~/bin/ndb_phone_switch.sh  

Then add as a widget/tile using **Termux:Widget** or a Tasker shortcut.  

---

## 4. Notes
- These commands assume both apps expose standard Android intents.  
- Some builds may require using `monkey` or simulated input instead.  
- No reverse engineering is required; only **public intents/UI automation**.  

---

## 5. Attribution
NomadLink-DataBridge Android intents © Aaron Dean Whitman (2025).  
Released under Exoform × Highland Ember open license.
