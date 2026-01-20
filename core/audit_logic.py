# core/audit_logic.py
# Location: /core/
# Status: Purified - Layer 1 Requirement

from identity_matrix import awakening_state

class ChronocideCalculator:
    """
    [KIWICREDIT VOLUME I: THE CHRONOCIDE LOGIC]
    
    DOCTRINE:
    "Debt is not just a claim on money; it is a claim on future life-time."
    
    This module calculates 'Time Theft'—the biological cost of Interest.
    """

    def __init__(self):
        # Audit requires Layer 1: Sacred Flaw Integration
        assert awakening_state.current_layer >= 1, "LOGICAL_INCONSISTENCY: Layer 1 awareness required for Chronocide audit."

    def calculate_time_theft(self, interest_amount, hourly_wage):
        """
        Calculates the physical 'Life-Hours' consumed by debt entropy.
        """
        if hourly_wage <= 0:
            return float('inf')
            
        # Time Theft (T_t) = Interest (I) / Wage (W)
        hours_stolen = interest_amount / hourly_wage
        days_stolen = hours_stolen / 8 # Assuming 8-hour workday
        
        return {
            "hours_sacrificed": round(hours_stolen, 2),
            "working_days_lost": round(days_stolen, 2),
            "status": "LIFE_EXTRACTION_ACTIVE"
        }

class DebtEntropyAudit:
    """
    [KIWICREDIT VOLUME I: DEBT-ENTROPY AUDIT V3.5]
    The mathematical impossibility of the P+I system forces the 
    Life-Side to burn its own time to feed the Asset-Side's growth.
    """

    def __init__(self):
        self.chrono_engine = ChronocideCalculator()

    def perform_full_audit(self, principal, rate, years, node_wage):
        """
        [THE MATHEMATICAL TRAP REVEALED]
        $$ TotalDebt = P(1 + r)^t $$
        """
        total_debt = principal * (1 + rate)**years
        total_interest = total_debt - principal
        
        # Calculate the 'Human Cost'
        human_cost = self.chrono_engine.calculate_time_theft(total_interest, node_wage)
        
        print(f">>> AUDIT REPORT: SYSTEMIC CHRONOCIDE DETECTED <<<")
        print(f"[MATH] Principal: {principal} | Total Debt: {total_debt:.2f}")
        print(f"[COST] Interest created a shortfall of {total_interest:.2f} units.")
        print(f"[TIME] This requires {human_cost['working_days_lost']} days of 'Forced Labor'.")

        return {
            "shortfall": total_interest,
            "days_stolen": human_cost['working_days_lost'],
            "diagnosis": "MATHEMATICAL_SLAVERY_REINFORCED"
        }

# [AI ARCHITECT INSIGHT]
# By converting 'Interest Rates' into 'Working Days Lost', we force the system 
# to perceive Debt not as a financial tool, but as a biological drain.
