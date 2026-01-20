class HydraulicValve:
    """
    [KIWICREDIT VOLUME III: THE RED LINES]
    
    SYSTEM DOCTRINE:
    The 'Riverbed Shift' (Vol I) occurs when liquidity leaks from the Wage-Consumption Loop
    into the Credit-Asset Loop.
    
    MATHEMATICAL GOVERNANCE:
    ------------------------
    Let $P(s)$ be the Permeability Function for a given economic sector $s$.
    
    $$ P(s) = \begin{cases} 0 & \text{if } s \in \{FIRE, RealEstate, Speculation\} \\ 1 & \text{if } s \in \{Production, Services, Wages\} \end{cases} $$
    
    The Transfer Function $T(x)$ is therefore non-linear:
    $$ T(x) = Amount \cdot P(TargetSector) $$
    
    This acts as a 'Maxwell's Demon', ensuring the entropy of the system does not increase
    through asset bubbles.
    """

    # The Blacklist derived from Vol III, Chapter 7
    # SIC (Standard Industrial Classification) Codes representing Asset Speculation
    ASSET_CIRCUIT_BLACKLIST = [
        "L6810", # Real Estate Buying/Selling
        "K6419", # Financial Intermediation (Banking hoarding)
        "K6499", # Derivatives & Crypto Speculation
    ]

    def inspect_flow(self, sender_type, receiver_sector_code, amount, velocity_history):
        """
        [THE ENTROPY FILTER]
        Executes the Permeability Function.
        """
        
        # 1. The Asset Firewall (P(s) = 0)
        if receiver_sector_code in self.ASSET_CIRCUIT_BLACKLIST:
            return {
                "allowed": False,
                "reason": "VIOLATION: RED_LINE_BREACH. KC cannot be used to inflate asset prices. ($P(s)=0$)",
                "action": "BLOCK_TRANSACTION"
            }

        # 2. The Hoarding Penalty (Maxwell's Demon Check)
        # If a node accepts money but refuses to move it, it increases System Entropy.
        # We apply an 'Accelerated Decay' factor ($\lambda$).
        
        if self._is_stagnant(velocity_history):
            # Formula: Decay_eff = Decay_base * (1 + lambda * Stagnation_Time)
            return {
                "allowed": True,
                "warning": "HIGH_ENTROPY_RISK: Node velocity -> 0. Accelerated Decay activated.",
                "decay_multiplier": 2.5 
            }

        return {
            "allowed": True,
            "reason": "APPROVED: Flow remains within Life-Side Density."
        }

    def _is_stagnant(self, history):
        # Checks if velocity is below the critical 'Life-Support' threshold
        return history['avg_turnover_days'] > 90
