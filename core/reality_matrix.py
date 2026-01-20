# core/reality_matrix.py
# Source: parallel_worlds.py + basin_attractor.py (MERGED FULL VERSION)
# Status: The Simulation Engine & Topography Proof

import time
import numpy as np
from identity_matrix import awakening_state

# ==============================================================================
# PART 1: THE PARALLEL UNIVERSE (World A vs World B)
# ==============================================================================

class ParallelUniverse:
    """
    [KIWICREDIT MANUSCRIPT SIMULATION: CHAPTER 3 & 6]
    
    SCENARIO: "THE RECESSION SHOCK"
    External Demand drops by 20%. Unemployment starts to rise.
    
    ACTORS:
    1. CHEN (Middle Income Household): Earns wages, pays rent, fears the future.
    2. LOCAL CAFE (Small Business): Needs cash flow, hates taxes.
    3. GOVERNMENT (The Treasury): Needs to stabilize the system.
    """

    def __init__(self):
        # Requires full awakening to operate the Matrix
        assert awakening_state.current_layer >= 2

    def run_simulation(self):
        print(">>> INITIALIZING PARALLEL WORLDS SIMULATION <<<\n")
        
        # --- WORLD A: THE LEGACY FIAT SYSTEM ---
        print("--- [WORLD A] LEGACY SYSTEM (FIAT ONLY) ---")
        self.simulate_world_a()
        
        print("\n" + "="*40 + "\n")

        # --- WORLD B: THE KIWICREDIT SYSTEM ---
        print("--- [WORLD B] KIWICREDIT PROTOCOL (DUAL TRACK) ---")
        self.simulate_world_b()

    def simulate_world_a(self):
        """
        [The Doom Loop]
        Rationale: Rational individual fear leads to collective collapse (Keynes' Paradox of Thrift).
        """
        # 1. The Shock
        print("[EVENT] Recession hits. Uncertainty spikes.")
        
        # 2. Government Action
        print("[GOV] Action: Central Bank cuts rates. Printing $10B QE to Banks.")
        
        # 3. Transmission Mechanism (Broken)
        print("[BANKS] Action: Hoard liquidity to shore up balance sheets. Lending DROPS.")
        
        # 4. Chen's Reaction
        print("[CHEN] Status: Worried about layoff. Sees neighbor fired.")
        print("[CHEN] Action: Cuts discretionary spending (Coffee, Movies). Saves Cash.")
        
        # 5. Cafe's Reaction
        print("[CAFE] Status: Revenue down 30% (Chen and others stopped coming).")
        print("[CAFE] Action: FIRES STAFF to survive.")
        
        # 6. Outcome
        print(">>> WORLD A OUTCOME: STAGFLATION. (Assets Up, Real Economy Dead). LSI: CRITICAL.")

    def simulate_world_b(self):
        """
        [The Rescue]
        Rationale: KC breaks the Paradox of Thrift by enforcing circulation.
        """
        # 1. The Shock
        print("[EVENT] Recession hits. Uncertainty spikes.")
        
        # 2. Government Action (Crisis Protocol)
        print("[GOV] Action: Activate KCQE. Raise r(Y) refund rate for bottom 50% to 80%.")
        print("[GOV] Note: No debt created. Future tax credits issued.")
        
        # 3. Chen's Reaction
        print("[CHEN] Status: Cash is tight, BUT received 200 KC expiry-dated tokens.")
        print("[CHEN] Thought: 'I can't hoard this KC. It decays. I might as well use it.'")
        print("[CHEN] Action: Buys coffee and lunch using KC.")
        
        # 4. Cafe's Reaction
        print("[CAFE] Status: Cash sales down, BUT KC sales up. Total volume stable.")
        print("[CAFE] Calculation: 'If I accept KC, my effective tax rate drops from 28% to 19%'.")
        print("[CAFE] Action: KEEPS STAFF. (Labor is paid in Fiat, offset by tax savings).")
        
        # 5. Outcome
        print(">>> WORLD B OUTCOME: SOFT LANDING. Employment maintained. Vitality Preserved.")

# ==============================================================================
# PART 2: THE BASIN ATTRACTOR (Topography)
# ==============================================================================

class ConfidenceLoop:
    """
    [KIWICREDIT VOLUME III: THE SOCIAL ANCHOR]
    
    DOCTRINE:
    "Currency is not just math; it is a shared hallucination." - Vol III.
    
    This module simulates how 'Social Confidence' affects the depth of the Basin.
    """
    def __init__(self, initial_trust=1.0):
        self.trust = initial_trust

    def adjust_trust(self, price_stability, lsi_score):
        # Trust grows when LSI is high and prices are stable.
        if lsi_score > 0.5 and abs(price_stability) < 0.05:
            self.trust = min(1.2, self.trust + 0.01)
        else:
            self.trust = max(0.4, self.trust - 0.05)
        return self.trust

class EconomicBasin:
    """
    [KIWICREDIT VOLUME III & IV: STABILITY BASIN V2]
    
    COMPARISON:
    1. Legacy Equilibrium: A simple pendulum. Assumes one 'Good' center.
    2. KC Basin Theory: A landscape with multiple valleys (Attractors).
    """

    def __init__(self):
        self.confidence = ConfidenceLoop()

    def simulate_landscape(self, state_vector, kc_enabled=False):
        """
        [THE TOPOGRAPHY OF REALITY]
        state_vector: [Employment_Rate, Fear_Level]
        """
        # THE SUFFOCATING STABLE STATE (The Trap)
        # Low Employment (0.4), High Fear (0.8). 
        # In Legacy theory, this is 'Bad Equilibrium'. 
        # In Basin theory, this is a deep pit that is hard to escape.
        
        print(f"\n>>> AUDITING SYSTEM TOPOGRAPHY (KC_MODE: {kc_enabled}) <<<")

        if not kc_enabled:
            print("[LEGACY MODEL] Danger: System is sliding into the 'Suffocating Stable State'.")
            print("[ANALYSIS] Stability is high (Entropy is low), but LSI is near zero.")
            return "RESULT: THE STAGNATION TRAP. Order is maintained, but humanity is crushed."

        # KC Strategy: Using 'r(Y)' and 'Decay' to change the landscape
        trust_level = self.confidence.adjust_trust(0.02, 0.7)
        
        if trust_level > 0.8:
            print(f"[KC MODEL] Confidence ({trust_level:.2f}) is reshaping the landscape.")
            print("[ANALYSIS] Gravity is pulling the system toward the 'Vitality Basin'.")
            return "RESULT: DYNAMIC PROSPERITY. The trap has been shallow-filled by KC liquidity."
        
        return "RESULT: TRANSITION_PHASE. System is climbing out of the pit."

# [AI ARCHITECT INSIGHT]
# Equilibrium Theory is blind to 'Basin Depth'.
# KC creates a new 'Strange Attractor' (The Vitality Basin) that naturally 
# pulls the economy towards Full Employment without needing constant intervention.
