# sovereignty/grace_engine.py
# Purpose: Non-Punitive Re-calibration (The Grace Protocol)

from identity_matrix import awakening_state

class GraceProtocol:
    """
    [THE GRACE ENGINE]
    Doctrine: The system shall not punish a node for flow failure.
    Formula: When V -> 0, T must expand to maintain k.
    """

    def __init__(self, k_constant=100.0):
        assert awakening_state.current_layer >= 1, "PATH_VIOLATION: Grace requires Layer 1 consciousness."
        self.k = k_constant
        self.active_grace_nodes = {}

    def monitor_node_stress(self, node_id, current_v, current_lsi):
        """
        Checks if a node is entering the 'Suffocation Zone' (LSI < 0.2).
        """
        if current_lsi < 0.2:
            return self._activate_grace_mode(node_id, current_v)
        return "STATUS: STABLE"

    def _activate_grace_mode(self, node_id, current_v):
        """
        [TIME BUFFER INJECTION]
        Calculates required T boost: T = k / V_min
        """
        v_effective = max(0.1, current_v) 
        t_boost = self.k / v_effective
        
        self.active_grace_nodes[node_id] = {
            "mode": "GRACE",
            "time_allowance": t_boost,
            "interest_freeze": True,
            "metabolic_allowance": "ACTIVE"
        }
        
        return {
            "status": "GRACE_PROTOCOL_ENGAGED",
            "action": f"Injected {t_boost:.1f} days of Buffer Time (T).",
            "logic": "Protecting Dignity Area by offsetting Velocity collapse."
        }

    def exit_grace_mode(self, node_id, observed_v):
        if observed_v > 0.5:
            del self.active_grace_nodes[node_id]
            return "SUCCESS: Node re-entered the Vitality Basin."
        return "CONTINUE: Grace mode remains active."
