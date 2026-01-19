class IgnitionCalculator:
    """
    [KIWICREDIT VOLUME IV: THE CRITICAL MASS PROTOCOL]
    
    DOCTRINE:
    "A single node is a freak; two nodes are a link; a hundred nodes are an ecosystem."
    """

    def calculate_flashpoint(self, neighborhood_population, sme_density):
        """
        Calculates the 'Flashpoint' ($F$) for local KC sustainability.
        $$ F = \frac{Total\_Metabolism}{SME\_Absorbtion\_Capacity} $$
        """
        required_nodes = neighborhood_population * 0.15 # 15% adoption rule
        synergy_strength = sme_density * 2.5
        
        is_self_sustaining = synergy_strength > 1.0
        
        return {
            "Required_SME_Count": math.ceil(required_nodes / 10),
            "Ecosystem_Status": "SELF_SUSTAINING" if is_self_sustaining else "INERT",
            "Growth_Strategy": "Recruit local bakery/pharmacy to unlock Alpha (1:1)."
        }
