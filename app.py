# Root level app.py
import sys
from pathlib import Path

# Add the package to the path
sys.path.insert(0, str(Path(__file__).parent / "DO_prediction_package"))

# Import and run the main app
from DO_prediction_package.app import *
