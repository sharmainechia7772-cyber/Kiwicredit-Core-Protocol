class WelfareMetrics:
    """
    [KIWICREDIT VOLUME II: THE NEW COORDINATE SYSTEM]
    
    SYSTEM DOCTRINE:
    Standard Macroeconomics optimizes for 'Aggregate Growth' (GDP).
    This ignores the 'Riverbed Shift' where growth flows only to assets.
    
    Kiwicredit optimizes for 'Thermodynamic Survival' (LSI).
    
    DEFINITIONS:
    ------------
    Let $W_{median}$ be the Median Wage.
    Let $C_{fixed}$ be Fixed Survival Costs (Rent, Power, Food, Transport).
    Let $\sigma_{risk}$ be the Volatility Buffer (Safety Net).
    
    The Living Space Index (LSI) is defined as:
    
    $$ LSI = \frac{W_{median} - C_{fixed}}{C_{housing}} $$
    
    Interpretation:
    - LSI < 0: Debt Serfdom (Entropy > Energy input).
    - LSI = 0: Subsistence (Zero Freedom).
    - LSI > 1: Dignity (Positive Freedom).
    """
    
    def calculate_LSI(self, median_wage, housing_cost, essential_basket):
        """
        [THE TARGET FUNCTION]
        This is what the System Architect must maximize.
        """
        fixed_costs = housing_cost + essential_basket
        disposable_energy = median_wage - fixed_costs 
        
        # Avoid division by zero
        if housing_cost == 0: return float('inf')
        
        # The Core Metric: How many times can you pay for shelter with your surplus?
        lsi_score = disposable_energy / housing_cost
        
        return {
            "LSI_Score": round(lsi_score, 2),
            "Status": self._interpret_lsi(lsi_score)
        }

    def _interpret_lsi(self, score):
        if score < 0:
            return "CRITICAL FAILURE: NEGATIVE LIVING SPACE. System is extracting life."
        elif score < 0.5:
            return "WARNING: FRAGILE. One shock will cause collapse."
        elif score >= 1.0:
            return "OPTIMAL: High Dignity State."
        return "STRESSED"

    def calculate_EDI(self, lsi, certainty_factor):
        """
        [EFFECTIVE DIGNITY INDEX]
        Dignity is not just having space; it is knowing that space won't disappear tomorrow.
        EDI = LSI * Certainty (where Certainty is inversely related to Anxiety).
        """
        return lsi * certainty_factor
