# EM-Muscle Integration into Exoform Architecture
**Project:** NomadLink-MIPA / Exoform  
**Module:** EM-Muscle  
**Author:** Aaron Dean Whitman (2025)  

---

## 1. Purpose
This document explains how the EM-Muscle module integrates into the full Exoform powered exosuit. It defines connections between mechanical pods, power systems, ROS 2 nodes, and NomadLink-MIPA’s distributed intelligence.

---

## 2. System Context
**Exoform Layers:**
1. **Mechanical:** Struts, joints, actuator pods.  
2. **Electrical:** Battery packs, BMS, CAN bus, fuses, wiring harness.  
3. **Software:** ROS 2 nodes, safety supervisor, gait planner, control nodes.  
4. **Cognitive:** Pilot interface (knuckle glove, IMU, EMG), DarkGPT planner, EnhancedAI gate.  

EM-Muscle fits at the boundary between **Mechanical** and **Software** layers.

---

## 3. Interfaces
- **Upstream Inputs:**  
  - `/exo/<joint>/cmd_deg_safe` (from safety supervisor).  
  - `/exo/intent_pose` (from IMU).  
  - `/exo/hand/knuckle_cmd_safe` (from glove).  

- **Outputs:**  
  - `/exo/joint_states` (feedback to pilot & AI layers).  
  - `/exo/hand/state` (finger feedback).  
  - `/exo/safety/fault` (on error).  

---

## 4. Power Integration
- Each EM-Muscle pod draws from the 48–72 V LiFePO₄ bus.  
- BMS publishes voltage/current/temp on CAN → bridged to ROS.  
- Pods fail safe on undervoltage or overcurrent.  

---

## 5. Cognitive Integration
- **DarkGPT:** Learns pilot intent patterns from hand, gait, and EMG signals.  
- **EnhancedAI:** Gates autonomy, preventing unsafe actions, while allowing assistance.  
- Both layers consume `/exo/joint_states` and `/exo/intent` → produce suggested modulation to gait planner.  

---

## 6. Deployment Steps
1. Validate EM-Muscle pods individually with `EM_MUSCLE_TEST_PLAN.md`.  
2. Add pods to leg assembly → verify walking gait in simulation.  
3. Enable IMU/knuckle glove control → validate with pilot-in-loop.  
4. Integrate DarkGPT/EnhancedAI nodes → verify assistance.  
5. Full suit assembly → phased integration (lower body → upper body → arms → full).  

---

## 7. Notes
- All modules remain **replaceable pods**; no hard dependencies.  
- Safety supervisor always overrides AI suggestions.  
- Logs must be archived for traceability at each step.  

— End of Integration Doc —
