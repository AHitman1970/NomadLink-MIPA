# EM-Muscle Module — Test Plan & Safety Checklist
**Project:** NomadLink-MIPA / Exoform  
**Module:** EM-Muscle  
**Author:** Aaron Dean Whitman (2025)  

---

## 1. Objective
Define a repeatable test procedure to validate EM-Muscle pods before integration into the full Exoform suit.

---

## 2. Pre-Test Checklist
- [ ] Verify wiring polarity and insulation.  
- [ ] Verify encoder alignment and zero calibration.  
- [ ] Confirm brake engages when unpowered.  
- [ ] Confirm ROS 2 safety supervisor node is running.  
- [ ] E-STOP wired, tested, and reachable.  
- [ ] Logging path `/var/log/exoform_*.csv` available.  

---

## 3. Bench Test Procedure
1. Mount EM-Muscle pod securely on gantry or test rig.  
2. Power on BMS and check voltage/current telemetry (`/exo/power/bms`).  
3. Send small amplitude sine wave (±5°) to joint via `/cmd_deg_safe`.  
4. Verify encoder feedback in `/joint_states`.  
5. Increase amplitude to 25–30% of joint limit.  
6. Measure pod temperature and current draw.  
7. Trigger E-STOP → verify immediate brake engage and zero torque.  
8. Log and save results.  

---

## 4. Safety Validation
- [ ] Current limits enforced (no overshoot > 10%).  
- [ ] Thermal derating at ≥80 °C.  
- [ ] Hard stop prevents over-rotation.  
- [ ] Fault → brake engaged < 100 ms.  
- [ ] ROS supervisor flags fault.  

---

## 5. Acceptance Criteria
Pod is safe for integration if:  
- Encoder error < 1°.  
- Current draw within spec (< continuous rating).  
- Thermal steady-state < 75 °C.  
- Fault recovery tested successfully.  

---

## 6. Notes
- Always test new firmware on a **single pod** first.  
- Maintain written logs for reproducibility.  
- Never bypass E-STOP or fault gating for tests.  

— End of EM-Muscle Test Plan —
