# Exoform — Technical Overview
**Project:** NomadLink-MIPA / Exoform  
**Author:** Aaron Dean Whitman (2025)  

---

## 1. Purpose
This document provides a master index of Exoform modules, linking technical components together under the NomadLink-MIPA architecture.  
It is the technical parallel to the Highland Ember declaration.

---

## 2. Architecture Layers
- **Actuation (EM-Muscle)** — powered joint pods (rotary + linear).  
- **Input Devices** — knuckle glove, EMG, IMU-based pilot interfaces.  
- **Power Systems** — LiFePO₄ packs, smart BMS, CAN telemetry.  
- **Control Nodes** — ROS 2 graph, safety supervisor, joint managers.  
- **Perception** — 360° camera array, stereo depth, terrain classification.  
- **Cognitive** — DarkGPT + EnhancedAI adaptive layers.  
- **Integration** — Suit-wide coordination through NomadLink-MIPA fabric.  

---

## 3. Current Modules
- `modules/em_muscle/EM_MUSCLE_DECLARATION.md`  
- `modules/em_muscle/EM_MUSCLE_SPEC.md`  
- `modules/em_muscle/EM_MUSCLE_BOM.csv`  
- `scripts/em_muscle_control_node.py`  
- `docs/EM_MUSCLE_TEST_PLAN.md`  
- `docs/EM_MUSCLE_INTEGRATION.md`  

---

## 4. Planned Modules
- **Leg Assembly** — hip, knee, ankle pods with stabilizers.  
- **Arm Assembly** — shoulder, elbow, wrist pods.  
- **Hand Assembly** — mechanical glove pods.  
- **Torso/Spine** — load-bearing pods and balance assist.  
- **Vision** — multi-camera + stereo modules.  
- **AI** — DarkGPT learner and EnhancedAI gate.  

---

## 5. Cross-Link with Highland Ember
For symbolic and cultural linkage, see:  
- `/docs/highland_ember/HIGHLAND_EMBER_DECLARATION.md`  
- `/docs/highland_ember/HIGHLAND_EMBER_MYTHOS.md`  
- `/docs/highland_ember/HIGHLAND_EMBER_SYMBOLS.md`  
- `/docs/highland_ember/HIGHLAND_EMBER_LINKS.md`  

---

## 6. Attribution
Exoform (Whitman, 2025) is © Aaron Dean Whitman.  
Freely usable under the Exoform open license with attribution.
