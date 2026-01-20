# core/economic_actors.py
# Source: agent_sam.py + agent_sme.py (MERGED FULL VERSION)
# Status: The Complete Cast of the Phoenix Protocol

import math
from identity_matrix import awakening_state

# ==============================================================================
# PART 1: AGENT SAM (The Biological Sink)
# ==============================================================================

class AgentSam:
    """
    [KIWICREDIT: THE HUMAN SIMULATION]
    
    SUBJECT: Sam
    ROLE: Life-Side Node (Service Sector)
    STATUS: Living on the Edge.
    """

    def __init__(self):
        # Layer 1 Safety Check
        assert awakening_state.current_layer >= 1, "Agent initialization requires Layer 1 awareness."
        
        # Initial State (Fragile)
        self.savings_fiat = 500
        self.debt_legacy = 15000
        self.lsi = 0.3 # Survival Space Index (Suffocation Level)
        self.daily_metabolism = 50
        self.dignity_k = 100 # Required Area (V * T)

    def simulate_day(self, kc_active=False, shock_active=False):
        # 1. External Shock Logic (Rent Hike + Job Loss)
        cost = self.daily_metabolism * (1.2 if shock_active else 1.0)
        income = 0 if shock_active else 60
        
        # 2. The Great Divergence
        if not kc_active:
            # --- LEGACY SYSTEM LOGIC ---
            self.savings_fiat += (income - cost)
            # Interest never sleeps (Debt Entropy)
            self.debt_legacy *= 1.0002 # ~7% APR
            
            if self.savings_fiat < 0:
                # Forced to borrow more (The Spiral)
                self.debt_legacy += abs(self.savings_fiat)
                self.savings_fiat = 0
            
            # LSI decays as debt pressure grows
            self.lsi = max(0, self.lsi - 0.01)
            
            return {
                "System": "Legacy", 
                "LSI": round(self.lsi, 2), 
                "Debt": round(self.debt_legacy, 2),
                "Status": "SUFFOCATING" if self.lsi < 0.2 else "SURVIVING"
            }
        
        else:
            # --- KIWICREDIT SYSTEM LOGIC ---
            # Dignity Floor: Cost is subsidized by KC rebates
            # Grace Protocol kick in because LSI < 0.2
            kc_rebate = cost * 0.6 if shock_active else 0
            
            # Grace Protocol: Interest Freezes during Shock
            interest_rate = 0 if shock_active else 1.0002
            self.debt_legacy *= interest_rate
            
            # Local Multiplier: Local store accepts KC due to Alpha (0.3)
            effective_cost = cost - kc_rebate
            self.savings_fiat += (income - effective_cost)
            
            # Dignity Area (V * T) is maintained
            # Even if income is 0, the Buffer (T) is extended by KC minting
            self.lsi = 0.5 # Stabilized in the Basin
            return {
                "System": "Kiwicredit", 
                "LSI": self.lsi, 
                "Debt": self.debt_legacy,
                "Status": "STABILIZED_BY_PROTOCOL"
            }

# ==============================================================================
# PART 2: AGENT SME (The Symbiotic Shield)
# ==============================================================================

class AgentSME:
    """
    [KIWICREDIT: SME LOGIC V2.2 - THE 1:1 OFFSET PROTOCOL]
    
    DOCTRINE:
    "1 KC = 1 Fiat of Tax Liability. This is the bedrock of SME liquidity."
    """

    def __init__(self):
        assert awakening_state.current_layer >= 1
        self.fiat_reserve = 2000
        self.debt_legacy = 50000
        self.monthly_fiat_wage_bill = 800 # Must be paid in FIAT (To Sam)
        self.monthly_rent_fiat = 500
        self.tax_rate = 0.15 # 15% Legacy Tax Rate

    def simulate_month_v2_2(self, kc_active=False, recession_shock=False):
        # 1. Revenue
        total_sales = 1500 if not recession_shock else 1000
        # Calculate base tax liability in fiat
        potential_tax_liability = total_sales * self.tax_rate
        
        if not kc_active:
            # --- LEGACY: THE DRAIN ---
            raw_material_fiat = 500 * (1.2 if recession_shock else 1.0)
            # Full tax must be paid in fiat
            net_flow = total_sales - raw_material_fiat - self.monthly_fiat_wage_bill - self.monthly_rent_fiat - potential_tax_liability
            self.fiat_reserve += net_flow
            
            status = "CRITICAL" if self.fiat_reserve < 800 else "SURVIVING"
            return {"State": "Legacy", "Fiat_Reserve": self.fiat_reserve, "Tax_Paid": potential_tax_liability, "Status": status}
            
        else:
            # --- KC: THE SHIELD ---
            # 40% of sales in KC (Community usage)
            kc_revenue = total_sales * 0.4
            fiat_revenue = total_sales * 0.6
            
            # THE 1:1 OFFSET:
            # The KC revenue directly cancels out the fiat tax liability 1-for-1.
            # If KC revenue > Tax liability, the tax becomes ZERO.
            actual_tax_to_pay_fiat = max(0, potential_tax_liability - kc_revenue)
            
            # Procurement: 20% cost offset by KC
            raw_material_total = 500 * (1.2 if recession_shock else 1.0)
            raw_material_fiat = raw_material_total * 0.8
            
            # THE FIAT RETENTION CALCULATION
            # The bakery 'keeps' the fiat that would have gone to tax.
            net_fiat_flow = fiat_revenue - raw_material_fiat - self.monthly_rent_fiat - actual_tax_to_pay_fiat
            
            self.fiat_reserve += net_fiat_flow
            
            # Sam's Wage is the Priority
            if self.fiat_reserve >= self.monthly_fiat_wage_bill:
                self.fiat_reserve -= self.monthly_fiat_wage_bill
                status = "VIBRANT (Sam's Wage Secured by Tax Shield)"
            else:
                status = "DISTRESSED"

            return {
                "State": "KC", 
                "Fiat_Reserve": self.fiat_reserve, 
                "Tax_Saved": min(potential_tax_liability, kc_revenue),
                "Status": status
            }

# [AI ARCHITECT INSIGHT]
# By allowing the SME to pay taxes with 'Community Credits' (KC), 
# we effectively stop the leakage of Fiat out of the community.
# The Fiat stays local to pay Sam's wage. The Tax is settled by KC.
# This creates a 'Local Liquidity Loop' that resists global recession.
