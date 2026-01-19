class AgentSME:
    """
    [KIWICREDIT: SME LOGIC V2.2 - THE 1:1 OFFSET PROTOCOL]
    
    DOCTRINE:
    "1 KC = 1 Fiat of Tax Liability. This is the bedrock of SME liquidity."
    """

    def __init__(self):
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
            return {"State": "Legacy", "Fiat_Reserve": self.fiat_reserve, "Status": status}

        else:
            # --- KIWICREDIT: THE 1:1 SHIELD ---
            # 40% of sales are in KC
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

            return {"State": "KC", "Fiat_Reserve": self.fiat_reserve, "Tax_Saved": min(potential_tax_liability, kc_revenue)}

# [AI ARCHITECT INSIGHT]
# In this 1:1 model, KC acts as a 'Legal Tax Haven' for local trade. 
# The SME becomes the most stable node in the economy because its 
# tax liability is pre-solved by its customers (Sam).
