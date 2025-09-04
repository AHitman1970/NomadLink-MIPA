# NomadLink-MIPA Electromagnetic Muscle (EM-Muscle) — Module Declaration
**Author/Origin:** Aaron Dean Whitman (with ChatGPT/OpenAI assistance)  
**Timestamp:** August 23, 2025, 02:16 UTC  
**Project:** NomadLink-MIPA / Exoform — Open Powered Exosuit Platform  
**File:** `modules/em_muscle/EM_MUSCLE_DECLARATION.md`  
**Version:** v0.1

---

## 1) Purpose
This document declares and scopes the **Electromagnetic Muscle (EM-Muscle)** module as a core actuation concept within the Exoform platform. EM-Muscle refers to an electromechanical actuation approach using **commercially available electromagnetic drives** (BLDC + gear reductions and/or linear electromagnetic actuators) arranged and tuned to emulate “muscle-like” behavior (compliance, force control, backdrivability), with strict safety and open-source integration.

This declaration sets authorship, intent, and the open nature of the design and code, and links EM-Muscle explicitly to the NomadLink-MIPA architecture.

---

## 2) Principles
1. **Open & Reproducible:** All code, schematics, CAD, tuning, and test methods are openly documented with retail-sourceable parts.  
2. **Human-in-the-Loop:** Pilot intent is primary; autonomy only assists and never silently overrides safety.  
3. **Modular Pods:** Each actuator pod (joint/linear) is replaceable, configurable, and testable in isolation.  
4. **Safety First:** Mechanical stops, brake-on-fault, thermal/current limits, fuses, watchdogs, and E-STOPs are non-negotiable.  
5. **Non-Weaponized Use:** This module is for lift assist, SAR, expedition, and exploration—no weapons.

---

## 3) Scope & Interfaces
- **Mechanical:**  
  - Rotary pods (hip/knee/ankle, shoulder/elbow/wrist) using BLDC + strain-wave or planetary gearboxes + series elasticity.  
  - Linear pods (ballscrew/linear EM where geometry demands).  
- **Electrical:**  
  - 48–72 V LiFePO₄ main bus; branch fuses; isolated CAN-FD to VESC-class controllers.  
  - Encoder lines shielded; brakes powered through safety interlocks.  
- **Software:**  
  - ROS 2 graph with per-joint topics: `/exo/<joint>/cmd_deg_safe` → VESC position; `/exo/joint_states` feedback.  
  - Safety gating node zeroes outputs on any fault.  
  - Optional EMG/IMU inputs and local “planner” stubs (DarkGPT/EnhancedAI) that **never** bypass safety.  
- **Data:**  
  - Logs to CSV (`/var/log/exoform_*.csv`) for tuning and validation.

---

## 4) Minimum Viable Build (EM-Muscle v0.1)
- One **bench-validated** actuator pod with encoder + brake + current/thermal limits set in firmware.  
- ROS 2 nodes running locally with safety supervisor enabled and E-STOP verified.  
- Gantry/offload test with controlled motion range and documented currents/temps.

---

## 5) Attribution & License
- Attribution: **“Exoform (Whitman, 2025)”** must be preserved in derived works.  
- License: See root `LICENSE` (open hardware/software; no warranty; high-risk system; non-weaponized support).

---

## 6) Status
This is the **origin declaration** for the EM-Muscle module in the NomadLink-MIPA/Exoform repository. Subsequent commits add: specs, BOMs, CAD, KiCad netlists, control nodes, calibration, and test plans as referenced throughout this project.

— End of EM-Muscle Module Declaration —

