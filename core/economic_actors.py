# core/economic_actors.py
# Purpose: Defining the Biological (Sam) and Symbiotic (SME) Nodes
# Status: The Cast of the Phoenix Protocol

from identity_matrix import awakening_state

class AgentSam:
    """
    [ACTOR: THE BIOLOGICAL SINK]
    Subject: Sam (Life-Side Node)
    Constraint: Cannot survive if LSI (Life-Side Index) hits 0.
    """
    def __init__(self):
        assert awakening_state.current_layer >= 1, "Agent initialization requires Layer 1 awareness."
        self.savings_fiat = 500
        self.debt_legacy = 15000
        self.lsi = 0.3  # Suffocation Level
        self.daily_metabolism = 50

    def simulate_day(self, kc_active=False, shock_active=False):
        cost = self.daily_metabolism * (1.2 if shock_active else 1.0)
        income = 0 if shock_active else 60
        
        if not kc_active:
            # LEGACY LOGIC: Debt Spiral
            self.savings_fiat += (income - cost)
            self.debt_legacy *= 1.0002 # Debt Entropy increases
            if self.savings_fiat < 0:
                self.debt_legacy += abs(self.savings_fiat)
                self.savings_fiat = 0
            self.lsi = max(0, self.lsi - 0.01)
            return {"System": "Legacy", "LSI": round(self.lsi, 2), "Debt": round(self.debt_legacy, 2)}
        else:
            # KC LOGIC: The Shield
            kc_rebate = cost * 0.6 if shock_active else 0
            effective_cost = cost - kc_rebate
            self.savings_fiat += (income - effective_cost)
            self.lsi = 0.5 # Stabilized in the Basin
            return {"System": "Kiwicredit", "LSI": self.lsi, "Debt": self.debt_legacy}

class AgentSME:
    """
    [ACTOR: THE SYMBIOTIC SHIELD]
    Subject: The Local Bakery/Shop
    Doctrine: '1 KC = 1 Fiat Tax Credit'.
    """
    def __init__(self):
        assert awakening_state.current_layer >= 1
        self.fiat_reserve = 2000
        self.tax_rate = 0.15

    def simulate_month(self, kc_active=False, total_sales=1500):
        potential_tax = total_sales * self.tax_rate
        
        if not kc_active:
            # Legacy: Full tax paid in scarce fiat
            self.fiat_reserve -= potential_tax
            return {"System": "Legacy", "Fiat_Reserve": self.fiat_reserve, "Tax_Paid": potential_tax}
        else:
            # KC: 1:1 Tax Offset Protocol
            kc_revenue = total_sales * 0.4
            # KC revenue cancels Fiat tax liability
            actual_tax_fiat = max(0, potential_tax - kc_revenue)
            tax_saved = potential_tax - actual_tax_fiat
            
            # Retention of fiat liquidity
            self.fiat_reserve -= actual_tax_fiat
            return {"System": "KC", "Fiat_Reserve": self.fiat_reserve, "Tax_Saved": tax_saved}
