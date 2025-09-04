# NomadLink-MIPA / Exoform Architecture  
**Author:** Aaron Dean Whitman (2025)  

---

## 1. Purpose
This document describes the high-level architecture of the Exoform powered exosuit under the NomadLink-MIPA framework, including technical modules, AI layers, and cultural integration.

---

## 2. System Layers
- **Mechanical Layer:** Actuator pods, joints, suit frame.  
- **Electrical Layer:** Batteries, BMS, power bus, cabling.  
- **Control Layer:** ROS 2 graph, safety supervisor, joint controllers.  
- **Perception Layer:** Cameras, IMUs, EMG sensors, glove input.  
- **Cognitive Layer:** DarkGPT (learner) + EnhancedAI (safety gate).  
- **Cultural Layer:** Highland Ember narratives, symbols, branding.  

---

## 3. Networking
- **Joint Tier:** CAN-FD bus at 1 Mbps+ for actuator pods.  
- **Segment Tier:** Ethernet ROS 2 for torso/limbs coordination.  
- **Brain Tier:** NomadLink-MIPA distributed compute fabric (multi-device).  

---

## 4. AI Integration
- **DarkGPT:** Learns pilot intent from motion/EMG/glove data.  
- **EnhancedAI:** Supervises and prevents unsafe actions.  
- Together: Adaptive “Jarvis/Stark” interdependence.  

---

## 5. Safety Model
- Hardware E-STOP on suit.  
- Each pod has fail-safe brake.  
- ROS 2 supervisor enforces safe commands only.  
- AI layers never bypass safety.  

---

## 6. Cultural Overlay
- Exoform = technical skeleton.  
- Highland Ember = symbolic skeleton.  
- Every technical module is paired with a symbolic counterpart (see `HIGHLAND_EMBER_LINKS.md`).  

---

## 7. Roadmap Tie-In
- Matches `docs/ROADMAP.md` for convergence points.  
- Tracks parallel development of hardware + narrative.  

---

## 8. Attribution
Architecture design © Aaron Dean Whitman (2025).  
Released under the open Exoform × Highland Ember license.  
Credit required: **“Exoform × Highland Ember (Whitman, 2025)”**
