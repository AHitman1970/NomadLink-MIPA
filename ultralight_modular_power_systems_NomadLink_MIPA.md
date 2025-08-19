# NomadLink Modular Independent Power Architecture (MIPA)
**Created by Aaron Dean Whitman**

---

# Repository Starter Files

## `README.md`
```markdown
# NomadLink MIPA
**NomadLink Modular Independent Power Architecture**  
**Created by Aaron Dean Whitman**

> Open‑source, modular, zone‑based renewable power architecture — from bicycle to skyscraper — designed to operate fully islanded with optional, user‑controlled interties (aka “shore power”).

## What is NomadLink MIPA?
NomadLink MIPA is an **open hardware architecture** for building **independent power zones** that can run standalone or connect temporarily to share energy. Each zone has its own renewable source(s), storage, and point‑of‑load distribution (DC‑first; AC only where necessary). Control is **tenant/user‑owned** via BLE/Thread; the system functions without cloud or building Wi‑Fi.

## Key Principles
- **Zones, not monoliths**: Each area/device cluster is its own micro‑grid.
- **Optional tethering**: Manual/isolated interties only when you choose.
- **DC‑first**: 48→12 V and USB‑C PD at the edge; inverters are off by default.
- **Near‑zero idle**: Hardware that truly sleeps; no vampire loads.
- **Scalable**: Bike → van → apartment → floor → tower.
- **Open & attributable**: Free to use/adapt with required credit.

## Quick Start
1. Pick a **zone** (e.g., van galley) and size: 100 W PV + 12 V 20–50 Ah LFP.
2. Use a **low‑idle MPPT**, short fused DC runs, and a **USB‑C PD hub**.
3. Keep zones **islanded** by default. Add an **isolated B2B** only if you need to share.
4. Measure Wh/day with a wattmeter; adjust panel or Ah as needed.

## Repo Map
```
.
├── README.md
├── LICENSE.md                      # CERN-OHL-P v2.0 + attribution clause
├── docs/
│   ├── architecture-overview.md    # Philosophy, layers, safety
│   ├── schematic-bike.md           # Nano‑zone reference
│   ├── schematic-van.md            # Micro‑zones reference
│   ├── schematic-apartment.md      # Unit‑grid reference
│   ├── schematic-floor.md          # Cluster‑grid reference
│   └── schematic-tower.md          # Macro‑grid reference
└── schematics/                     # Diagrams (SVG)
```

## License & Attribution
Licensed under **CERN-OHL-P v2.0** with an **Attribution Requirement**:
> “NomadLink Modular Independent Power Architecture — Created by Aaron Dean Whitman”

See [`LICENSE.md`](./LICENSE.md) for full terms.
```

---

## `LICENSE.md`
```text
NomadLink Modular Independent Power Architecture (MIPA)
Created by Aaron Dean Whitman

License: CERN Open Hardware Licence Version 2 - Permissive (CERN-OHL-P v2)
Full text: https://ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2

— BEGIN ATTRIBUTION REQUIREMENT —
All copies, adaptations, and derivative works must include the credit line:
“NomadLink Modular Independent Power Architecture — Created by Aaron Dean Whitman”
This credit must appear in documentation and, where technically feasible, in user interfaces or product labeling.
— END ATTRIBUTION REQUIREMENT —

— BEGIN CERN-OHL-P v2.0 SHORT FORM —
You may redistribute and modify this Documentation and make products using it under the terms of the CERN-OHL-P v2.
This Documentation is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY,
SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN-OHL-P v2 for applicable conditions.
— END CERN-OHL-P v2.0 SHORT FORM —

— NOTICES —
This repository may include trademarks (e.g., “NomadLink MIPA”). Trademarks are not licensed under CERN-OHL.
Use of the marks requires permission or fair-use compliance. The underlying technical documentation remains open as above.
```

---

