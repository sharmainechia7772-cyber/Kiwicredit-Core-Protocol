class SystemStateManager:
    """
    [KIWICREDIT VOLUME III: CRISIS MANAGEMENT]
    
    MODULE: KCQE (KiwiCredit Quantitative Easing)
    
    SYSTEM DOCTRINE:
    In a recession, Legacy Systems inject liquidity into the TOP (Banks),
    hoping it leaks to the bottom. (It doesn't).
    
    Kiwicredit injects liquidity directly into the BOTTOM (Households),
    via the r(Y) Refund Rate.
    
    This module manages the State Transition from 'NORMAL' to 'CRISIS'.
    """

    def __init__(self):
        self.current_state = "NORMAL"
        
        # Default Parameters (Peacetime)
        self.params = {
            "minting_anchor_ratio": 0.10, # 10% of GST
            "r_max_refund": 0.60,         # Max 60% refund for poor
            "burn_rate": 1.0              # Standard decay
        }

    def detect_shock(self, gdp_growth, unemployment_trend):
        """
        [THE SENSOR]
        Detects exogenous shocks (e.g., Pandemic, Crash).
        """
        if gdp_growth < -0.02 or unemployment_trend > 0.05:
            return self.activate_crisis_protocol("RECESSION_DETECTED")
        else:
            return self.revert_to_normal()

    def activate_crisis_protocol(self, reason):
        """
        [WAR MODE: KCQE]
        Unlike Fiat QE, KCQE does not create Public Debt.
        It temporarily widens the channel to keep people alive.
        """
        self.current_state = "CRISIS_MODE"
        
        # BOOST PARAMETERS
        # 1. Mint more against real activity to stimulate flow
        self.params["minting_anchor_ratio"] = 0.20 
        
        # 2. Give more to the poor (Survival Support)
        self.params["r_max_refund"] = 0.90 
        
        # 3. Slow down decay to reduce anxiety
        self.params["burn_rate"] = 0.5 
        
        return {
            "STATUS": "CRISIS_ACTIVE",
            "REASON": reason,
            "ACTION": "Injecting direct debt-free liquidity to Life-Side.",
            "NOTE": "This state is TEMPORARY. Will revert when LSI stabilizes."
        }

    def revert_to_normal(self):
        """
        [THE EXIT STRATEGY]
        Prevents permanent inflation.
        """
        self.current_state = "NORMAL"
        self.params = {
            "minting_anchor_ratio": 0.10,
            "r_max_refund": 0.60,
            "burn_rate": 1.0
        }
        return "SYSTEM_NORMAL"
