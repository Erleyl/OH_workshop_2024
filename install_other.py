import os
import sys
from subprocess import Popen, PIPE

# Function to run a command and check its success
def run_and_check(args, check, message, failure, success):
    print(message)
    r = Popen(args, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    o, e = r.communicate()
    out = o + e
    if r.returncode == 0 and check in out:
        print(success)
    else:
        print(failure, out)

# Update package lists and install system packages
run_and_check(
    ["apt-get", "update"],
    "Reading package lists",
    "Updating package lists...",
    "Failed to update package lists.",
    "Package lists updated."
)

run_and_check(
    ["apt-get", "install", "-y", "mafft", "iqtree"],
    "Setting up",
    "Installing MAFFT and IQ-TREE...",
    "Failed to install MAFFT and IQ-TREE.",
    "MAFFT and IQ-TREE installed or already present."
)

# Install Python packages
run_and_check(
    ["pip", "install", "biopython", "treetime"],
    "Successfully installed",
    "Installing Biopython and TreeTime...",
    "Failed to install Biopython and TreeTime.",
    "Biopython and TreeTime installed or already present."
)
