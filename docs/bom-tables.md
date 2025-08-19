





---


## `docs/bom-tables.md`
```markdown
# Bills of Materials (BOM) — NomadLink MIPA
**Created by Aaron Dean Whitman**


These tables are generic starting points. Substitute equivalent components as needed.


## Bike Nano-Zone
| Component | Spec / Notes | Qty |
|--------------------|-----------------------------------|-----|
| PV Panel | 100W foldable, 18V nominal | 1 |
| MPPT Controller | 10A, ≤8 mA idle | 1 |
| Battery | 12V LFP, 10–20Ah, with BMS | 1 |
| Fuse (main) | 15A blade | 1 |
| USB-C PD Hub | 60–100W, 12V input | 1 |
| LED rail (optional)| 12V LED strip/lamps | 1 |
| Cables/Connectors | XT60/SAE, fused leads | set |


## Bike Propulsion Charge Path
| Component | Spec / Notes | Qty |
|--------------------|-----------------------------------|-----|
| PV Panel | 100–160W foldable | 1 |
| Solar Charger | MPPT→CC/CV at pack voltage | 1 |
| Battery (motor) | 36V/48V e-bike pack, 7–10Ah | 1 |
| Fuse | 20–30A near pack | 1 |
| Cables | Distinct connectors (e.g. Anderson vs XT60) | set |


## Van Zones (per zone)
| Component | Spec / Notes | Qty |
|--------------------|-----------------------------------|-----|
| PV Panel | 100W removable/tiltable | 1 |
| MPPT Controller | 10–15A, low idle | 1 |
| Battery | 12V LFP, 20Ah (lights) or 50Ah (fridge) | 1 |
| Fuse block | 3–10A fuses | 1 |
| USB-C PD Hub | 60–100W | 1 |
| 12V Loads | LED strips, pumps, fans | as req |
| Cables/Connectors | Short 12–14 AWG, XT60/Powerpole | set |


## Apartment Unit-Grid
| Component | Spec / Notes | Qty |
|--------------------|-----------------------------------|-----|
| PV Array | BIPV, 400–1200W | 1 |
| MPPT Controller | 20–40A | 1 |
| Battery Stack | 48V LFP, 1–4 kWh, swappable modules | 1+ |
| DC/DC Converter | 48→12V, 20–40A | 1 |
| USB-C PD Hub | 100W+ | 1 |
| Inverter (opt) | 48V→AC, low idle, 500–1000W | 1 |
| Isolated Coupler | 48V BiDir, manual enable | 1 |


## Floor Cluster-Grid
| Component | Spec / Notes | Qty |
