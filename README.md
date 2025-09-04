# NomadLink MIPA
**NomadLink Modular Independent Power Architecture**
**Created by Aaron Dean Whitman**


> Open‑source, modular, zone‑based renewable power architecture — from basic survival to skyscraper — designed to operate fully islanded with optional, user‑controlled interties (aka “shore power”).


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

nomadlink-mipa/
│
├── README.md                # Overview, attribution, quick start
├── LICENSE.md               # CERN-OHL with your attribution clause
├── docs/
│   ├── architecture-overview.md
│   ├── schematic-bike.md
│   ├── schematic-van.md
│   ├── schematic-apartment.md
│   ├── schematic-floor.md
│   ├── schematic-tower.md
│   └── scaling-examples.md
├── schematics/
│   ├── bike-diagram.png
│   ├── van-diagram.png
│   ├── apartment-diagram.png
│   ├── floor-diagram.png
│   └── tower-diagram.png
├── patent/
│   └── provisional-patent-draft.md
└── LICENSES/
    └── attribution-clause.txt
---

# Exoform / Highland Ember — Linked Projects
**Author:** Aaron Dean Whitman  
**Timestamp:** 2025  

---

## 1. Overview
This repository contains the **NomadLink-MIPA Exoform** project (open-source powered exosuit architecture) and its linked creative/technical sibling project **Highland Ember**.  

Both projects are tied by the principle of **modular, open systems**:  
- **Exoform** — mechanized extension of the human body (engineering focus).  
- **Highland Ember** — cultural, narrative, and symbolic framework (creative focus).  

---

## 2. Linkage
- Highland Ember provides the **mythos, branding, and narrative** identity.  
- Exoform provides the **technical, mechanical, and software** implementation.  
- Together they represent **applied open-source creativity**: technology and culture unified.

---

## 3. Current Status
- ✅ EM-Muscle module declaration.  
- ✅ EM-Muscle technical specification.  
- ✅ EM-Muscle BOM.  
- ✅ EM-Muscle control stub.  
- ✅ Test plan and safety checklist.  
- ✅ Integration doc.  

Next steps:
- Add more modules (control, vision, AI layers).  
- Extend Highland Ember narrative docs into `/docs/highland_ember/`.  
- Create linkage README in both directories.  

---

## 4. Attribution
All works © Aaron Dean Whitman (2025) under open Exoform/Highland Ember license.  
Please credit **“Exoform (Whitman, 2025)”** in derived works.

