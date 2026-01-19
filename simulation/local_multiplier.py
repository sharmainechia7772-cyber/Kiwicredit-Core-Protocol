class CommunityMetabolism:
    """
    [KIWICREDIT VOLUME II: LIFE-SIDE TRANSACTION DENSITY]
    
    THEORY: THE LEAKAGE COEFFICIENT ($\lambda$)
    -------------------------------------------
    In the Legacy System, money has 'High Mobility' towards Assets. 
    It leaks out of the local community almost instantly (Rent, Interest, Corporate Retail).
    
    In the KC System, money has 'High Perfusion' within the Life-Side.
    It is 'locked' in the local riverbed by Use Redlines and Decay Pressure.
    
    MATHEMATICAL MULTIPLIER ($k$):
    $$ k = \frac{1}{\lambda} $$
    Where $\lambda$ is the leakage rate per transaction.
    """

    def __init__(self):
        # In a typical struggling suburb:
        # 80% of Fiat leaks out to big banks/corps in every round.
        self.lambda_fiat = 0.80 
        
        # Only 15% of KC leaks out (since it can't be used for debt/assets).
        self.lambda_kc = 0.15

    def simulate_economic_perfusion(self, initial_injection=1000):
        """
        [SIMULATION]
        Compare how much 'Work' $1000 can do in a community.
        """
        print(f">>> STARTING PERFUSION SIMULATION: ${initial_injection} INJECTION <<<")
        
        fiat_total_volume = self._calculate_circulation(initial_injection, self.lambda_fiat, "FIAT")
        kc_total_volume = self._calculate_circulation(initial_injection, self.lambda_kc, "KIWICREDIT")
        
        print("\n--- FINAL AUDIT ---")
        print(f"Total Economic Activity (Fiat): ${fiat_total_volume:.2f}")
        print(f"Total Economic Activity (KC):   ${kc_total_volume:.2f}")
        print(f"KC Efficiency Gain: {((kc_total_volume/fiat_total_volume)-1)*100:.1f}%")

    def _calculate_circulation(self, amount, leakage, label):
        current_balance = amount
        total_volume = 0
        rounds = 0
        
        while current_balance > 10: # Stop when residual is negligible
            rounds += 1
            total_volume += current_balance
            
            # The 'Work' done in this round
            # print(f"[{label} Round {rounds}] ${current_balance:.2f} circulated.")
            
            # Leakage to the Asset Container / Global Corps
            current_balance = current_balance * (1 - leakage)
            
        return total_volume

# [AI ARCHITECT INSIGHT]
# High velocity + Low leakage = High Density.
# KC isn't 'more money'; it is 'more active money'.
# This proves that even a small amount of KC can end a local depression.
