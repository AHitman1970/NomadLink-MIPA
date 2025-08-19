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
