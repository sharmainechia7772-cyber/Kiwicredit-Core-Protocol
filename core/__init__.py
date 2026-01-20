# core/__init__.py
# Status: The Engine Room of Thermodynamic Justice (Complete)

"""
CORE PACKAGE
The mathematical heart of the Phoenix Protocol.
Here, we enforce the Governing Law: V * T = k.
"""

# 1. Physics & Math
from .audit_logic import DebtEntropyAudit, ChronocideCalculator
from .dignity_logic import DignityAreaProtocol
from .hope_geometry import FutureHorizonEngine
from .minting_protocol import GenesisProtocol
from .decay_engine import KiwicreditToken, GarbageCollector
from .model_optimizer import EconomicOptimizer

# 2. Time & Concurrency
from .temporal_engine import TemporalSovereignty
from .concurrency_manager import EconomyThread, WatchdogTimer

# 3. Actors & Simulation
from .economic_actors import AgentSam, AgentSME
from .reality_matrix import ParallelUniverse, EconomicBasin
from .vector_navigation import EndpointDeviationAudit

__all__ = [
    'DebtEntropyAudit', 'ChronocideCalculator', 'DignityAreaProtocol',
    'FutureHorizonEngine', 'GenesisProtocol', 'KiwicreditToken', 
    'GarbageCollector', 'EconomicOptimizer', 'TemporalSovereignty',
    'EconomyThread', 'WatchdogTimer', 'AgentSam', 'AgentSME',
    'ParallelUniverse', 'EconomicBasin', 'EndpointDeviationAudit'
]
