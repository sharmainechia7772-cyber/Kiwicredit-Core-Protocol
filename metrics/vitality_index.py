class ResilienceAuditor:
    """
    [KIWICREDIT VOLUME IV: THE ANTI-FRAGILITY PROTOCOL]
    
    DOCTRINE:
    "A resilient system doesn't resist shock; it absorbs and converts it." - Vol IV.
    
    This sub-module simulates an 'Exogenous Shock' (e.g., Energy Price Hike) 
    and measures the recovery speed of the Life-Side.
    """

    def simulate_shock_recovery(self, shock_magnitude, local_multiplier):
        """
        Calculates the Resilience Score ($R$).
        High local multiplier (KC) leads to faster recovery.
        """
        # Time to Recovery (T_r) is inversely proportional to local circulation
        recovery_time = shock_magnitude / (1 + local_multiplier)
        
        # Resilience Score R = 1 / T_r
        resilience_score = 1 / max(0.1, recovery_time)
        
        return {
            "shock_absorbed": shock_magnitude,
            "recovery_speed": round(resilience_score, 2),
            "status": "RESILIENT" if resilience_score > 0.5 else "FRAGILE"
        }

class VitalityDetector:
    """
    [KIWICREDIT VOLUME IV: VITALITY INDEX V2]
    
    SYSTEM DOCTRINE:
    We distinguish between 'Dead Stability' (Equilibrium) and 'Living Vitality' (Resilience).
    """

    def __init__(self):
        self.resilience_engine = ResilienceAuditor()

    def audit_community_vitality(self, velocity, autonomy, local_kc_multiplier):
        """
        [THE PULSE OF THE SYSTEM]
        Calculates the Vitality Score (V) based on flow and self-healing capacity.
        """
        # 1. Base Vitality: Flow times Autonomy
        # $$ V_{base} = Velocity \cdot Autonomy $$
        base_vitality = velocity * autonomy
        
        # 2. Resilience Check: How does it handle a 20% cost-of-living shock?
        resilience_report = self.resilience_engine.simulate_shock_recovery(0.2, local_kc_multiplier)
        
        # 3. Comprehensive Analysis
        if base_vitality < 0.2:
            status = "STAGNANT (Suffocation Risk)"
        elif resilience_report['recovery_speed'] < 0.3:
            status = "FRAGILE_PROSPERITY (Collapse Risk)"
        else:
            status = "VIBRANT_AND_ROBUST"

        return {
            "vitality_score": round(base_vitality, 2),
            "resilience_speed": resilience_report['recovery_speed'],
            "system_status": status,
            "diagnosis": f"Local Multiplier {local_kc_multiplier} provides the necessary buffer."
        }

# [AI ARCHITECT INSIGHT]
# In the Legacy System, shocks lead to 'Hysteresis' (permanent damage). 
# In KC, the high local velocity acts as an 'Economic Immune System', 
# allowing the community to re-equilibrate without waiting for central intervention.
