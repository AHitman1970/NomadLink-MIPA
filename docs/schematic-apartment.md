

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
