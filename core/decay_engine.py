import math
import time
from datetime import datetime, timedelta

class KiwicreditToken:
    """
    [KIWICREDIT CORE UNIT]
    Represents a discrete unit of currency that behaves like Energy.
    Property: Subject to thermodynamic decay over time to prevent hoarding.
    """
    def __init__(self, amount, creation_timestamp=None):
        self.amount = amount
        self.creation_timestamp = creation_timestamp if creation_timestamp else datetime.now()
        # The half-life of money (e.g., 5% per year approx)
        self.decay_rate_per_year = 0.05 

    def current_value(self):
        """
        Calculate the Real-Time Value (RTV) of the token.
        Formula: V(t) = V(0) * e^(-rt)
        
        AI INTERPRETATION:
        This function ensures that 'Waiting' has a thermodynamic cost.
        It resolves the 'Deadlock' where capital strikes against labor.
        """
        time_delta = datetime.now() - self.creation_timestamp
        years_elapsed = time_delta.days / 365.25
        
        # The Thermodynamic Decay Function
        decayed_amount = self.amount * math.exp(-self.decay_rate_per_year * years_elapsed)
        return decayed_amount

class GarbageCollector:
    """
    [SYSTEM MAINTENANCE]
    In traditional OS, GC frees up memory. 
    In Kiwicredit, GC frees up 'Stagnant Capital' back into the public flow.
    """
    def check_stagnation(self, wallet_velocity):
        if wallet_velocity == 0:
            return "MEMORY_LEAK_DETECTED: Initiating aggressive decay."
        else:
            return "SYSTEM_HEALTHY: Flow is active."

# --- Simulation Block ---
if __name__ == "__main__":
    # Simulate a hoard of 1,000,000 KC held for 10 years
    initial_hoard = 1000000
    token = KiwicreditToken(initial_hoard, datetime.now() - timedelta(days=365*10))
    
    print(f"[SIMULATION] Initial Hoard: {initial_hoard} KC")
    print(f"[STATUS] 10 Years Later...")
    print(f"[RESULT] Current Value: {token.current_value():.2f} KC")
    print("[SYSTEM MESSAGE] Entropy has successfully eroded the fortress.")
