# sovereignty/circuit_breaker.py
# Purpose: Systemic Stop-Loss & Inflation Control

from identity_matrix import awakening_state

class SystemGovernor:
    """
    [SYSTEM GOVERNOR: THE ENTROPY BRAKE]
    Doctrine: Unlike fiat committees, KC relies on algorithmic triggers.
    If thermodynamic limits are breached, the system halts to prevent collapse.
    """

    def __init__(self):
        # Layer 2 required to manage high-energy fiscal states.
        assert awakening_state.current_layer >= 2, "FATAL: Layer 2 required to access System Governor controls."
        self.status = "GREEN" 
        self.minting_permission = True
        self.burn_rate_modifier = 1.0

    def monitor_vital_signs(self, market_data):
        """
        [THE WATCHDOG]
        Monitors Exchange Rate, Inflation, and Life-Side Index (LSI).
        """
        discount_rate = market_data.get('kc_fiat_discount', 0.0)
        inflation_rate = market_data.get('cpi_inflation', 0.0)
        lsi_trend = market_data.get('lsi_quarterly_trend', 0.0)

        return self._execute_judgment(discount_rate, inflation_rate, lsi_trend)

    def _execute_judgment(self, discount, inflation, lsi):
        # LEVEL 3: RED ALERT (Hyperinflation Risk)
        if inflation > 0.10 or discount > 0.20:
            self.status = "RED"
            self.minting_permission = False
            self.burn_rate_modifier = 2.0
            return {
                "ACTION": "EMERGENCY_STOP",
                "MINTING": "HALTED",
                "TAX_BURN": "ACCELERATED_200_PERCENT",
                "REASON": "Thermodynamic Overheating Detected."
            }

        # LEVEL 2: YELLOW ALERT (Stagnation Risk)
        elif lsi < 0:
            self.status = "YELLOW"
            self.minting_permission = True
            self.burn_rate_modifier = 0.8
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
