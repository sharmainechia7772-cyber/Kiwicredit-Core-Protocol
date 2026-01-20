import math

class ProgressiveDistributor:
    """
    [KIWICREDIT VOLUME III: DISTRIBUTION LOGIC]
    
    THE r(Y) CURVE:
    ---------------
    Standard Universal Basic Income (UBI) gives a flat amount ($C$) to everyone.
    Kiwicredit uses a dynamic refund function $r(Y)$ based on income $Y$.
    
    FORMULA:
    $$ r(Y) = r_{max} \cdot \frac{1}{1 + \beta \cdot (Y / Y_{median})} $$
    
    Where:
    - $r_{max}$: Maximum refund rate for zero income (e.g., 60%).
    - $\beta$: Steepness coefficient (Controls how fast support drops off).
    - $Y_{median}$: The economy's median wage anchor.
    
    OBJECTIVE:
    Maximize LSI (Living Space) for the bottom 40% without breaking the fiscal budget.
    """

    def __init__(self, r_max=0.60, beta=1.5, median_wage=50000):
        self.r_max = r_max      # 60% refund at the bottom
        self.beta = beta        # Steepness curve
        self.median_wage = median_wage

    def calculate_refund_rate(self, annual_income):
        """
        [PRECISION INJECTION]
        Calculates exactly how much KC a node receives based on their fiscal position.
        """
        
        # Normalize income against the median
        income_ratio = annual_income / self.median_wage
        
        # The Logistic Decay Function
        # As income rises, the r(Y) rate smoothly descends, but never hits zero (Universality).
        r_y = self.r_max / (1 + (self.beta * income_ratio))
        
        return {
            "income": annual_income,
            "income_ratio": f"{income_ratio:.2f}x Median",
            "refund_rate": f"{r_y:.1%}",
            "status": "OPTIMAL_ALLOCATION"
        }

    def simulate_impact(self, gst_spend):
        """
        Shows the difference between Rich and Poor nodes spending the same amount.
        """
        # Node A: Struggling Worker (Income = 0.5x Median)
        rate_A = self.calculate_refund_rate(self.median_wage * 0.5)['refund_rate']
        
        # Node B: Wealthy CEO (Income = 5.0x Median)
        rate_B = self.calculate_refund_rate(self.median_wage * 5.0)['refund_rate']
        
        return f"For ${gst_spend} spend: Poor gets {rate_A} back. Rich gets {rate_B} back."
