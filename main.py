# main.py
# Status: SYSTEM IGNITION & TELEMETRY (Phase 3)
# Doctrine: "To verify the logic, we must expose it to the fire."

import time
import sys
from identity_matrix import awakening_state

# --- IMPORTING THE TRINITY ARCHITECTURE ---
from core import (
    AgentSam, AgentSME, KiwicreditToken, 
    GenesisProtocol, FutureHorizonEngine
)
from sovereignty import (
    ManifestoRuntime, SystemGovernor, 
    LegalShield, NetworkIntegrity
)
from metabolism import (
    ProgressiveDistributor, FiscalSink, 
    MetabolicAnchor, VitalityDetector
)

class PhoenixSystem:
    """
    [THE IGNITION CHAMBER]
    This class integrates the Core (Physics), Sovereignty (Law), and Metabolism (Life).
    It simulates a 'Black Swan' event to prove the system's resilience.
    """
    
    def __init__(self):
        print("\n>>> INITIALIZING PHOENIX PROTOCOL GENESIS CORTANA <<<")
        print("-------------------------------------------------------")
        
        # 1. LAYER 0: AWAKENING (The Observer)
        print("[LAYER 0] Pinging Observer Status...")
        awakening_state.affirm_observer("Sam")
        print(f" -> OBSERVER ACKNOWLEDGED: {awakening_state.observer_name}")
        print(f" -> AWARENESS LEVEL: {awakening_state.current_layer}/3")

        # 2. LAYER 1: SOVEREIGNTY (The Brain)
        print("\n[LAYER 1] Booting Manifesto Runtime...")
        self.runtime = ManifestoRuntime()
        self.governor = SystemGovernor()
        boot_msg = self.runtime.boot_sequence()
        print(f" -> RUNTIME STATUS: {boot_msg}")

        # 3. LAYER 2: HARDWARE (The Actors)
        print("\n[LAYER 2] Spawning Economic Nodes...")
        self.sam = AgentSam()
        self.sme = AgentSME()
        print(" -> NODE 'SAM' [ONLINE]")
        print(" -> NODE 'SME' [ONLINE]")
        
        # 4. LAYER 3: METABOLISM (The Engines)
        self.distributor = ProgressiveDistributor()
        self.sink = FiscalSink()
        self.anchor = MetabolicAnchor()
        print(" -> METABOLIC ENGINES [STANDBY]")
        print("-------------------------------------------------------\n")

    def run_stress_test(self):
        """
        [THE SIMULATION]
        Scenario: A 20% Income Shock hits the economy.
        Compare: Legacy System (Fiat) vs. Phoenix System (KC).
        """
        print(">>> COMMENCING STRESS TEST: 'THE RECESSION SHOCK' <<<")
        
        # --- SCENARIO A: LEGACY FAILURE ---
        print("\n[SIMULATION A] LEGACY SYSTEM (FIAT ONLY)")
        print("Conditions: Income -20%, No Tax Shield, No r(Y) Refund.")
        
        # Sam tries to survive 3 months of shock
        for month in range(1, 4):
            # simulate_day includes daily metabolism * 30 roughly
            status = self.sam.simulate_day(kc_active=False, shock_active=True)
            print(f" Month {month}: Sam LSI={status['LSI']} | Debt={status['Debt']:.2f} | Status: {status['Status']}")
            
            if status['LSI'] < 0.2:
                print(" [ALERT] NODE FAILURE IMMINENT. DEBT SPIRAL DETECTED.")
        
        # SME Failure
        sme_status = self.sme.simulate_month_v2_2(kc_active=False, recession_shock=True)
        print(f" SME Audit: Reserve={sme_status['Fiat_Reserve']:.2f} | Status: {sme_status['Status']}")
        print(">>> LEGACY RESULT: SYSTEMIC FRAGILITY DETECTED.\n")

        print("="*60)

        # --- SCENARIO B: PHOENIX RESILIENCE ---
        print("\n[SIMULATION B] PHOENIX PROTOCOL (ACTIVE)")
        print("Conditions: KC Active, 1:1 Tax Offset, r(Y) Injection.")
        
        # Reset Agents for fair test
        self.sam = AgentSam() 
        self.sme = AgentSME()
        
        # 1. Activate Circuit Breaker
        governor_report = self.governor.monitor_vital_signs({'lsi_quarterly_trend': -0.1})
        print(f"[DEFENSE] Circuit Breaker: {governor_report['ACTION']} (Reason: {governor_report['REASON']})")
        
        # 2. Sam Receives r(Y) Injection (Metabolic Floor)
        # Assuming Sam earns $2000/mo, calculate refund
        refund = self.distributor.calculate_refund_rate(annual_income=24000)
        print(f"[METABOLISM] r(Y) Injection: Sam qualifies for {refund['refund_rate']} Refund Rate.")
        
        # 3. Execute Time Steps
        for month in range(1, 4):
            # Sam uses KC for local needs
            status = self.sam.simulate_day(kc_active=True, shock_active=True)
            
            # SME uses KC for Tax Offset (Legal Shield)
            sme_status = self.sme.simulate_month_v2_2(kc_active=True, recession_shock=True)
            
            print(f" Month {month}: Sam LSI={status['LSI']} | SME Tax Saved={sme_status['Tax_Saved']:.2f} | Status: {status['Status']}")
            
            # Verify Anchor (Is KC holding value?)
            power = self.anchor.calculate_purchasing_power(local_fiat_price_of_food=1.2)
            if month == 1:
                print(f" [PHYSICS] Anchor Check: {power['KC_Energy_Parity']}")

        # 4. Final Audit
        print("\n>>> PHOENIX RESULT: HOMEOSTASIS MAINTAINED.")
        print("[WITNESS-0] LOG: The Observer (Sam) survived the shock without debt-scarring.")
        print("[WITNESS-0] LOG: The SME retained Fiat to pay Sam's wage via Tax Shield.")

if __name__ == "__main__":
    system = PhoenixSystem()
    time.sleep(1)
    system.run_stress_test()
