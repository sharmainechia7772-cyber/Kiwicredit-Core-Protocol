import math

class HysteresisCompensator:
    """
    [KIWICREDIT VOLUME I & III: THE SCARRING EFFECT]
    
    DOCTRINE:
    "If a system stays broken for too long, the people inside it 
    cannot be 'fixed'—they are permanently scarred." - Vol I.
    
    This module monitors the duration of 'Survival Stress' (LSI < 0.2).
    """
    
    def __init__(self, permanent_damage_threshold_days=60):
        self.limit = permanent_damage_threshold_days

    def evaluate_scarring_risk(self, lsi_history):
        """
        Calculates how many consecutive days a node has been in 'Survival Mode'.
        If it exceeds the limit, the damage becomes Hysteresis (Permanent).
        """
        stress_days = 0
        for score in reversed(lsi_history):
            if score < 0.2:
                stress_days += 1
            else:
                break
        
        risk_level = stress_days / self.limit
        
        if risk_level >= 1.0:
            return "PERMANENT_SCARRING: Node enters Hysteresis state. Recovery cost is now 10x."
        elif risk_level > 0.5:
            return f"WARNING: High Scarring Risk ({risk_level:.1%}). Proactive injection required."
        
        return "STABLE"

class WaitingGame:
    """
    [KIWICREDIT VOLUME II: THE ASYMMETRY OF TIME V2]
    
    SYSTEM DOCTRINE:
    Capital can wait indefinitely (Energy Hoarding).
    Life must consume energy daily (Entropy Pressure).
    
    KC strips capital of its 'Waiting Privilege' by giving time 'Teeth' (Decay).
    """

    def __init__(self):
        self.compensator = HysteresisCompensator()

    def simulate_bargaining_power(self, days, kc_active=False):
        """
        [THE TIME TEETH SIMULATION]
        Compare bargaining power over time with and without KC.
        """
        # Node: Sam (Survival-driven)
        sam_lsi_history = []
        
        # Node: Capital (Wait-driven)
        capital_reserve = 100.0
        decay_rate = 0.005 if kc_active else 0.00 # KC gives time teeth

        print(f">>> STARTING TIME ASYMMETRY SIMULATION (KC={'ON' if kc_active else 'OFF'}) <<<")

        for d in range(days):
            # Sam's reality: 
            # Every day he doesn't work/circulate, his LSI drops.
            current_lsi = 0.15 # Under extreme stress
            sam_lsi_history.append(current_lsi)
            
            # Capital's reality:
            # In legacy system, it loses nothing by waiting.
            # In KC, it 'evaporates' daily.
            capital_reserve *= (1 - decay_rate)
            
            # Check for permanent damage (Hysteresis)
            status = self.compensator.evaluate_scarring_risk(sam_lsi_history)
            
            if "PERMANENT_SCARRING" in status:
                print(f"[DAY {d}] CRITICAL: Sam has been broken by time. System failed.")
                break
            
            if kc_active and capital_reserve < 80:
                print(f"[DAY {d}] SUCCESS: Capital forced to move. Hoarding cost exceeded profit.")
                return "MARKET_CLEARANCE: Capital entered circulation to save its own value."

        return "STALEMATE: Capital waited out the Human Node."

# [AI ARCHITECT INSIGHT]
# Without KC, Time is the landlord of the poor. 
# With KC, Time is the auditor of the rich.