## `docs/architecture-overview.md`
```markdown
# NomadLink MIPA — Architecture Overview
**Created by Aaron Dean Whitman**

## Purpose
Define a modular, independent power system built from **zones** that operate standalone and can be **optionally tethered** without parasitic loss. The architecture scales from **personal mobility** to **multi‑tenant towers** while keeping control **user‑owned** and radios **optional**.

## Design Tenets
1. **Zones**: Each zone = source(s) + storage + local DC distribution. 
2. **Optional Interties**: Isolated, manually enabled (or policy‑guarded) couplers; de‑energized when idle.
3. **DC‑First**: 48 V backbone where useful; 12 V and USB‑C PD at the edge; AC only for legacy loads.
4. **True Sleep**: Components chosen for sub‑milliamp quiescent where possible; hard power switches.
5. **User Sovereignty**: Tenant controls their zone locally (BLE/Thread); building ops read meters only.
6. **Safety by Simplicity**: Short fused runs, sectionalized buses, fail‑safe defaults, life‑safety on dedicated branches.

## Layered Topology
- **Nano-Zone (Bike)** → foldable PV, accessory LFP, e‑pack isolated, BLE lights.
- **Micro-Zone (Van)** → 100 W PV + 10–50 Ah LFP per area, PD hubs, optional B2B.
- **Unit-Grid (Apartment)** → BIPV 0.4–1.2 kW, 1–4 kWh storage, 48→12 V DC, AC optional.
- **Cluster-Grid (Floor)** → opt‑in 48 V DC ring, isolated bidir couplers, 10–50 kWh buffer.
- **Macro-Grid (Tower)** → BIPV + rooftop PV + elevator regen → 380 V DC backbone, MWh storage, optional grid intertie.

## Safety & Compliance
- **Fusing**: Main fuse ≤15 cm from battery positive; branch fuses at 125% of load.
- **Isolation**: Only isolated DC/DC for interties and risers; sectionalize backbones.
- **Life‑Safety**: Stairs/alarms/pumps on dedicated DC branches with independent batteries and wired control.
- **Fire & Chemistries**: Prefer LFP for stationary storage; provide temp monitoring and clearances per local code.

## Licensing & Credit
Open hardware under **CERN-OHL-P v2.0** with required attribution:
> “NomadLink Modular Independent Power Architecture — Created by Aaron Dean Whitman.”
```

---

## `docs/schematic-bike.md`
```markdown
# Schematic — Bike Nano-Zone

```svg
<svg width="500" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="20" width="100" height="40" fill="lightyellow" stroke="black"/>
  <text x="25" y="45">100W PV Panel</text>
  <line x1="120" y1="40" x2="200" y2="40" stroke="black" marker-end="url(#arrow)"/>

  <rect x="200" y="20" width="100" height="40" fill="lightblue" stroke="black"/>
  <text x="205" y="45">MPPT Controller</text>

  <line x1="300" y1="40" x2="380" y2="40" stroke="black" marker-end="url(#arrow)"/>
  <rect x="380" y="20" width="100" height="40" fill="lightgreen" stroke="black"/>
  <text x="385" y="45">12V LFP Battery</text>

  <line x1="430" y1="60" x2="430" y2="100" stroke="black" marker-end="url(#arrow)"/>
  <rect x="360" y="100" width="140" height="40" fill="pink" stroke="black"/>
  <text x="365" y="125">USB-C PD Hub → Lights/Phone</text>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="black"/>
    </marker>
  </defs>
</svg>
```
```

---

## `docs/schematic-van.md`
```markdown
# Schematic — Van Micro-Zones

```svg
<svg width="600" height="250" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="20" width="100" height="40" fill="lightyellow" stroke="black"/>
  <text x="25" y="45">100W PV</text>
  <line x1="120" y1="40" x2="200" y2="40" stroke="black" marker-end="url(#arrow)"/>

  <rect x="200" y="20" width="120" height="40" fill="lightblue" stroke="black"/>
  <text x="205" y="45">MPPT (10–15A)</text>
  <line x1="320" y1="40" x2="400" y2="40" stroke="black" marker-end="url(#arrow)"/>

  <rect x="400" y="20" width="120" height="40" fill="lightgreen" stroke="black"/>
  <text x="405" y="45">12V LFP 20–50Ah</text>

  <line x1="460" y1="60" x2="460" y2="120" stroke="black" marker-end="url(#arrow)"/>
  <rect x="380" y="120" width="160" height="40" fill="pink" stroke="black"/>
  <text x="385" y="145">USB-C PD Hub / Lights / Pump</text>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="black"/>
    </marker>
  </defs>
</svg>
```
```

---

## `docs/schematic-apartment.md`
```markdown
# Schematic — Apartment Unit-Grid

```svg
<svg width="700" height="300" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="20" width="120" height="40" fill="lightyellow" stroke="black"/>
  <text x="25" y="45">BIPV/400–1200W</text>
  <line x1="140" y1="40" x2="220" y2="40" stroke="black" marker-end="url(#arrow)"/>

  <rect x="220" y="20" width="120" height="40" fill="lightblue" stroke="black"/>
  <text x="225" y="45">MPPT Controller</text>
  <line x1="340" y1="40" x2="420" y2="40" stroke="black" marker-end="url(#arrow)"/>

  <rect x="420" y="20" width="120" height="40" fill="lightgreen" stroke="black"/>
  <text x="425" y="45">48V Battery 1–4kWh</text>

  <line x1="480" y1="60" x2="480" y2="120" stroke="black" marker-end="url(#arrow)"/>
  <rect x="400" y="120" width="160" height="40" fill="pink" stroke="black"/>
  <text x="405" y="145">48→12V DC/DC → USB-C, Lights</text>

  <line x1="540" y1="60" x2="540" y2="200" stroke="black" marker-end="url(#arrow)"/>
  <rect x="460" y="200" width="160" height="40" fill="orange" stroke="black"/>
  <text x="465" y="225">48→AC Inverter (optional)</text>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="black"/>
    </marker>
  </defs>
</svg>
```
```

---

