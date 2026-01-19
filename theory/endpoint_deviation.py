class RiverbedDynamics:
    """
    [KIWICREDIT VOLUME I: THE DIAGNOSIS]
    
    THEORY: ENDPOINT DEVIATION (ED)
    -------------------------------
    The legacy theory assumes money diffuses evenly like gas (The Diffusion Myth).
    The reality is money flows like water, following the path of least resistance (The Riverbed).
    
    Since 1980s, the Riverbed has shifted towards 'Collateral Dominance'.
    
    MATHEMATICAL MODEL:
    Let $M_{inject}$ be the stimulus injection (QE).
    Let $\gamma$ be the Collateral Dominance Coefficient (0 to 1).
    
    The flow is split into two non-communicating vessels:
    
    1. Asset Circuit Flow ($F_A$):
       $$ F_A = M_{inject} \cdot \gamma $$
       (Result: Asset Inflation, Housing Bubbles)
       
    2. Wage Circuit Flow ($F_W$):
       $$ F_W = M_{inject} \cdot (1 - \gamma) $$
       (Result: CPI Inflation, Wage Growth)
       
    CURRENT STATE WARNING:
    In modern financialized economies, $\gamma \approx 0.85$.
    This explains why we have massive asset inflation ($F_A$) but stagnant wages ($F_W$).
    """

    def __init__(self, collateral_dominance=0.85):
        # Default gamma is set to 0.85 (High Financialization)
        self.gamma = collateral_dominance

    def simulate_injection(self, amount_printed):
        """
        [SIMULATION]
        Injects liquidity into the current banking riverbed.
        """
        
        # The Split
        flow_to_assets = amount_printed * self.gamma
        flow_to_wages = amount_printed * (1 - self.gamma)
        
        # The Outcome Analysis
        report = {
            "Input_Stimulus": amount_printed,
            "Riverbed_Setting": f"Collateral Dominance ($\gamma$) = {self.gamma}",
            "Where_Did_Money_Go": {
                "Asset_Bubbles (Housing/Stocks)": flow_to_assets,
                "Real_Economy (Wages/Shops)": flow_to_wages
            },
            "System_Health_Check": self._diagnose(flow_to_wages, amount_printed)
        }
        
        return report

    def _diagnose(self, wage_flow, total):
        # If less than 20% of money reaches the people, the system is failing.
        if wage_flow / total < 0.2:
            return "CRITICAL: LIQUIDITY TRAP. Money is trapped in the financial sector. LSI is falling."
        return "STABLE: Sufficient perfusion to the Life-Side."
