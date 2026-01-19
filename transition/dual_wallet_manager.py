class DualWalletManager:
    """
    [KIWICREDIT VOLUME III: THE SURVIVAL ARBITRAGE]
    
    DOCTRINE:
    "Aggressively spend KC on the inside; defensively hold Fiat for the outside."
    """

    def suggest_payment_strategy(self, sam_fiat, sam_kc, bill_amount, bill_category):
        """
        [THE STRATEGY ENGINE]
        Decides which currency to use based on the 'Fiat Retention' law.
        """
        if bill_category in ["ESSENTIAL", "COMMUNITY", "FOOD"]:
            # Rule: Always try to use KC for local life-side needs.
            return {
                "Preferred_Currency": "KC",
                "Fiat_Saved": bill_amount,
                "Advice": "Save your fiat for legacy debt (Principal/Interest)."
            }
        
        if bill_category == "LEGACY_DEBT":
            # Rule: KC cannot pay legacy debt (The Redline).
            return {
                "Preferred_Currency": "FIAT",
                "Action": "Apply saved fiat from previous life-side transactions."
            }
            
        return {"Preferred_Currency": "HYBRID"}
