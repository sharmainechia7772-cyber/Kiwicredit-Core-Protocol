class AntiCamouflageProtocol:
    """
    [KIWICREDIT VOLUME III: THE IMMUNE RESPONSE]
    
    DOCTRINE:
    "Complexity is the cloak of the parasite." - Vol III.
    
    This sub-module calculates a 'Friction Score' ($F$) based on the 
    structural complexity of the transaction.
    """

    def audit_complexity(self, transaction_metadata):
        """
        The more layers, offshore links, or derivatives involved, 
        the higher the friction.
        """
        complexity_score = 0
        
        if transaction_metadata.get('multi_layer_holding', False):
            complexity_score += 0.5  # Masking ownership
        if transaction_metadata.get('offshore_link', False):
            complexity_score += 0.4  # Capital flight risk
        if transaction_metadata.get('derivative_basis', False):
            complexity_score += 0.6  # Speculative nature
            
        return complexity_score

class EligibilityEngine:
    """
    [KIWICREDIT VOLUME III: ELIGIBILITY ENGINE V2]
    
    SYSTEM DOCTRINE:
    KC is a selectively permeable membrane. It allows the nutrients of the 
    Life-Side to flow, while blocking the toxicity of the Asset-Circuit.
    """

    CATEGORIES = {
        "ESSENTIAL": {"weight": 1.0, "max_kc": 1.0},
        "SERVICE":   {"weight": 0.8, "max_kc": 0.6},
        "LUXURY":    {"weight": 0.1, "max_kc": 0.05},
        "ASSET":     {"weight": 0.0, "max_kc": 0.0}
    }

    def __init__(self):
        self.immune_system = AntiCamouflageProtocol()

    def process_request(self, category, amount, metadata):
        """
        [THE DYNAMIC FILTER]
        Filters money based on category AND structural integrity.
        """
        # 1. Base classification
        config = self.CATEGORIES.get(category, {"weight": 0.0, "max_kc": 0.0})
        
        # 2. Complexity Friction (Anti-Camouflage)
        friction = self.immune_system.audit_complexity(metadata)
        
        # 3. Calculate Effective Utility
        # Even if it's 'ESSENTIAL', if it's complex, it loses eligibility.
        final_weight = max(0, config['weight'] - friction)
        allowed_kc = amount * final_weight
        
        if final_weight <= 0:
            return {
                "status": "REJECTED",
                "reason": "HIGH_COMPLEXITY_FRAUD_RISK",
                "diagnosis": "Asset-side parasite attempting to enter Life-Side riverbed."
            }

        return {
            "status": "APPROVED",
            "eligible_amount": allowed_kc,
            "friction_tax": amount * (1 - final_weight),
            "logic": f"Category: {category} | Friction Applied: {friction:.2f}"
        }

# [AI ARCHITECT INSIGHT]
# In the Legacy System, complexity is rewarded with tax loopholes. 
# In KC, complexity is punished with physical friction. 
# This makes the 'Life-Side' naturally simple and transparent.
