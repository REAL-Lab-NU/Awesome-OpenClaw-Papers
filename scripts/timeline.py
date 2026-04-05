import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Dark theme
plt.rcParams['figure.facecolor'] = '#1a1b2e'
plt.rcParams['axes.facecolor'] = '#1a1b2e'
plt.rcParams['text.color'] = 'white'
plt.rcParams['font.family'] = 'sans-serif'

fig, ax = plt.subplots(figsize=(18, 6.5))
ax.set_xlim(-0.5, 17)
ax.set_ylim(-3.5, 4.2)
ax.axis('off')

# Phase backgrounds
phases = [
    (-0.5, 2.5, '#607D8B', 0.15, 'January', 'LAUNCH'),
    (2.5, 7.5, '#42A5F5', 0.12, 'February', 'EXPLOSION'),
    (7.5, 13, '#EF5350', 0.12, 'March', 'CRISIS & RESPONSE'),
    (13, 17, '#66BB6A', 0.12, 'April', 'MATURITY'),
]

for x0, x1, color, alpha, month, label in phases:
    ax.axvspan(x0, x1, alpha=alpha, color=color, zorder=0)
    ax.text((x0 + x1) / 2, 3.8, f'{month} 2026', fontsize=11, fontweight='bold',
            ha='center', va='center', color=color, alpha=0.9)
    ax.text((x0 + x1) / 2, 3.35, label, fontsize=7, ha='center', va='center',
            color=color, alpha=0.5, style='italic', fontweight='bold')

# Timeline bar with gradient effect
ax.plot([-0.3, 16.5], [0, 0], color='white', linewidth=3, alpha=0.25, zorder=1)
# Glow effect
ax.plot([-0.3, 16.5], [0, 0], color='white', linewidth=8, alpha=0.05, zorder=0)

# Events: (x, text, side, color, date_label, marker_symbol)
events = [
    (0.5,  'Moltbook\nlaunched',                        1,  '#607D8B', 'Jan 28',   's'),
    (1.5,  'OpenClaw released\n100K stars in 60hrs',    -1,  '#607D8B', 'Jan 29',   '*'),
    (3.5,  '"SaaSpocalypse"\n$285B market cap erased',   1,  '#42A5F5', 'Feb 3',    'v'),
    (5.0,  'Microsoft advisory\n"not for workstations"',-1,  '#42A5F5', 'Feb 19',   '^'),
    (6.5,  'ClawHavoc campaign\n824+ malicious skills',  1,  '#42A5F5', 'Late Feb', 'D'),
    (8.5,  '250K stars\nbeats React 10yr record',       -1,  '#EF5350', 'Mar 3',    '*'),
    (10.0, 'Meta acquires\nMoltbook',                    1,  '#EF5350', 'Mar 10',   'p'),
    (11.5, 'NVIDIA NemoClaw\nat GTC 2026',              -1,  '#EF5350', 'Mar 16',   'h'),
    (14.5, '335K stars\n54+ papers, 20+ reports',        1,  '#66BB6A', 'Apr',      'o'),
]

for x, text, side, color, date_label, marker in events:
    # Outer glow on dot
    ax.plot(x, 0, marker, color=color, markersize=16, alpha=0.3, zorder=2)
    # Main dot
    ax.plot(x, 0, marker, color=color, markersize=10, zorder=3,
            markeredgecolor='white', markeredgewidth=0.8)

    # Connector line (dashed for style)
    y_connect = side * 0.65
    ax.plot([x, x], [0.15 * side, y_connect], color=color, linewidth=1.5,
            alpha=0.5, zorder=2, linestyle='-')

    # Text card with rounded box
    y_text = side * 1.7
    bbox_props = dict(
        boxstyle="round,pad=0.5",
        facecolor=color, alpha=0.18,
        edgecolor=color, linewidth=1.3
    )
    ax.text(x, y_text, text, fontsize=8, ha='center', va='center',
            color='white', fontweight='normal', bbox=bbox_props, zorder=5,
            linespacing=1.5)

    # Date label on opposite side of card
    y_date = -side * 0.4
    ax.text(x, y_date, date_label, fontsize=6.5, ha='center', va='center',
            color=color, alpha=0.75, fontweight='bold', zorder=5)

# Growth stats bar at bottom
stats_y = -3.1
stats_text = (
    "Stars: 0  >  100K  >  250K  >  335K        "
    "Moltbook: 0  >  770K  >  1.6M agents        "
    "Skills: 0  >  5,700  >  13,700+"
)
# Background bar
bar = FancyBboxPatch((1, stats_y - 0.35), 14.5, 0.7,
                      boxstyle="round,pad=0.15",
                      facecolor='white', alpha=0.05, edgecolor='white',
                      linewidth=0.5, zorder=4)
ax.add_patch(bar)
ax.text(8.25, stats_y, stats_text,
        fontsize=7.5, ha='center', va='center', color='white', alpha=0.5,
        fontfamily='monospace', zorder=5)

# Title
ax.text(8.25, -2.2, 'OpenClaw Research Ecosystem Timeline',
        fontsize=9, ha='center', va='center', color='white', alpha=0.3,
        fontweight='bold', style='italic')

plt.tight_layout(pad=0.3)
plt.savefig('/Users/wangziqing/Research/Awesome-OpenClaw-Research/assets/timeline.png',
            dpi=200, bbox_inches='tight', facecolor='#1a1b2e', edgecolor='none')
plt.close()
print("Saved timeline.png")
