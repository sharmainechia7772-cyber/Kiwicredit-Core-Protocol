class EntropySink:
    """
    [KIWICREDIT VOLUME III: RECOVERY & CLOSURE]
    
    SYSTEM DOCTRINE:
    Infinite accumulation violates thermodynamics.
    Money must eventually 'die' (return to the State) to prevent system heat death (Inflation).
    
    THE ALPHA PROTOCOL ($\alpha$):
    -----------------------------
    Let $T_{nominal}$ be the statutory corporate tax rate (e.g., 28%).
    Let $R_{KC}$ be the ratio of revenue accepted in Kiwicredit.
    Let $\alpha$ be the Incentive Coefficient (e.g., 0.5).
    
    The Effective Tax Rate $T_{eff}$ is calculated as:
    
    $$ T_{eff} = T_{nominal} \cdot (1 - \alpha \cdot R_{KC}) $$
    
    This creates a Game Theoretic Dominant Strategy:
    "It is always rational for a firm to accept KC, as long as the decay cost < tax savings."
    """

    def __init__(self, nominal_tax_rate=0.28, alpha_coefficient=0.5):
        self.nominal_tax = nominal_tax_rate # The standard fiat tax rate
        self.alpha = alpha_coefficient      # The power of the KC discount

    def calculate_tax_obligation(self, total_profit, kc_revenue_ratio):
        """
        [THE RATIONALITY ENGINE]
        Calculates how much tax is saved by participating in the KC network.
        """
        
        # Apply the Alpha Formula
        effective_rate = self.nominal_tax * (1 - (self.alpha * kc_revenue_ratio))
        
        # Safety Clip: Government needs some minimum cash flow (e.g., floor at 10%)
        effective_rate = max(effective_rate, 0.10) 
        
        tax_due = total_profit * effective_rate
        savings = (self.nominal_tax - effective_rate) * total_profit
        
        return {
            "nominal_rate": f"{self.nominal_tax:.2%}",
            "effective_rate": f"{effective_rate:.2%}",
            "tax_savings": savings,
            "strategy_advice": "OPTIMAL: ACCEPT_KC" if savings > 0 else "NEUTRAL"
        }

    def burn_tokens(self, kc_amount):
        """
        [THE CLOSURE]
        KC used for tax is NOT re-spent by the government.
        It is ANNIHILATED to control inflation.
        """
        # Thermodynamic End-State
        print(f"[SYSTEM LOG] BURNING {kc_amount} KC. Returning to the Void.")
        return "ENTROPY_REDUCED"
