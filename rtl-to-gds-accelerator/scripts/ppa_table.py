#!/usr/bin/env python3
import csv,sys
rows=list(csv.DictReader(open(sys.argv[1])))
cols=['configuration','frequency_mhz','wns_ns','tns_ns','area_um2','power_mw','utilization_percent','congestion','energy_per_op']
print('| '+' | '.join(cols)+' |');print('|'+ '|'.join(['---']*len(cols))+'|')
for r in rows: print('| '+' | '.join(r.get(c,'') for c in cols)+' |')
