#!/usr/bin/env python3
"""Parse small text report exports into a normalized JSON summary.
Patterns are intentionally conservative; missing values remain null rather than guessed.
"""
import argparse,json,re
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('reports',nargs='+');a=p.parse_args()
text='\n'.join(Path(x).read_text(errors='ignore') for x in a.reports)
def grab(pattern):
    m=re.search(pattern,text,re.I|re.M); return float(m.group(1)) if m else None
out={
 'wns_ns':grab(r'\bWNS\b\s*[:=]?\s*(-?\d+(?:\.\d+)?)'),
 'tns_ns':grab(r'\bTNS\b\s*[:=]?\s*(-?\d+(?:\.\d+)?)'),
 'area_um2':grab(r'(?:total\s+)?(?:cell\s+)?area\s*[:=]\s*(\d+(?:\.\d+)?)'),
 'power_mw':grab(r'(?:total\s+)?power\s*[:=]\s*(\d+(?:\.\d+)?)'),
 'utilization_percent':grab(r'utili[sz]ation\s*[:=]\s*(\d+(?:\.\d+)?)'),
 'drc_violations':grab(r'drc\s+(?:violations?|count)\s*[:=]\s*(\d+)'),
 'lvs_errors':grab(r'lvs\s+(?:errors?|count)\s*[:=]\s*(\d+)')
}
print(json.dumps(out,indent=2))
