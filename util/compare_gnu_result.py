#!/usr/bin/python
"""
Compare the current results to the last results gathered from the main branch to highlight
if a PR is making the results better/worse
"""

import json
import sys

NEW = json.load(open("gnu-result.json"))
OLD = json.load(open("latest-gnu-result.json"))

# Extract the specific results from the dicts
last = OLD[list(OLD.keys())[0]]
current = NEW[list(NEW.keys())[0]]

pass_d = int(current["pass"]) - int(last["pass"])
fail_d = int(current["fail"]) - int(last["fail"])
error_d = int(current["error"]) - int(last["error"])
skip_d = int(current["skip"]) - int(last["skip"])

# Get an annotation to highlight changes
print(
    f"::warning ::Changes from main: PASS {pass_d:+d} / FAIL {fail_d:+d} / ERROR {error_d:+d} / SKIP {skip_d:+d} "
)

# Check if there are no changes.
if pass_d == 0:
    print("::warning ::Gnu tests No changes")

# If results are worse fail the job to draw attention
if pass_d < 0:
    sys.exit(1)
