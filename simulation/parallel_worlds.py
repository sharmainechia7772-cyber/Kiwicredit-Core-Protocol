import time

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
        print("[BANKS] Action: Lending to Mortgage Market (Safe Collateral). Refusing small biz loans.")
        print("[MARKET] Result: House Prices UP 10%. Rents increase.")
        
        # 4. Chen's Reaction
        print("[CHEN] Status: Rent is up. Worried about losing job.")
        print("[CHEN] Action: CUTS SPENDING. Stops buying daily coffee ($5/day saved).")
        
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
        print(">>> WORLD B OUTCOME: SOFT LANDING. (Employment Stable, LSI Protected).")

if __name__ == "__main__":
    sim = ParallelUniverse()
    sim.run_simulation()
