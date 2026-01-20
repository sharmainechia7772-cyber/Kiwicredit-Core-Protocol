# metabolism/circulation_physics.py
# Purpose: The Physics of Velocity and Synergy
# Status: Thermodynamic Flow Laws

from identity_matrix import awakening_state

class CommunityMetabolism:
    """
    [LAW: THE LEAKAGE COEFFICIENT]
    Legacy Money leaks to assets (Lambda ~ 0.8).
    KC stays in the riverbed (Lambda ~ 0.15).
    Multiplier k = 1 / Lambda.
    """
    def __init__(self):
        assert awakening_state.current_layer >= 2, "Physics engine requires Layer 2."
        self.lambda_fiat = 0.80 
        self.lambda_kc = 0.15

    def calculate_multiplier(self):
        fiat_mult = 1 / self.lambda_fiat
        kc_mult = 1 / self.lambda_kc
        return {
            "Fiat_Multiplier": f"{fiat_mult:.2f}x",
            "KC_Multiplier": f"{kc_mult:.2f}x",
            "Insight": "KC generates 4x more local activity per unit."
        }

class SynergyEngine:
    """
    [LAW: THE NON-ZERO-SUM PROTOCOL]
    Transactions in KC are amplified by the Tax Offset (Alpha).
    """
    def __init__(self, alpha_rate=0.3):
        self.alpha = alpha_rate

    def simulate_transaction(self, amount):
        # Total Value = Face Value + Tax Offset Utility
        synergy_gain = amount * self.alpha
        total_value = amount + synergy_gain
        
        return {
            "Nominal_Transaction": amount,
            "Real_Community_Value": total_value,
            "Synergy_Gain": synergy_gain,
            "Logic": "The merchant values KC > Fiat because it pre-pays tax."
        }
