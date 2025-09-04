# Electromagnetic Muscle (EM-Muscle) — Technical Specification
**Project:** NomadLink-MIPA / Exoform  
**Module:** EM-Muscle  
**Author:** Aaron Dean Whitman  
**Version:** v0.1  

---

## 1. Overview
The EM-Muscle module defines the actuation layer of the Exoform suit.  
It provides rotary and linear actuators, designed with **commercially available parts** (BLDC motors, gear reductions, elastic couplers, brakes) to mimic natural human muscle function.

---

## 2. Architecture
- **Compute Tiers**
  - Joint Controller: STM32/ESP32 with FOC firmware (VESC-class).
  - Segment SBC: Raspberry Pi/ROCK single-board computer with ROS 2 nodes.
  - Brain Tier: NomadLink-MIPA distributed AI (DarkGPT/EnhancedAI layers).
- **Networking**
  - CAN-FD at 1 Mbps+ for joint loops.
  - Ethernet ROS 2 backbone for coordination.
- **Power**
  - 48–72 V LiFePO₄ packs.
  - Smart BMS with CAN telemetry.
  - Hot-swappable pods.

---

## 3. Actuator Pods
- **Rotary Pods** (shoulder, elbow, wrist, hip, knee, ankle)
  - BLDC + strain-wave or planetary gearbox.
  - Series-elastic coupler for torque sensing.
  - Integrated brake for fail-safe stop.
- **Linear Pods**
  - Ballscrew or linear EM drive.
  - Used for spine assist, chest expansion, or heavy lift modules.

---

## 4. Sensors
- Encoders: magnetic absolute (AS5047/AS5600).
- Force: series elasticity deflection + load cells.
- Foot plates: HX711 strain-gauge bridges.
- IMUs: 9DoF (MPU-9250, BMI-160).
- EMG (optional): pilot intent mapping.

---

## 5. Safety Systems
- Hardware E-STOP cuts bus power.
- Brake-on-fault at each joint.
- Thermal and overcurrent derating in firmware.
- Mechanical stops at joint limits.
- Watchdog at ROS 2 supervisor node.

---

## 6. ROS 2 Interfaces
- **Commands**
  - `/exo/<joint>/cmd_deg_safe` → Position target (Float32).
- **States**
  - `/exo/joint_states` → Joint angles.
  - `/exo/hand/state` → Finger positions.
  - `/exo/power/bms` → Voltage/current/temp.
- **Safety**
  - `/exo/safety/fault` → Bool.
  - `/exo/hand/knuckle_cmd_safe` → Filtered glove inputs.

---

## 7. Minimal Test Build
- Single joint pod (bench mount).
- Controlled via ROS 2 loop (knuckle glove optional).
- Verify:
  - Encoder feedback.
  - Torque/current limits.
  - Brake engage on fault.
  - Logging to `/var/log/exoform_*.csv`.

---

## 8. Roadmap
- v0.1: Bench test pod.
- v0.2: Dual-joint integration (hip + knee).
- v0.3: Full leg assembly with compliance.
- v0.4: Upper-limb pods.
- v1.0: Full Exoform suit integration.

---

## 9. Attribution
All designs, code, and schematics are open-source under the Exoform License (Whitman 2025). Attribution: **“Exoform (Whitman, 2025)”**.
