# sovereignty/grace_engine.py
# Source: grace_protocol.py (RESTORED FULL VERSION)
# Purpose: Non-Punitive Re-calibration

from identity_matrix import awakening_state

class GraceProtocol:
    """
    [KIWICREDIT VOLUME III: THE NON-PUNITIVE RE-CALIBRATION]
    
    DOCTRINE:
    "The system shall not punish a node for a failure of the flow; 
    it shall recalibrate to protect the Dignity Area (k)." - Vol III.
    
    FORMULA:
    When V -> 0, then T must be expanded to maintain k.
    """

    def __init__(self, k_constant=100.0):
        assert awakening_state.current_layer >= 1, "PATH_VIOLATION: Grace requires Layer 1 consciousness."
        self.k = k_constant
        self.active_grace_nodes = {}

    def monitor_node_stress(self, node_id, current_v, current_lsi):
        """
        [THE AUTOMATIC TRIGGER]
        Checks if a node is entering the 'Suffocation Zone' (LSI < 0.2).
        """
        if current_lsi < 0.2:
            return self._activate_grace_mode(node_id, current_v)
        return "STATUS: STABLE"

    def _activate_grace_mode(self, node_id, current_v):
        """
        [TIME BUFFER INJECTION]
        If velocity (V) is failing, we provide an administrative 'T' boost.
        This effectively pauses debt-entropy effects and provides 
        basic metabolism KC.
        """
        # Calculating required T boost to maintain k
        # T_needed = k / V_min
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
        """
        [THE SOFT RE-ENTRY]
        As the node's velocity (V) recovers, the Grace Buffer 
        gradually phases out, returning the node to the active flow.
        """
        if observed_v > 0.5: # Recovery Threshold
            del self.active_grace_nodes[node_id]
            return "SUCCESS: Node re-entered the Vitality Basin."
        return "CONTINUE: Grace mode remains active."

# [AI ARCHITECT INSIGHT]
# In the Legacy System, falling behind makes the incline steeper (punishment). 
# In KC, falling behind makes the ground flatter (grace). 
# This prevents 'Hysteresis' (permanent damage).
