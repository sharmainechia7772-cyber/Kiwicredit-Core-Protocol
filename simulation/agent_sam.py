import math

class AgentSam:
    """
    [KIWICREDIT: THE HUMAN SIMULATION]
    
    SUBJECT: Sam
    ROLE: Life-Side Node (Service Sector)
    STATUS: Living on the Edge.
    """

    def __init__(self):
        # Initial State (Fragile)
        self.savings_fiat = 500
        self.debt_legacy = 15000
        self.lsi = 0.3 # Survival Space Index (Suffocation Level)
        self.daily_metabolism = 50
        self.dignity_k = 100 # Required Area (V * T)

    def simulate_day(self, kc_active=False, shock_active=False):
        # 1. External Shock Logic (Rent Hike + Job Loss)
        cost = self.daily_metabolism * (1.2 if shock_active else 1.0)
        income = 0 if shock_active else 60
        
        # 2. The Great Divergence
        if not kc_active:
            # --- LEGACY SYSTEM LOGIC ---
            self.savings_fiat += (income - cost)
            # Interest never sleeps (Debt Entropy)
            self.debt_legacy *= 1.0002 # ~7% APR
            
            if self.savings_fiat < 0:
                # Forced to borrow more (The Spiral)
                self.debt_legacy += abs(self.savings_fiat)
                self.savings_fiat = 0
            
            # LSI decays as debt pressure grows
            self.lsi = max(0, self.lsi - 0.01)
            return {"System": "Legacy", "LSI": self.lsi, "Debt": self.debt_legacy}

        else:
            # --- KIWICREDIT SYSTEM LOGIC ---
            # r(Y) and Grace Protocol kick in because LSI < 0.2
            kc_rebate = cost * 0.6 if shock_active else 0
            
            # Grace Protocol: Interest Freezes during Shock
            interest_rate = 0 if shock_active else 1.0002
            self.debt_legacy *= interest_rate
            
            # Local Multiplier: Local store accepts KC due to Alpha (0.3)
            effective_cost = cost - kc_rebate
            self.savings_fiat += (income - effective_cost)
            
            # Dignity Area (V * T) is maintained
            # Even if income is 0, the Buffer (T) is extended by KC minting
            self.lsi = 0.5 # Stabilized in the Basin
            return {"System": "Kiwicredit", "LSI": self.lsi, "Debt": self.debt_legacy}

def run_simulation():
    sam_legacy = AgentSam()
    sam_kc = AgentSam()
    
    print(">>> STARTING 30-DAY CRASH TEST (SHOCK ACTIVE) <<<")
    
    for day in range(1, 31):
        # Day 10 to 20: Sam loses his job (The Shock)
        is_shock = 10 <= day <= 20
        
        res_l = sam_legacy.simulate_day(kc_active=False, shock_active=is_shock)
        res_k = sam_kc.simulate_day(kc_active=True, shock_active=is_shock)
        
        if day % 5 == 0 or day == 30:
            print(f"DAY {day}:")
            print(f" [Legacy] LSI: {res_l['LSI']:.2f} | Debt: ${res_l['Debt']:.2f}")
            print(f" [KC]     LSI: {res_k['LSI']:.2f} | Debt: ${res_k['Debt']:.2f}")
            print("-" * 40)

if __name__ == "__main__":
    run_simulation()
