# Contributing Guidelines  
**Repo:** NomadLink-MIPA (Exoform × Highland Ember)  
**Author:** Aaron Dean Whitman (2025)  

---

## 1. Philosophy
This project merges **technical engineering (Exoform)** and **cultural storytelling (Highland Ember)**.  
Contributions must respect both domains:  
- **Technical commits** should improve functionality, safety, or documentation.  
- **Cultural commits** should expand mythos, symbols, or narrative.  

---

## 2. Commit Messages
Use [Conventional Commits](https://www.conventionalcommits.org/):  

- `feat:` → new feature (e.g., `feat(em-muscle): add torque control loop`)  
- `fix:` → bug fix  
- `docs:` → documentation only  
- `test:` → add/modify test plan  
- `chore:` → repo maintenance (no code/doc changes)  

**Format:**  


---

## 3. Branching Model
- `main` → stable branch (always working).  
- `dev` → integration branch for new features.  
- Feature branches: `feature/<module>` (e.g., `feature/em-muscle-control`).  
- Bugfix branches: `fix/<issue>` (e.g., `fix/can-timeout`).  

---

## 4. Pull Request Checklist
Before opening a PR:  
- [ ] Code/doc builds without errors.  
- [ ] Test plan updated if needed.  
- [ ] Symbols/Mythos updated if cultural component is affected.  
- [ ] Commit message follows convention.  

---

## 5. Coding Standards
- Python: PEP 8 style.  
- ROS 2 nodes: must include safe defaults (publish 0 torque if no command).  
- Docs: Markdown, wrapped at 80–100 chars for readability.  

---

## 6. Attribution
Every contribution must preserve authorship attribution to Aaron Dean Whitman and the open-source license:  
**“Exoform × Highland Ember (Whitman, 2025)”**  

---

## 7. Notes
Contributors should see `docs/INDEX.md` for project structure.  
All cultural + technical tracks are equal parts of this repository.  
