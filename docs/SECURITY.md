# Security & Safety Guidelines  
**Repo:** NomadLink-MIPA (Exoform × Highland Ember)  
**Author:** Aaron Dean Whitman (2025)  

---

## 1. Purpose
This document defines the **security, safety, and ethical boundaries** of the Exoform project.  
The design is **open-source** but must remain aligned with survival, exploration, and constructive use cases.

---

## 2. Safety Principles
- All actuator pods default to **zero torque** if communication is lost.  
- Every pod includes a **fail-safe brake**.  
- Hardware E-STOP is mandatory in all builds.  
- ROS 2 safety supervisor must always be active before enabling power.  
- Thermal, overcurrent, and positional limits enforced in firmware.  

---

## 3. Security Principles
- Use **signed firmware** on MCUs and SBCs where possible.  
- CAN/Ethernet nodes must validate message CRCs and discard invalid data.  
- Logs are written to **immutable CSV** for forensic traceability.  
- Pilot authentication (optional) may use biometric or hardware token to prevent unauthorized use.  

---

## 4. Ethical Boundaries
- The Exoform × Highland Ember projects are released under an **open license**.  
- They are **not intended for weaponization**.  
- The license does not restrict modification, but all derivative authors bear responsibility for their choices.  
- The cultural layer (Highland Ember) exists to remind that this technology is more than a machine — it is part of a **human story**.  

---

## 5. Incident Reporting
- Users and contributors should report security or safety issues via GitHub Issues.  
- Include logs (`/var/log/exoform_*.csv`) when relevant.  
- Issues must be documented openly — no private “black-box” fixes.  

---

## 6. Attribution
Security and safety guidelines © Aaron Dean Whitman (2025).  
Released under the Exoform × Highland Ember license.  
Credit required: **“Exoform × Highland Ember (Whitman, 2025)”**
