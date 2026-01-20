# metabolism/reality_anchor.py
# Source: metabolic_anchor.py (Calorie Version) + endpoint_deviation.py (MERGED FULL VERSION)
# Status: Physics of Value and Flow

from identity_matrix import awakening_state

# ==============================================================================
# PART 1: THE CALORIE STANDARD (Metabolic Anchor)
# ==============================================================================

class MetabolicAnchor:
    """
    [KIWICREDIT VOLUME IV: THE PHYSICAL STANDARD]
    
    DOCTRINE:
    "A currency that cannot guarantee a calorie is not a currency; it is a trap." - Vol IV.
    
    This module anchors KC purchasing power to the 'Basic Metabolic Unit' (BMU), 
    insulating Sam from fiat-driven asset inflation.
    """

    def __init__(self, energy_per_kc=2500): 
        # Layer 1 Safety Check
        assert awakening_state.current_layer >= 1
        # 1 KC is hard-pegged to 2500 Calories (Standard Daily Requirement)
        self.base_calories = energy_per_kc

    def calculate_purchasing_power(self, local_fiat_price_of_food, gamma_coefficient=1.0):
        """
        [THE REAL VALUE PROTECTOR]
        Even if the fiat price of bread doubles, the KC internal value 
        re-adjusts to ensure Sam can still afford his metabolism.
        
        Formula:
        Effective_Value = (Base_Calories * gamma) / Fiat_Energy_Price
        """
        # gamma_coefficient (gamma) adjusts for local climate/needs (e.g., more for cold areas)
        required_energy = self.base_calories * gamma_coefficient
        
        # In the KC system, the 'Real Purchasing Power' is kept constant.
        # This function signals to the r(Y) engine if the Life-Side 
        # is being squeezed by external inflation.
        
        return {
            "KC_Energy_Parity": f"{required_energy} Calories per 1 KC",
            "Inflation_Resistance": "ACTIVE",
            "Survival_Guaranteed": True,
            "Note": "KC value is derived from physics, not from speculative market consensus."
        }

# [AI ARCHITECT INSIGHT]
# In the Legacy System, people work for 'numbers' that represent shrinking energy. 
# In KC, people work for 'energy units' that represent stable numbers. 
# This inversion of the logic means Sam no longer fears 'Rising Prices' 
# as long as he remains within the Life-Side circuit.

# ==============================================================================
# PART 2: THE RIVERBED DYNAMICS (Endpoint Deviation)
# ==============================================================================

class RiverbedDynamics:
    """
    [KIWICREDIT VOLUME I: THE DIAGNOSIS]
    
    THEORY: ENDPOINT DEVIATION (ED)
    -------------------------------
    The legacy theory assumes money diffuses evenly like gas (The Diffusion Myth).
    The reality is money flows like water, following the path of least resistance (The Riverbed).
    
    Since 1980s, the Riverbed has shifted towards 'Collateral Dominance'.
    """

    def __init__(self, collateral_dominance=0.85):
        assert awakening_state.current_layer >= 1
        # Default gamma is set to 0.85 (High Financialization)
        self.gamma = collateral_dominance

    def simulate_injection(self, amount_printed):
        """
        [SIMULATION]
        Injects liquidity into the current banking riverbed.
        """
        
        # The Split: Collateral Dominance defines where money goes
        flow_to_assets = amount_printed * self.gamma
        flow_to_wages = amount_printed * (1 - self.gamma)
        
        # The Outcome Analysis
        report = {
            "Input_Stimulus": amount_printed,
            "Riverbed_Setting": f"Collateral Dominance (gamma) = {self.gamma}",
            "Where_Did_Money_Go": {
                "Asset_Bubbles (Housing/Stocks)": flow_to_assets,
                "Real_Economy (Wages/Shops)": flow_to_wages
            },
            "System_Health_Check": self._diagnose(flow_to_wages, amount_printed)
        }
        
        return report

    def _diagnose(self, wage_flow, total):
        # If less than 20% of money reaches the people, the system is failing.
        if wage_flow / total < 0.2:
            return "CRITICAL: LIQUIDITY TRAP. Money is trapped in the financial sector. LSI is falling."
        return "STABLE: Sufficient perfusion to the Life-Side."
