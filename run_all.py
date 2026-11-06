#!/usr/bin/env python3
"""Regenerate every figure that does not need the private port, then run the public tests."""
import subprocess, sys, os
here = os.path.dirname(os.path.abspath(__file__))
subprocess.check_call([sys.executable, os.path.join(here, "figures", "make_figures.py")], cwd=here)
rc = subprocess.call([sys.executable, "-m", "pytest", "-q", os.path.join(here, "tests")], cwd=here)
print("\nSteps that need the private nguyen_port.py (not in this repository): 1_refit/refit8d.py, multistart.py, weak_profiles.py, verify_reproduction.py. See docs/PERMISSION_STATUS.md.")
sys.exit(rc)
