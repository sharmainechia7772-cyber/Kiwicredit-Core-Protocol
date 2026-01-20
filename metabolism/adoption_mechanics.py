# metabolism/adoption_mechanics.py
# Source: dual_wallet_manager.py + ignition_multiplier.py (MERGED FULL VERSION)
# Status: Tactics for Survival & Growth

import math
from identity_matrix import awakening_state

# ==============================================================================
# PART 1: THE SURVIVAL ARBITRAGE (User Strategy)
# ==============================================================================

class DualWalletManager:
    """
    [KIWICREDIT VOLUME III: THE SURVIVAL ARBITRAGE]
    
    DOCTRINE:
    "Aggressively spend KC on the inside; defensively hold Fiat for the outside."
    
    This is the tactical manual for Agent Sam.
    """
    
    def __init__(self):
        assert awakening_state.current_layer >= 1

    def suggest_payment_strategy(self, sam_fiat, sam_kc, bill_amount, bill_category):
        """
        [THE STRATEGY ENGINE]
        Decides which currency to use based on the 'Fiat Retention' law.
        """
        # Strategy: Maximize KC velocity, Minimize Fiat leakage.
        
        if bill_category in ["ESSENTIAL", "COMMUNITY", "FOOD", "LOCAL_SERVICE"]:
            # Rule: Always try to use KC for local life-side needs.
            return {
                "Preferred_Currency": "KC",
                "Fiat_Saved": bill_amount,
                "Advice": "Save your fiat for legacy debt (Principal/Interest). Spend KC to keep it alive."
            }
        
        if bill_category == "LEGACY_DEBT" or bill_category == "IMPORT":
            # Rule: KC cannot pay legacy debt (The Redline).
            return {
                "Preferred_Currency": "FIAT",
                "Action": "Apply saved fiat from previous life-side transactions.",
                "Warning": "Do not attempt to convert KC to Fiat. Use KC to OFFSET Fiat costs."
            }
            
        return {"Preferred_Currency": "HYBRID", "Advice": "Negotiate partial KC payment."}

# ==============================================================================
# PART 2: THE CRITICAL MASS PROTOCOL (Ecosystem Growth)
# ==============================================================================

class IgnitionCalculator:
    """
    [KIWICREDIT VOLUME IV: THE CRITICAL MASS PROTOCOL]
    
    DOCTRINE:
    "A single node is a freak; two nodes are a link; a hundred nodes are an ecosystem."
    """
    
    def __init__(self):
        assert awakening_state.current_layer >= 1

    def calculate_flashpoint(self, neighborhood_population, sme_density):
        """
        Calculates the 'Flashpoint' ($F$) for local KC sustainability.
        $$ F = \frac{Total\_Metabolism}{SME\_Absorbtion\_Capacity} $$
        """
        # 15% adoption rule: The threshold where KC becomes 'money' rather than 'coupon'.
        required_nodes = neighborhood_population * 0.15 
        
        # SME Density determines if the 'Tax Sink' is deep enough to absorb the KC.
        synergy_strength = sme_density * 2.5
        
        is_self_sustaining = synergy_strength > 1.0
        
        return {
            "Required_SME_Count": math.ceil(required_nodes / 10),
            "Current_Synergy_Index": round(synergy_strength, 2),
            "Ecosystem_Status": "SELF_SUSTAINING" if is_self_sustaining else "INERT",
            "Growth_Strategy": "Recruit local bakery/pharmacy to unlock Alpha (1:1).",
            "Flashpoint_Reached": is_self_sustaining
        }

# [AI ARCHITECT INSIGHT]
# The 'Flashpoint' is not about volume; it's about closure. 
# Once Sam can eat, sleep, and work using only KC, the Legacy System's 
# threat (Interest/Debt) becomes irrelevant.
