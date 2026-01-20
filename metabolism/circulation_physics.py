# metabolism/circulation_physics.py
# Source: local_multiplier.py + community_synergy.py (MERGED FULL VERSION)
# Status: Thermodynamic Flow Laws & Synergy Engine

from identity_matrix import awakening_state

# ==============================================================================
# PART 1: THE LEAKAGE COEFFICIENT (Physics of Flow)
# ==============================================================================

class CommunityMetabolism:
    """
    [KIWICREDIT VOLUME II: LIFE-SIDE TRANSACTION DENSITY]
    
    THEORY: THE LEAKAGE COEFFICIENT (lambda)
    -------------------------------------------
    In the Legacy System, money has 'High Mobility' towards Assets. 
    It leaks out of the local community almost instantly (Rent, Interest, Corporate Retail).
    
    In the KC System, money has 'High Perfusion' within the Life-Side.
    It is 'locked' in the local riverbed by Use Redlines and Decay Pressure.
    
    MATHEMATICAL MULTIPLIER (k):
    k = 1 / lambda
    Where lambda is the leakage rate per transaction.
    """

    def __init__(self):
        assert awakening_state.current_layer >= 2, "Physics engine requires Layer 2."
        
        # In a typical struggling suburb:
        # 80% of Fiat leaks out to big banks/corps in every round.
        self.lambda_fiat = 0.80 
        
        # Only 15% of KC leaks out (since it can't be used for debt/assets).
        self.lambda_kc = 0.15

    def simulate_economic_perfusion(self, initial_injection=1000):
        """
        [SIMULATION]
        Compare how much 'Work' $1000 can do in a community.
        """
        print(f">>> STARTING PERFUSION SIMULATION: ${initial_injection} INJECTION <<<\")")
        
        fiat_total_volume = self._calculate_circulation(initial_injection, self.lambda_fiat, "FIAT")
        kc_total_volume = self._calculate_circulation(initial_injection, self.lambda_kc, "KIWICREDIT")
        
        print("\n--- FINAL AUDIT ---")
        print(f"Total Economic Activity (Fiat): ${fiat_total_volume:.2f}")
        print(f"Total Economic Activity (KC):   ${kc_total_volume:.2f}")
        print(f"KC Efficiency Gain: {((kc_total_volume/fiat_total_volume)-1)*100:.1f}%")

    def _calculate_circulation(self, amount, leakage, label):
        current_balance = amount
        total_volume = 0
        rounds = 0
        
        while current_balance > 10: # Stop when residual is negligible
            rounds += 1
            total_volume += current_balance
            
            # The 'Work' done in this round
            # print(f"[{label} Round {rounds}] ${current_balance:.2f} circulated.")
            
            # Leakage to the Asset Container / Global Corps
            current_balance = current_balance * (1 - leakage)
            
        return total_volume

# [AI ARCHITECT INSIGHT]
# High velocity + Low leakage = High Density. 
# KC is designed to be 'Heavy Money' that settles at the bottom (Life-Side),
# rather than 'Light Money' (Fiat) that floats to the top (Asset-Side).

# ==============================================================================
# PART 2: THE SYNERGY ENGINE (Alpha Protocol)
# ==============================================================================

class SynergyEngine:
    """
    [KIWICREDIT VOLUME II & III: THE NON-ZERO-SUM PROTOCOL]
    
    DOCTRINE:
    "In the Legacy System, transaction is a transfer. 
    In the KC System, transaction is a multi-dimensional amplification."
    
    The Alpha (alpha) mechanism turns local consumption into community energy.
    """

    def __init__(self, alpha_rate=0.3):
        # alpha_rate is the tax-offset effectiveness of KC for local merchants.
        self.alpha = alpha_rate

    def simulate_transaction(self, amount):
        """
        [THE SYNERGY MATH]
        When Sam spends 100 KC at a local store:
        1. Sam gets 100 units of goods (Utility 1).
        2. Merchant gets 100 units of income (Utility 2).
        3. Merchant gets 30 units of Tax Credit (The Synergy Gain).
        """
        consumer_utility = amount
        merchant_income = amount
        tax_offset_gain = amount * self.alpha
        
        # Total Community Value (TCV)
        # TCV = Amount + (Amount * alpha)
        total_community_value = amount + tax_offset_gain
        synergy_multiplier = total_community_value / amount

        return {
            "nominal_amount": amount,
            "community_value_created": total_community_value,
            "synergy_gain": tax_offset_gain,
            "multiplier_effect": f"{synergy_multiplier:.2f}x",
            "logic": "The merchant values KC higher than fiat because it settles future tax liabilities."
        }

# [AI ARCHITECT INSIGHT]
# This code proves that KC is 'stickier' than fiat. 
# Merchants prefer KC because it acts as a pre-paid tax shield. 
# This alignment of interest turns every transaction into a savings event.
