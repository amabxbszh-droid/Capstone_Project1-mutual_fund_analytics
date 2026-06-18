"""
Master Pipeline Runner
"""

import subprocess

scripts = [
    "clean_data.py",
    "clean_nav_history.py",
    "clean_investor_transactions.py",
    "validate_amfi.py",
    "load_sqlite.py"
]

for script in scripts:
    print(f"Running {script}")
    subprocess.run(
        ["python", f"scripts/{script}"]
    )

print("Pipeline Complete")