## `docs/schematic-floor.md`
```markdown
# Schematic — Floor Cluster-Grid

```svg
<svg width="700" height="300" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="20" width="120" height="40" fill="lightgreen" stroke="black"/>
  <text x="25" y="45">Floor Buffer Battery 10–50kWh</text>

  <line x1="80" y1="60" x2="80" y2="120" stroke="black" marker-end="url(#arrow)"/>
  <rect x="20" y="120" width="120" height="40" fill="lightblue" stroke="black"/>
  <text x="25" y="145">48V DC Ring Bus</text>

  <line x1="140" y1="140" x2="260" y2="140" stroke="black" marker-end="url(#arrow)"/>
  <rect x="260" y="120" width="120" height="40" fill="pink" stroke="black"/>
  <text x="265" y="145">Unit Coupler (Isolated)</text>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="black"/>
    </marker>
  </defs>
</svg>
```
```

---

## `docs/schematic-tower.md`
```markdown
# Schematic — Tower Macro-Grid

```svg
<svg width="900" height="400" xmlns="http://www.w3.org/2000/svg">
  <rect x="20" y="20" width="150" height="40" fill="lightyellow" stroke="black"/>
  <text x="25" y="45">Rooftop PV + BIPV</text>
  <line x1="170" y1="40" x2="270" y2="40" stroke="black" marker-end="url(#arrow)"/>

  <rect x="270" y="20" width="150" height="40" fill="lightblue" stroke="black"/>
  <text x="275" y="45">MPPT / Combiner</text>
  <line x1="420" y1="40" x2="520" y2="40" stroke="black" marker-end="url(#arrow)"/>

  <rect x="520" y="20" width="150" height="40" fill="lightgreen" stroke="black"/>
  <text x="525" y="45">380V DC Backbone</text>

  <line x1="595" y1="60" x2="595" y2="120" stroke="black" marker-end="url(#arrow)"/>
  <rect x="520" y="120" width="150" height="40" fill="pink" stroke="black"/>
  <text x="525" y="145">Battery Racks (MWh)</text>

  <line x1="670" y1="40" x2="800" y2="40" stroke="black" marker-end="url(#arrow)"/>
  <rect x="800" y="20" width="80" height="40" fill="orange" stroke="black"/>
  <text x="805" y="45">Grid Tie*</text>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="black"/>
    </marker>
  </defs>
</svg>
```
```

---



---

## `docs/schematic-bike.md`
```markdown
# Schematic — Bike Nano‑Zone
**NomadLink MIPA — Created by Aaron Dean Whitman**

This reference keeps accessories isolated from propulsion. All parts are examples; substitute any components that match the spec.

## Block Diagram (inline SVG)
> Save separately as `schematics/bike-nano.svg` if you prefer.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="420" viewBox="0 0 900 420">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" />
    </marker>
    <style>
      .box{fill:#fff;stroke:#000;stroke-width:2;}
      .title{font: bold 14px sans-serif;}
      .cap{font: 12px sans-serif;}
      .note{font: italic 11px sans-serif;}
      .line{stroke:#000;stroke-width:2;marker-end:url(#arrow);} 
    </style>
  </defs>

  <!-- Accessory island -->
  <rect class="box" x="40" y="30" width="380" height="160" rx="10"/>
  <text class="title" x="230" y="55" text-anchor="middle">Accessory Micro‑Grid (Island)</text>

  <rect class="box" x="60" y="80" width="120" height="50" rx="6"/>
  <text class="cap" x="120" y="110" text-anchor="middle">100W PV</text>

  <rect class="box" x="200" y="80" width="100" height="50" rx="6"/>
  <text class="cap" x="250" y="110" text-anchor="middle">MPPT 10A</text>

  <rect class="box" x="330" y="80" width="70" height="50" rx="6"/>
  <text class="cap" x="365" y="110" text-anchor="middle">12V LFP 10–20Ah</text>

  <line class="line" x1="180" y1="105" x2="200" y2="105"/>
  <line class="line" x1="300" y1="105" x2="330" y2="105"/>

  <rect class="box" x="200" y="150" width="100" height="30" rx="6"/>
  <text class="cap" x="250" y="170" text-anchor="middle">Fuse 15A main</text>
  <line class="line" x1="365" y1="105" x2="250" y2="165"/>

  <rect class="box" x="60" y="200" width="130" height="50" rx="6"/>
  <text class="cap" x="125" y="230" text-anchor="middle">USB‑C PD Hub 60–100W</text>
  <line class="line" x1="250" y1="165" x2="125" y2="225"/>

  <rect class="box" x="220" y="200" width="120" height="50" rx="6"/>
  <text class="cap" x="280" y="230" text-anchor="middle">12V LED rail*</text>
  <line class="line" x1="250" y1="165" x2="280" y2="225"/>
  <text class="note" x="280" y="260" text-anchor="middle">*omit if all BLE lights are self‑battery</text>

  <!-- Propulsion island -->
  <rect class="box" x="480" y="30" width="380" height="200" rx="10"/>
  <text class="title" x="670" y="55" text-anchor="middle">Propulsion Charge Path (Isolated)</text>

  <rect class="box" x="500" y="80" width="120" height="50" rx="6"/>
  <text class="cap" x="560" y="110" text-anchor="middle">100–160W PV</text>

  <rect class="box" x="640" y="80" width="120" height="50" rx="6"/>
  <text class="cap" x="700" y="110" text-anchor="middle">MPPT→CC/CV</text>

  <rect class="box" x="780" y="80" width="60" height="50" rx="6"/>
  <text class="cap" x="810" y="110" text-anchor="middle">36/48V e‑pack</text>

  <line class="line" x1="620" y1="105" x2="640" y2="105"/>
  <line class="line" x1="760" y1="105" x2="780" y2="105"/>

  <rect class="box" x="640" y="150" width="120" height="30" rx="6"/>
  <text class="cap" x="700" y="170" text-anchor="middle">Fuse 20–30A near pack</text>
  <line class="line" x1="810" y1="105" x2="700" y2="165"/>

  <rect class="box" x="780" y="150" width="60" height="30" rx="6"/>
  <text class="cap" x="810" y="170" text-anchor="middle">Controller</text>
  <line class="line" x1="810" y1="130" x2="810" y2="150"/>
</svg>
```

