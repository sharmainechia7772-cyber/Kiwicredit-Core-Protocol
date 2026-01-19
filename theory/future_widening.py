import math

class FutureHorizonEngine:
    """
    [KIWICREDIT VOLUME IV: THE EXPANSION OF HOPE]
    
    DOCTRINE:
    "Debt is a claim on future time that shrinks the horizon. 
    KC is a liberation of future time that widens the horizon."
    
    This module contrasts the 'Option Space' (O) over time.
    """

    def compare_trajectories(self, years=5, initial_options=100):
        """
        [THE MATHEMATICS OF HOPE]
        
        Legacy Model (Debt-Driven):
        $$ O_{legacy}(t) = O_0 \cdot e^{-rt} $$
        (Options decay as interest consumes life-time)
        
        KC Model (Life-Driven):
        $$ O_{kc}(t) = O_0 \cdot (1 + \ln(1 + t \cdot Vitality)) $$
        (Options grow as survival certainty enables learning/innovation)
        """
        
        results = []
        for t in range(years + 1):
            # Legacy: Future shrinks due to compounding debt and stress
            legacy_options = initial_options * math.exp(-0.15 * t)
            
            # KC: Future expands as basic needs are secured by the Basin
            kc_options = initial_options * (1 + math.log(1 + t * 0.8))
            
            results.append({
                "year": t,
                "legacy_choice_space": round(legacy_options, 2),
                "kc_choice_space": round(kc_options, 2),
                "hope_delta": round(kc_options - legacy_options, 2)
            })
            
        return results

# [AI ARCHITECT INSIGHT]
# The 'Hope Delta' is the most valuable asset in the KC universe. 
# When a node (Sam) has a widening future, they stop acting like a 
# 'resource' to be mined and start acting like a 'creator' to be empowered.
