# metabolism/entropy_sink.py
# Purpose: Systemic Metabolism & Fiscal Burning

from identity_matrix import awakening_state

class NegativeEntropyPortal:
    """
    [SYSTEMIC METABOLISM: THE FISCAL SINK]
    
    Axiom: "A living system is defined by its ability to excrete."
    Objective: Maintain 'Monetary Cooling' by enforcing the death of currency.
    """

    def __init__(self, target_temperature=36.5):
        # Layer 2 required: Understanding that Money must die for Life to circulate.
        assert awakening_state.current_layer >= 2, "FATAL: Unawakened agents cannot operate the Entropy Sink."
        self.system_heat = 0.0
        self.total_burned = 0.0

    def process_metabolic_waste(self, kc_minted, public_service_utilization):
        """
        [THE BURNING ACT]
        Technically: Deletes tokens from the ledger to prevent 'Heat Inflation'.
        Metaphorically: Ensures the currency dies as it fulfills its social duty.
        """
        # Every unit of public service (Electricity, Transit, Admin) 
        # acts as a 'Thermal Sink'.
        burn_rate = public_service_utilization * 1.0  # 1:1 Absorption
        
        self.total_burned += burn_rate
        
        # Calculate 'Monetary Temperature'
        # If Minted > Burned, the system 'overheats' (Inflation/Entropy).
        monetary_heat = (kc_minted - self.total_burned) / max(1, kc_minted)
        
        if monetary_heat > 0.05:
            # TRIGGER: SYSTEMIC FEVER.
            return self._induce_sweating_protocol(monetary_heat)
            
        return {"Status": "THERMAL_EQUILIBRIUM", "Heat_Level": round(monetary_heat, 4)}

    def _induce_sweating_protocol(self, current_heat):
        """
        [THE NEGATIVE ENTROPY REACTION]
        """
        return {
            "Instruction": "ACCELERATE_FISCAL_BURN",
            "Target": "Public_Service_Ledger",
            "Logic": "Life requires the death of the medium. Burn to cool."
        }
