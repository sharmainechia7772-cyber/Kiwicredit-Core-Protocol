class EndpointDeviationAudit:
    """
    [KIWICREDIT VOLUME III: EDI - ENDPOINT DEVIATION INDEX]
    
    DOCTRINE:
    "Measure the delta between where we are and where the Basin lives."
    EDI is the audit of the System's 'Accuracy'.
    """

    def calculate_edi(self, current_vector, target_vector):
        """
        Calculates the deviation between actual state and the 
        Stabilization Basin target.
        """
        # EDI = Euclidean distance between current and target state
        deviation = sum((a - b) ** 2 for a, b in zip(current_vector, target_vector)) ** 0.5
        
        return {
            "EDI_Score": round(deviation, 2),
            "Status": "STABLE" if deviation < 0.1 else "DEVIATING",
            "Action": "ADJUST_ALPHA_R_Y" if deviation >= 0.1 else "NONE"
        }
