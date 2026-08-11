#!/usr/bin/env python3
"""Public-repository hygiene check.

This script intentionally checks only things that can be validated without
proprietary tools or hardware. It does not claim that RTL, EDA, or benchmark
results have been reproduced unless those artifacts are actually present.
"""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {'.md','.txt','.py','.sh','.yml','.yaml','.sv','.v','.vh','.svh','.c','.cc','.cpp','.h','.hpp','.tcl','.sdc','.cmake'}
BANNED_PUBLIC_PHRASES = [
    'aspi'+'rational', 'resume '+'strategy', 'ai '+'generated', 'chat'+'gpt', 'master '+'repository'
]
SECRET_PATTERNS = {
    'private key': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'github token': re.compile(r'gh[pousr]_[A-Za-z0-9_]{20,}'),
    'aws access key': re.compile(r'AKIA[0-9A-Z]{16}'),
    'generic bearer token': re.compile(r'Bearer\s+[A-Za-z0-9._~-]{24,}', re.I),
}
ABS_PATHS = [re.compile(r'/Users/[^/\s]+/'), re.compile(r'/home/[^/\s]+/'), re.compile(r'[A-Za-z]:\\Users\\[^\\\s]+\\')]

issues=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or '.git' in p.parts or p.suffix.lower() not in TEXT_SUFFIXES:
        continue
    if p.resolve() == Path(__file__).resolve():
        continue
    try: text=p.read_text(errors='ignore')
    except Exception: continue
    low=text.lower()
    # The audit/report files may discuss prohibited source-language terms privately;
    # public repository files should not.
    if 'private_work' not in p.parts:
        for phrase in BANNED_PUBLIC_PHRASES:
            if phrase in low:
                issues.append(f'{p.relative_to(ROOT)}: public-facing phrase to remove: {phrase!r}')
    for label,pat in SECRET_PATTERNS.items():
        if pat.search(text): issues.append(f'{p.relative_to(ROOT)}: possible {label}')
    for pat in ABS_PATHS:
        if pat.search(text): issues.append(f'{p.relative_to(ROOT)}: machine-specific absolute path')

if issues:
    print('PUBLICATION CHECK: FAIL')
    for i in issues: print(' -',i)
    sys.exit(1)
print('PUBLICATION CHECK: PASS')
