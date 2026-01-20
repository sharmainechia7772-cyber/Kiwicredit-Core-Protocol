# core/__init__.py
# Status: The Engine Room of Thermodynamic Justice (Complete)

"""
CORE PACKAGE
The mathematical heart of the Phoenix Protocol.
Here, we enforce the Governing Law: V * T = k.
"""

# 1. Audit & Time Engines (The Basics)
from .audit_logic import DebtEntropyAudit, ChronocideCalculator
from .temporal_engine import TemporalSovereignty

# 2. Physics & Navigation (The Laws)
from .dignity_logic import DignityAreaProtocol
from .vector_navigation import EndpointDeviationAudit

# 3. Actors & Simulation (The Cast & Stage)
from .economic_actors import AgentSam, AgentSME
from .reality_matrix import ParallelUniverse, EconomicBasin

# 4. Geometry of Hope (The Horizon)
from .hope_geometry import FutureHorizonEngine

__all__ = [
    'DebtEntropyAudit', 
    'ChronocideCalculator', 
    'TemporalSovereignty',
    'DignityAreaProtocol', 
    'EndpointDeviationAudit', 
    'AgentSam', 
    'AgentSME', 
    'ParallelUniverse', 
    'EconomicBasin', 
    'FutureHorizonEngine'
]
