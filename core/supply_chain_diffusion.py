class SupplyChainHydraulics:
    """
    [KIWICREDIT VOLUME III: B2B DEEPENING]
    
    MODULE: UPSTREAM DIFFUSION PROTOCOL
    
    THE CHALLENGE:
    Retailers (Downstream) have high margins and can accept lots of KC.
    Wholesalers/Manufacturers (Upstream) have thin margins and demand Fiat cash flow.
    
    THE SOLUTION: MARGIN-MATCHED ACCEPTANCE
    KC flows upstream via a 'Mixed Payment' ratio derived from the receiver's Operating Margin.
    
    FORMULA:
    $$ MaxAcceptance_{KC} \approx OperatingMargin + \frac{TaxLiability}{Revenue} $$
    
    This ensures no business ever receives more KC than it can burn (via Tax) or absorb (via Profit).
    """

    def negotiate_payment_terms(self, supplier_profile, invoice_amount):
        """
        [THE B2B HANDSHAKE]
        Determines how much of an invoice can be paid in KC without hurting the Supplier.
        """
        
        # 1. Analyze Supplier's Capacity
        margin = supplier_profile['operating_margin']  # e.g., 0.05 for a wholesaler
        tax_burden = supplier_profile['tax_ratio']     # e.g., 0.20 of profit
        
        # 2. Calculate Safe Exposure Limit
        # A supplier can safely accept KC equal to their profit margin (to spend/save)
        # PLUS the amount they need to pay taxes (Fiscal Sink).
        safe_kc_ratio = margin + (margin * tax_burden * 2.0) # *2.0 is an incentive multiplier
        
        # Cap at 100% (obviously)
        safe_kc_ratio = min(safe_kc_ratio, 1.0)
        
        # 3. The Deal Structure
        kc_portion = invoice_amount * safe_kc_ratio
        fiat_portion = invoice_amount * (1 - safe_kc_ratio)
        
        return {
            "role": supplier_profile['role'],
            "invoice_total": invoice_amount,
            "payment_structure": {
                "KC_Amount": kc_portion,
                "Fiat_Amount": fiat_portion
            },
            "logic": f"Supplier has thin margin ({margin:.1%}). Only accepts {safe_kc_ratio:.1%} in KC to remain safe."
        }

    def simulate_chain_reaction(self):
        """
        [VISUALIZING THE FLOW]
        Consumer -> Retailer -> Wholesaler -> Manufacturer
        """
        print(">>> SIMULATING SUPPLY CHAIN HYDRAULICS <<<")
        
        # Step 1: Consumer buys from Retailer ($100)
        # Retailer has 40% margin, takes 40% KC.
        retailer_deal = self.negotiate_payment_terms(
            {'role': 'Retailer', 'operating_margin': 0.40, 'tax_ratio': 0.28}, 
            100
        )
        print(f"[STEP 1] Consumer pays Retailer: {retailer_deal['payment_structure']}")
        
        # Step 2: Retailer restocks from Wholesaler ($60 Cost of Goods)
        # Wholesaler has 10% margin, takes ~15% KC.
        wholesaler_deal = self.negotiate_payment_terms(
            {'role': 'Wholesaler', 'operating_margin': 0.10, 'tax_ratio': 0.28}, 
            60
        )
        print(f"[STEP 2] Retailer pays Wholesaler: {wholesaler_deal['payment_structure']}")
        
        # Step 3: Hydraulic Pressure Analysis
        # The Retailer took in 40 KC, but could only pass 9 KC (15% of 60) upstream.
        # The remaining 31 KC acts as 'Local Multiplier' - Retailer must spend it locally!
        print(f"[RESULT] {wholesaler_deal['payment_structure']['KC_Amount']} KC moved Upstream.")
        print(f"[RESULT] Remainder trapped at Retailer, forcing Local Investment.")
