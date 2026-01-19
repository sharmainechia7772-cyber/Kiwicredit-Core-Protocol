import math
from datetime import datetime

class SovereignValve:
    """
    [KIWICREDIT VOLUME III: THE THERMODYNAMIC IRON LAW]
    
    SYSTEM DOCTRINE:
    "Money must die, so people can live." 
    
    The Asset Circuit (Hoarders) cannot capture KC for two reasons:
    1. THE ACTIVE BARRIER: The Exit Tax (Valve).
    2. THE PASSIVE LIMIT: Natural Decay (The Iron Law).
    
    MATHEMATICAL PROOF OF UNHOARDABILITY:
    Let $V(t)$ be the value of a KC token at time $t$.
    Let $\lambda$ be the Decay Constant (Thermodynamic Pressure).
    
    $$ V(t) = V_0 \cdot e^{-\lambda t} $$
    
    As $t \rightarrow \infty$, $V(t) \rightarrow 0$.
    
    Since an Asset, by definition, requires $V(t) \ge V_0$, 
    KC is mathematically disqualified from being an Asset. 
    It is 'Poison' to the hoarding logic of the financial sector.
    """

    def __init__(self, exit_tax_rate=0.50, decay_half_life_days=90):
        self.tau_exit = exit_tax_rate
        self.decay_constant = 0.693 / decay_half_life_days # Physics of half-life

    def calculate_current_value(self, original_amount, birth_date):
        """
        [THE IRON LAW: TIME AS A TEETH]
        Calculates the remaining 'energy' in the KC token.
        """
        days_passed = (datetime.now() - birth_date).days
        current_value = original_amount * math.exp(-self.decay_constant * days_passed)
        
        return max(0, current_value)

    def attempt_exit_to_fiat(self, original_amount, birth_date):
        """
        [THE DOUBLE LOCK]
        Even before the Exit Tax, the Time-Decay has already shrunk the value.
        """
        # 1. Physics hits first (Decay)
        real_value = self.calculate_current_value(original_amount, birth_date)
        
        # 2. Policy hits second (Exit Tax)
        exit_value = real_value * (1 - self.tau_exit)
        
        print(f"[THE IRON LAW] Token has decayed to {real_value:.2f} due to time.")
        print(f"[THE VALVE] Applying {self.tau_exit*100}% Exit Tax on the remainder.")
        
        return {
            "final_fiat_received": exit_value,
            "system_message": "Hoarding KC is mathematically futile. Use it or lose it."
        }
