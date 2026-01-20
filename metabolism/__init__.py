# metabolism/__init__.py
# Status: The Circulation System of Hope (Complete)

"""
METABOLISM PACKAGE
Converts systemic security into cognitive innovation.
Also handles the Excretion (Burning) of excess entropy and Energy Anchoring.
"""

# metabolism/__init__.py
# Status: System Circulation (Aligned with Filesystem)

# 1. Flow & Measures
from .circulation_physics import CommunityMetabolism, SynergyEngine
from .distribution_logic import ProgressiveDistributor
from .supply_chain_diffusion import SupplyChainHydraulics
from .metrics import WelfareMetrics
from .adoption_mechanics import DualWalletManager, IgnitionCalculator
from .vitality_monitor import VitalityDetector

# 2. Sinks & Burning
from .entropy_sink import NegativeEntropyPortal
from .fiscal_sink import FiscalSink
# Note: 'EntropySink' class is inside 'fiscal_interface.py' (Alpha Protocol)
from .fiscal_interface import EntropySink as AlphaEntropySink 

# 3. Anchors & Dividends
from .cognitive_dividend import CognitiveBandwidthEngine
from .reality_anchor import MetabolicAnchor, RiverbedDynamics

__all__ = [
    'CommunityMetabolism', 'SynergyEngine', 
    'ProgressiveDistributor', 'SupplyChainHydraulics', 'WelfareMetrics',
    'DualWalletManager', 'IgnitionCalculator', 'VitalityDetector',
    'NegativeEntropyPortal', 'FiscalSink', 'AlphaEntropySink',
    'CognitiveBandwidthEngine', 'MetabolicAnchor', 'RiverbedDynamics'
]
