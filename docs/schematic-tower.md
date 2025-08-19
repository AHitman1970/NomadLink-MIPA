

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
