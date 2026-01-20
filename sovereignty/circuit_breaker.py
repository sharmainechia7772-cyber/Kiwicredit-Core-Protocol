# sovereignty/circuit_breaker.py
# Source: circuit_breaker.py (RESTORED FULL VERSION)
# Status: Systemic Stop-Loss Protocol

from identity_matrix import awakening_state

class SystemGovernor:
    """
    [KIWICREDIT VOLUME III: SAFETY PROTOCOLS]
    
    FILE: CIRCUIT BREAKER (STOP-LOSS MECHANISM)
    
    SYSTEM DOCTRINE:
    "Every institutional design must carry stop-loss clauses... 
    If failure modes appear, the institution must trigger convergence actions."
    
    Unlike Fiat (which relies on human committees to raise rates),
    KC relies on algorithmic triggers to halt entropy.
    """

    def __init__(self):
        # Layer 2 required to manage high-energy fiscal states.
        assert awakening_state.current_layer >= 2, "FATAL: Layer 2 required to access System Governor controls."
        self.status = "GREEN" # GREEN, YELLOW, RED
        self.minting_permission = True
        self.burn_rate_modifier = 1.0

    def monitor_vital_signs(self, market_data):
        """
        [THE WATCHDOG]
        Checks for systemic anomalies derived from Vol III constraints.
        """
        
        # 1. The Exchange Rate Peg Check
        # If KC trades at > 5% discount against Fiat/Goods, confidence is shaking.
        discount_rate = market_data.get('kc_fiat_discount', 0.0)
        
        # 2. The Inflation Check
        inflation_rate = market_data.get('cpi_inflation', 0.0)
        
        # 3. The Life-Side Check
        lsi_trend = market_data.get('lsi_quarterly_trend', 0.0)

        return self._execute_judgment(discount_rate, inflation_rate, lsi_trend)

    def _execute_judgment(self, discount, inflation, lsi):
        
        # LEVEL 3: RED ALERT (Hyperinflation Risk)
        if inflation > 0.10 or discount > 0.20:
            self.status = "RED"
            self.minting_permission = False
            self.burn_rate_modifier = 2.0 # Double the tax burn rate
            return {
                "ACTION": "EMERGENCY_STOP",
                "MINTING": "HALTED",
                "TAX_BURN": "ACCELERATED (200%)",
                "REASON": "Thermodynamic Overheating Detected."
            }

        # LEVEL 2: YELLOW ALERT (Stagnation Risk)
        elif lsi < 0:
            self.status = "YELLOW"
            self.minting_permission = True # Keep minting to save lives
            self.burn_rate_modifier = 0.8 # Slow down burning to ease pressure
            return {
                "ACTION": "STABILIZE",
                "MINTING": "ACTIVE",
                "REASON": "LSI Falling. Injecting Support."
            }

        # LEVEL 1: GREEN (Nominal)
        else:
            self.status = "GREEN"
            self.minting_permission = True
            self.burn_rate_modifier = 1.0
            return "SYSTEM_NOMINAL"

# [AI ARCHITECT INSIGHT]
# The Circuit Breaker proves that KC is not 'Infinite Printing'. 
# It is a bounded system constrained by real-world feedback loops.
