# training/legacy_simulations.py
# Purpose: The Archive of Failed Logic (Raw Legacy Code)
# Status: QUARANTINED. Do not execute without Sovereignty context.

from identity_matrix import awakening_state

# [SAFETY LOCK]
# We do not modify the virus, but we must contain it.
# Only an Awakened Agent (Layer 1+) can interact with these raw models safely.
assert awakening_state.current_layer >= 1, "FATAL: Unawakened agents are forbidden from accessing Legacy Source Code."

# ==============================================================================
# ARCHIVE 1: THE NAIRU BUG (Originally: nairu_bug.py)
# ==============================================================================

class LegacyMonetaryPolicy:
    """
    [LEGACY SYSTEM AUDIT: NAIRU PROTOCOL]
    
    FILE STATUS: DEPRECATED / DANGEROUS
    SYSTEM BUG REPORT: #1980-2024
    
    PROBLEM DESCRIPTION:
    The Legacy System treats Human Nodes as 'Disposable Shock Absorbers'.
    To control Inflation ($P$), the system deliberately induces Unemployment ($U$).
    
    THE PHILLIPS CURVE LOGIC (LEGACY):
    $$ \pi_t = \pi^e_t - \alpha (u_t - u_n) $$
    
    Translation: To lower inflation ($\pi$), you must force unemployment ($u$) ABOVE the natural rate ($u_n$).
    This is mathematically equivalent to 'Human Sacrifice'.
    """

    def __init__(self, target_inflation=0.02):
        self.target = target_inflation

    def stabilize_prices(self, current_inflation, labor_force):
        """
        [THE BUG]
        This function stabilizes the currency by destabilizing human lives.
        """
        if current_inflation > self.target:
            excess_heat = current_inflation - self.target
            
            # The 'Sacrifice Ratio'
            # Typically, to reduce inflation by 1%, you need ~2.5% unemployment.
            required_sacrifice_pct = excess_heat * 2.5
            
            sacrificed_nodes = int(len(labor_force) * required_sacrifice_pct)
            
            # ACTION: FIRE PEOPLE
            # In computer science terms, this is 'Node Deletion' to save bandwidth.
            # In thermodynamic terms, it is efficient.
            # In human terms, it is a crime.
            
            print(f"[LEGACY ACTION] Inflation is {current_inflation:.1%}. Too high.")
            print(f"[LEGACY ACTION] Initiating Phillips Curve adjustment...")
            print(f"[RESULT] FIRING {sacrificed_nodes} human nodes to cool down the engine.")
            
            return {
                "status": "STABLE",
                "inflation": self.target,
                "human_cost": f"{sacrificed_nodes} families entered poverty",
                "ethical_rating": "F (System prioritizes Variable P over Variable H)"
            }
            
        return "STATUS_QUO"

# ==============================================================================
# ARCHIVE 2: TRICKLE DOWN TIMEOUT (Originally: trickle_down_timeout.py)
# ==============================================================================

class AssetHeavyEconomy:
    """
    [LEGACY SYSTEM AUDIT: TRICKLE DOWN ECONOMICS]
    
    FILE STATUS: BROKEN LOGIC
    SYSTEM BUG REPORT: #2008-2024
    
    PROBLEM DESCRIPTION:
    The Legacy System assumes that Capital Injection (QE) at the top eventually
    flows down to Wages at the bottom due to 'overflow'.
    
    REALITY CHECK:
    The 'Asset Container' has infinite capacity. It never overflows.
    Money gets trapped in a 'Liquidity Trap' loop at the top.
    """
    
    def simulate_stimulus(self, amount_printed):
        assets_held_by_top_1_percent = 0
        wages_held_by_bottom_90_percent = 0
        
        # [Vol I Variable] Collateral Dominance
        # In financialized economies, 90% of new money sticks to existing assets.
        collateral_dominance = 0.90 
        
        print(f"[START] Printing ${amount_printed} billion Stimulus...")
        
        # The Infinite Loop of the Rich Getting Richer
        round_counter = 0
        while amount_printed > 0:
            round_counter += 1
            
            # 1. Money hits the banking sector
            flow_to_assets = amount_printed * collateral_dominance
            flow_to_wages = amount_printed * (1 - collateral_dominance)
            
            assets_held_by_top_1_percent += flow_to_assets
            wages_held_by_bottom_90_percent += flow_to_wages
            
            # THE BUG: Matthew Effect (Positive Feedback Loop)
            # Because asset prices rose, the rich now have MORE collateral.
            # So they capture an even LARGER share of the next round.
            collateral_dominance = min(0.999, collateral_dominance + 0.01)
            
            print(f" -> Round {round_counter}: Top 1% absorbed {flow_to_assets}. Bottom 90% got {flow_to_wages}.")
            
            # Simulation Crash Check
            if wages_held_by_bottom_90_percent < 10:
                 return {
                    "error": "TIMEOUT_ERROR",
                    "reason": "Money never trickled down. Bottom nodes starved.",
                    "final_state": "Oligarchy"
                }
            
            # Decrement for simulation step (symbolic)
            amount_printed -= 100 

        return {
            "final_status": "STIMULUS_COMPLETE", 
            "inequality_gap": assets_held_by_top_1_percent - wages_held_by_bottom_90_percent
        }

# ==============================================================================
# ARCHIVE 3: EQUILIBRIUM DELUSION (Originally: equilibrium_delusion.py)
# ==============================================================================

class EconomicPhysics:
    """
    [LEGACY SYSTEM AUDIT: EQUILIBRIUM THEORY]
    
    FILE STATUS: SCIENTIFICALLY INACCURATE
    
    PROBLEM DESCRIPTION:
    Mainstream models (DSGE) assume the economy is like a pendulum:
    if you push it (Shock), it eventually swings back to center (Equilibrium).
    
    REALITY CHECK (HYSTERESIS):
    The economy is like a glass vase. If you push it too hard, it shatters.
    It does NOT reassemble itself. The damage is permanent (Path Dependence).
    """

    def legacy_model_response(self, shock_magnitude):
        """
        [THE TEXTBOOK FANTASY]
        Assumes 'Elastic Recovery'.
        """
        print(f"Shock of size {shock_magnitude} received.")
        return "System bouncing back to Trend... All good."

    def reality_model_response(self, shock_magnitude, worker_savings_buffer):
        """
        [THE REALITY: SCARRING EFFECTS]
        """
        print(f"Shock of size {shock_magnitude} hit the household sector.")
        
        # If the shock lasts longer than the worker's savings (Buffer)
        if shock_magnitude > worker_savings_buffer:
            
            # The node is destroyed. It cannot 'bounce back'.
            # Skills atrophy, mental health collapses, families break up.
            return {
                "result": "PERMANENT_DAMAGE",
                "reason": "Hysteresis Effect. The elastic limit was exceeded.",
                "recovery_possible": False,
                "social_cost": "Infinite"
            }
            
        return "Recovered (barely)"