## Notes
- Keep propulsion and accessory connectors distinct to avoid mis‑plugging.
- Choose controllers with **≤8 mA** idle.
- BLE lights remember last state so they work without a phone.
```

---

## `docs/schematic-van.md`
```markdown
# Schematic — Van Micro‑Zones
**NomadLink MIPA — Created by Aaron Dean Whitman**

Four independent zones (Fridge, Galley, Bedroom, Bath) with removable/tiltable PV. Optional cross‑tie only when you choose.

## Block Diagram (inline SVG)
> Save separately as `schematics/van-zones.svg` if you prefer.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="980" height="520" viewBox="0 0 980 520">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" />
    </marker>
    <style>
      .box{fill:#fff;stroke:#000;stroke-width:2;}
      .title{font: bold 14px sans-serif;}
      .cap{font: 12px sans-serif;}
      .line{stroke:#000;stroke-width:2;marker-end:url(#arrow);} 
      .dashed{stroke-dasharray:6 4;}
    </style>
  </defs>

  <!-- Zone template repeated -->
  <!-- Fridge Zone -->
  <rect class="box" x="30" y="30" width="430" height="190" rx="10"/>
  <text class="title" x="245" y="55" text-anchor="middle">Fridge Zone</text>
  <rect class="box" x="50" y="80" width="120" height="40" rx="6"/><text class="cap" x="110" y="105" text-anchor="middle">100–200W PV</text>
  <rect class="box" x="190" y="80" width="100" height="40" rx="6"/><text class="cap" x="240" y="105" text-anchor="middle">MPPT 15A</text>
  <rect class="box" x="310" y="80" width="130" height="40" rx="6"/><text class="cap" x="375" y="105" text-anchor="middle">12V LFP 50Ah</text>
  <line class="line" x1="170" y1="100" x2="190" y2="100"/>
  <line class="line" x1="290" y1="100" x2="310" y2="100"/>
  <rect class="box" x="190" y="130" width="100" height="30" rx="6"/><text class="cap" x="240" y="150" text-anchor="middle">Fuse 10A</text>
  <rect class="box" x="310" y="130" width="130" height="30" rx="6"/><text class="cap" x="375" y="150" text-anchor="middle">12V Fridge</text>
  <line class="line" x1="375" y1="100" x2="240" y2="145"/>
  <line class="line" x1="375" y1="100" x2="375" y2="130"/>

  <!-- Galley Zone -->
  <rect class="box" x="510" y="30" width="430" height="190" rx="10"/>
  <text class="title" x="725" y="55" text-anchor="middle">Galley Zone</text>
  <rect class="box" x="530" y="80" width="120" height="40" rx="6"/><text class="cap" x="590" y="105" text-anchor="middle">100W PV</text>
  <rect class="box" x="670" y="80" width="100" height="40" rx="6"/><text class="cap" x="720" y="105" text-anchor="middle">MPPT 10A</text>
  <rect class="box" x="790" y="80" width="130" height="40" rx="6"/><text class="cap" x="855" y="105" text-anchor="middle">12V LFP 20Ah</text>
  <line class="line" x1="650" y1="100" x2="670" y2="100"/>
  <line class="line" x1="770" y1="100" x2="790" y2="100"/>
  <rect class="box" x="670" y="130" width="100" height="30" rx="6"/><text class="cap" x="720" y="150" text-anchor="middle">Fuse 5A</text>
  <rect class="box" x="790" y="130" width="130" height="30" rx="6"/><text class="cap" x="855" y="150" text-anchor="middle">USB‑C PD / Pump</text>
  <line class="line" x1="855" y1="100" x2="720" y2="145"/>
  <line class="line" x1="855" y1="100" x2="855" y2="130"/>

  <!-- Bedroom Zone -->
  <rect class="box" x="30" y="260" width="430" height="190" rx="10"/>
  <text class="title" x="245" y="285" text-anchor="middle">Bedroom Zone</text>
  <rect class="box" x="50" y="330" width="120" height="40" rx="6"/><text class="cap" x="110" y="355" text-anchor="middle">100W PV</text>
  <rect class="box" x="190" y="330" width="100" height="40" rx="6"/><text class="cap" x="240" y="355" text-anchor="middle">MPPT 10A</text>
  <rect class="box" x="310" y="330" width="130" height="40" rx="6"/><text class="cap" x="375" y="355" text-anchor="middle">12V LFP 20Ah</text>
  <line class="line" x1="170" y1="350" x2="190" y2="350"/>
  <line class="line" x1="290" y1="350" x2="310" y2="350"/>
  <rect class="box" x="190" y="380" width="100" height="30" rx="6"/><text class="cap" x="240" y="400" text-anchor="middle">Fuse 3A</text>
  <rect class="box" x="310" y="380" width="130" height="30" rx="6"/><text class="cap" x="375" y="400" text-anchor="middle">LED / PD Hub</text>
  <line class="line" x1="375" y1="350" x2="240" y2="395"/>
  <line class="line" x1="375" y1="350" x2="375" y2="380"/>

  <!-- Bath Zone -->
  <rect class="box" x="510" y="260" width="430" height="190" rx="10"/>
  <text class="title" x="725" y="285" text-anchor="middle">Bath/Utility Zone</text>
  <rect class="box" x="530" y="330" width="120" height="40" rx="6"/><text class="cap" x="590" y="355" text-anchor="middle">50–100W PV</text>
  <rect class="box" x="670" y="330" width="100" height="40" rx="6"/><text class="cap" x="720" y="355" text-anchor="middle">MPPT 10A</text>
  <rect class="box" x="790" y="330" width="130" height="40" rx="6"/><text class="cap" x="855" y="355" text-anchor="middle">12V LFP 10–20Ah</text>
  <line class="line" x1="650" y1="350" x2="670" y2="350"/>
  <line class="line" x1="770" y1="350" x2="790" y2="350"/>
  <rect class="box" x="670" y="380" width="100" height="30" rx="6"/><text class="cap" x="720" y="400" text-anchor="middle">Fuse 3A</text>
  <rect class="box" x="790" y="380" width="130" height="30" rx="6"/><text class="cap" x="855" y="400" text-anchor="middle">LED / USB‑C</text>
  <line class="line" x1="855" y1="350" x2="720" y2="395"/>
  <line class="line" x1="855" y1="350" x2="855" y2="380"/>

  <!-- Optional cross tie (manual) -->
  <line class="line dashed" x1="460" y1="125" x2="510" y2="125"/>
  <text class="cap" x="485" y="115" text-anchor="middle">(optional B2B, isolated, switched)</text>
  <line class="line dashed" x1="460" y1="355" x2="510" y2="355"/>
</svg>
```

## Notes
- Keep each zone islanded; bring them together only via an **isolated B2B** with a hard switch.
- Use **USB‑C PD** for devices; avoid inverters.
```

---

## `docs/schematic-apartment.md`
```markdown
# Schematic — Apartment Unit‑Grid
**NomadLink MIPA — Created by Aaron Dean Whitman**

A self‑contained apartment with BIPV, swappable storage, DC‑first distribution, and an opt‑in coupler to the floor ring.

## Block Diagram (inline SVG)
> Save separately as `schematics/unit-grid.svg` if you prefer.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="960" height="520" viewBox="0 0 960 520">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" />
    </marker>
    <style>
      .box{fill:#fff;stroke:#000;stroke-width:2;}
      .title{font: bold 14px sans-serif;}
      .cap{font: 12px sans-serif;}
      .line{stroke:#000;stroke-width:2;marker-end:url(#arrow);} 
      .dashed{stroke-dasharray:6 4;}
    </style>
  </defs>

  <rect class="box" x="30" y="30" width="900" height="460" rx="12"/>
  <text class="title" x="480" y="55" text-anchor="middle">Apartment Unit‑Grid (Island by default)</text>

  <rect class="box" x="60" y="90" width="140" height="50" rx="6"/><text class="cap" x="130" y="120" text-anchor="middle">BIPV 0.4–1.2 kW</text>
  <rect class="box" x="220" y="90" width="120" height="50" rx="6"/><text class="cap" x="280" y="120" text-anchor="middle">MPPT</text>
  <rect class="box" x="360" y="90" width="150" height="50" rx="6"/><text class="cap" x="435" y="120" text-anchor="middle">48V Battery Stack 1–4 kWh (swappable)</text>
  <line class="line" x1="200" y1="115" x2="220" y2="115"/>
  <line class="line" x1="340" y1="115" x2="360" y2="115"/>

  <rect class="box" x="540" y="90" width="140" height="50" rx="6"/><text class="cap" x="610" y="120" text-anchor="middle">48→12V DC/DC</text>
  <rect class="box" x="700" y="90" width="110" height="50" rx="6"/><text class="cap" x="755" y="120" text-anchor="middle">12V DC Loads</text>
  <line class="line" x1="510" y1="115" x2="540" y2="115"/>
  <line class="line" x1="680" y1="115" x2="700" y2="115"/>

  <rect class="box" x="540" y="160" width="140" height="50" rx="6"/><text class="cap" x="610" y="190" text-anchor="middle">48→USB‑C PD</text>
  <rect class="box" x="700" y="160" width="110" height="50" rx="6"/><text class="cap" x="755" y="190" text-anchor="middle">Phones/Laptops</text>
  <line class="line" x1="510" y1="185" x2="540" y2="185"/>
  <line class="line" x1="680" y1="185" x2="700" y2="185"/>

  <rect class="box" x="540" y="230" width="140" height="50" rx="6"/><text class="cap" x="610" y="260" text-anchor="middle">48→AC Inverter*</text>
  <rect class="box" x="700" y="230" width="110" height="50" rx="6"/><text class="cap" x="755" y="260" text-anchor="middle">Legacy AC</text>
  <text class="cap" x="610" y="300" text-anchor="middle">*off by default</text>
  <line class="line" x1="510" y1="255" x2="540" y2="255"/>
  <line class="line" x1="680" y1="255" x2="700" y2="255"/>

  <rect class="box" x="360" y="330" width="150" height="50" rx="6"/><text class="cap" x="435" y="360" text-anchor="middle">Isolated BiDir Coupler</text>
  <rect class="box" x="540" y="330" width="140" height="50" rx="6"/><text class="cap" x="610" y="360" text-anchor="middle">48V Floor Ring (normally off)</text>
  <line class="line dashed" x1="510" y1="355" x2="540" y2="355"/>
</svg>
```

## Notes
- The coupler is user‑enabled; the floor ring is de‑energized unless multiple units opt‑in.
- DC‑first distribution minimizes idle losses.
```

---

## `docs/schematic-floor.md`
```markdown
# Schematic — Floor Cluster‑Grid
**NomadLink MIPA — Created by Aaron Dean Whitman**

Independent units with an optional, sectionalized 48 V DC ring and a small buffer store for cooperative lending.

## Block Diagram (inline SVG)
> Save separately as `schematics/floor-cluster.svg` if you prefer.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="980" height="520" viewBox="0 0 980 520">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" />
    </marker>
    <style>
      .box{fill:#fff;stroke:#000;stroke-width:2;}
      .title{font: bold 14px sans-serif;}
      .cap{font: 12px sans-serif;}
      .line{stroke:#000;stroke-width:2;marker-end:url(#arrow);} 
      .ring{stroke:#000;stroke-width:3;fill:none;}
      .dashed{stroke-dasharray:6 4;}
    </style>
  </defs>

  <text class="title" x="490" y="30" text-anchor="middle">Floor Cluster with Optional 48 V DC Ring</text>

  <!-- Ring bus -->
  <rect class="box" x="70" y="60" width="840" height="300" rx="12"/>
  <text class="cap" x="490" y="80" text-anchor="middle">48 V DC Ring (sectionalized, normally off)</text>

  <!-- Buffer storage -->
  <rect class="box" x="420" y="110" width="140" height="60" rx="8"/>
  <text class="cap" x="490" y="145" text-anchor="middle">Floor Buffer 10–50 kWh</text>

  <!-- Unit couplers -->
  <rect class="box" x="120" y="220" width="140" height="60" rx="8"/>
  <text class="cap" x="190" y="255" text-anchor="middle">Unit A Coupler</text>

  <rect class="box" x="320" y="220" width="140" height="60" rx="8"/>
  <text class="cap" x="390" y="255" text-anchor="middle">Unit B Coupler</text>

  <rect class="box" x="520" y="220" width="140" height="60" rx="8"/>
  <text class="cap" x="590" y="255" text-anchor="middle">Unit C Coupler</text>

  <rect class="box" x="720" y="220" width="140" height="60" rx="8"/>
  <text class="cap" x="790" y="255" text-anchor="middle">Unit D Coupler</text>

  <line class="line dashed" x1="190" y1="220" x2="190" y2="170"/>
  <line class="line dashed" x1="390" y1="220" x2="390" y2="170"/>
  <line class="line dashed" x1="590" y1="220" x2="590" y2="170"/>
  <line class="line dashed" x1="790" y1="220" x2="790" y2="170"/>

  <text class="cap" x="490" y="380" text-anchor="middle">Couplers are isolated and manually enabled; ring is de‑energized unless needed.</text>
</svg>
```

## Notes
- Sectionalize the ring with breakers so a fault isolates without taking the floor down.
- Meter transfers for neighbor‑lending if desired.
```

---

## `docs/schematic-tower.md`
```markdown
# Schematic — Tower Macro‑Grid
**NomadLink MIPA — Created by Aaron Dean Whitman**

A self‑contained high‑rise with BIPV curtain walls, rooftop PV, elevator regeneration, large storage, and an optional grid intertie (shore power).

## Block Diagram (inline SVG)
> Save separately as `schematics/tower-macro.svg` if you prefer.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="980" height="620" viewBox="0 0 980 620">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" />
    </marker>
    <style>
      .box{fill:#fff;stroke:#000;stroke-width:2;}
      .title{font: bold 14px sans-serif;}
      .cap{font: 12px sans-serif;}
      .line{stroke:#000;stroke-width:2;marker-end:url(#arrow);} 
      .dashed{stroke-dasharray:6 4;}
    </style>
  </defs>

  <text class="title" x="490" y="30" text-anchor="middle">Tower Macro‑Grid (Islanding by Default)</text>

  <!-- Generation block -->
  <rect class="box" x="40" y="60" width="360" height="160" rx="12"/>
  <text class="cap" x="220" y="85" text-anchor="middle">Generation</text>
  <rect class="box" x="60" y="90" width="140" height="40" rx="6"/><text class="cap" x="130" y="115" text-anchor="middle">Rooftop PV</text>
  <rect class="box" x="210" y="90" width="170" height="40" rx="6"/><text class="cap" x="295" y="115" text-anchor="middle">BIPV Curtain Wall</text>
  <rect class="box" x="60" y="140" width="140" height="40" rx="6"/><text class="cap" x="130" y="165" text-anchor="middle">Elevator Regen</text>
  <rect class="box" x="210" y="140" width="170" height="40" rx="6"/><text class="cap" x="295" y="165" text-anchor="middle">Solar Thermal (DHW)</text>

  <!-- Combiner & DC backbone -->
  <rect class="box" x="420" y="90" width="140" height="50" rx="8"/>
  <text class="cap" x="490" y="120" text-anchor="middle">MPPT / Combiner</text>
  <line class="line" x1="400" y1="110" x2="420" y2="115"/>
  <line class="line" x1="400" y1="160" x2="420" y2="115"/>

  <rect class="box" x="600" y="90" width="160" height="50" rx="8"/>
  <text class="cap" x="680" y="120" text-anchor="middle">380 V DC Backbone</text>
  <line class="line" x1="560" y1="115" x2="600" y2="115"/>

  <!-- Storage -->
  <rect class="box" x="600" y="160" width="160" height="60" rx="8"/>
  <text class="cap" x="680" y="190" text-anchor="middle">Battery Racks 0.5–5 MWh</text>
  <rect class="box" x="780" y="160" width="160" height="60" rx="8"/>
  <text class="cap" x="860" y="190" text-anchor="middle">Thermal Storage 20–100 m³</text>
  <line class="line" x1="680" y1="140" x2="680" y2="160"/>

  <!-- Floor distribution -->
  <rect class="box" x="540" y="260" width="160" height="50" rx="8"/>
  <text class="cap" x="620" y="290" text-anchor="middle">380→48 V Floor DC/DC</text>
  <rect class="box" x="540" y="330" width="160" height="50" rx="8"/>
  <text class="cap" x="620" y="360" text-anchor="middle">48 V Floor Rings</text>
  <line class="line" x1="680" y1="220" x2="620" y2="260"/>

  <!-- Legacy AC branch -->
  <rect class="box" x="740" y="260" width="160" height="50" rx="8"/>
  <text class="cap" x="820" y="290" text-anchor="middle">380→AC Inverters*</text>
  <rect class="box" x="740" y="330" width="160" height="50" rx="8"/>
  <text class="cap" x="820" y="360" text-anchor="middle">Legacy AC Panels</text>
  <text class="cap" x="820" y="385" text-anchor="middle">*Off unless needed</text>
  <line class="line" x1="680" y1="220" x2="820" y2="260"/>

  <!-- Shore power intertie -->
  <rect class="box" x="420" y="260" width="100" height="50" rx="8"/>
  <text class="cap" x="470" y="290" text-anchor="middle">Grid Intertie (shore)</text>
  <line class="line dashed" x1="470" y1="240" x2="470" y2="260"/>

  <!-- Notes -->
  <text class="cap" x="490" y="560" text-anchor="middle">Islanding by default; sectionalized DC; life‑safety on dedicated DC with independent storage.</text>
</svg>
```

## Notes
- Anti‑islanding and protection per local code for the shore power point.
- Elevator regen feeds the DC bus; ultracaps/flywheels optional for millisecond events.
```



---

## `docs/bom-tables.md`
```markdown
# Bills of Materials (BOM) — NomadLink MIPA
**Created by Aaron Dean Whitman**

These tables are generic starting points. Substitute equivalent components as needed.

## Bike Nano-Zone
| Component          | Spec / Notes                      | Qty |
|--------------------|-----------------------------------|-----|
| PV Panel           | 100W foldable, 18V nominal        | 1   |
| MPPT Controller    | 10A, ≤8 mA idle                   | 1   |
| Battery            | 12V LFP, 10–20Ah, with BMS        | 1   |
| Fuse (main)        | 15A blade                         | 1   |
| USB-C PD Hub       | 60–100W, 12V input                | 1   |
| LED rail (optional)| 12V LED strip/lamps               | 1   |
| Cables/Connectors  | XT60/SAE, fused leads             | set |

## Bike Propulsion Charge Path
| Component          | Spec / Notes                      | Qty |
|--------------------|-----------------------------------|-----|
| PV Panel           | 100–160W foldable                 | 1   |
| Solar Charger      | MPPT→CC/CV at pack voltage        | 1   |
| Battery (motor)    | 36V/48V e-bike pack, 7–10Ah       | 1   |
| Fuse               | 20–30A near pack                  | 1   |
| Cables             | Distinct connectors (e.g. Anderson vs XT60) | set |

## Van Zones (per zone)
| Component          | Spec / Notes                      | Qty |
|--------------------|-----------------------------------|-----|
| PV Panel           | 100W removable/tiltable           | 1   |
| MPPT Controller    | 10–15A, low idle                  | 1   |
| Battery            | 12V LFP, 20Ah (lights) or 50Ah (fridge) | 1 |
| Fuse block         | 3–10A fuses                       | 1   |
| USB-C PD Hub       | 60–100W                           | 1   |
| 12V Loads          | LED strips, pumps, fans           | as req |
| Cables/Connectors  | Short 12–14 AWG, XT60/Powerpole   | set |

## Apartment Unit-Grid
| Component          | Spec / Notes                      | Qty |
|--------------------|-----------------------------------|-----|
| PV Array           | BIPV, 400–1200W                   | 1   |
| MPPT Controller    | 20–40A                            | 1   |
| Battery Stack      | 48V LFP, 1–4 kWh, swappable modules | 1+ |
| DC/DC Converter    | 48→12V, 20–40A                    | 1   |
| USB-C PD Hub       | 100W+                             | 1   |
| Inverter (opt)     | 48V→AC, low idle, 500–1000W       | 1   |
| Isolated Coupler   | 48V BiDir, manual enable          | 1   |

## Floor Cluster-Grid
| Component          | Spec / Notes                      | Qty |
|--------------------|-----------------------------------|-----|
| DC Ring Bus        | 48V, sectionalized                | 1   |
| Buffer Storage     | 10–50 kWh                         | 1   |
| Unit Couplers      | Isolated BiDir DC/DC              | per unit |
| Breakers           | Sectionalize ring                 | as req |

## Tower Macro-Grid
| Component          | Spec / Notes                      | Qty |
|--------------------|-----------------------------------|-----|
| Generation Sources | Rooftop PV, BIPV, elevator regen, solar thermal | multi |
| Combiner           | MPPT/DC aggregator                | 1+  |
| DC Backbone        | 380V riser                        | 1   |
| Battery Racks      | 0.5–5 MWh modular                 | 1+  |
| Thermal Storage    | 20–100 m³ hot water/PCM           | 1   |
| Floor Converters   | 380→48V DC/DC                     | per floor |
| Inverters (legacy) | 380V→AC, sectional, off default   | as req |
| Grid Intertie      | Shore power contactor             | 1   |
```

---

## `docs/field-checklist.md`
```markdown
# NomadLink MIPA — Field Checklist
**Created by Aaron Dean Whitman**

## Commissioning a Zone
- [ ] Mount PV panel; ensure tilt/angle unobstructed.
- [ ] Connect PV to MPPT (correct polarity).
- [ ] Connect MPPT to battery (fuse ≤15 cm from + terminal).
- [ ] Confirm MPPT charge profile matches battery chemistry.
- [ ] Wire DC/DC converters and hubs; size fuses at 125% load.
- [ ] Verify idle current draw <10 mA when system off.
- [ ] Label all cables and fuses.

## Daily Operation
- [ ] Place PV in sun; avoid shading.
- [ ] Check battery SOC on BMS or LED meter.
- [ ] Confirm devices charge via USB-C PD.
- [ ] BLE devices remember last state without phone.

## Maintenance
- [ ] Inspect connectors/cables monthly for wear.
- [ ] Test fuse continuity with spares available.
- [ ] Rotate/swappable batteries periodically.
- [ ] Ventilate battery spaces (ambient cabin air).

## Troubleshooting Quick Ref
- **No charge**: Check PV → MPPT polarity, sun exposure.
- **Fast drain**: Verify idle draws, switch off inverters.
- **Device not charging**: Confirm PD negotiation, cable rating.
- **Overheating**: Ensure ventilation for fridge/compressor zones.

## Emergency
- [ ] Each zone has manual disconnect switch.
- [ ] Keep at least one foldable PV + 20Ah battery as emergency reserve.
- [ ] Life-safety loads (lights, alarms) on dedicated battery.
```

