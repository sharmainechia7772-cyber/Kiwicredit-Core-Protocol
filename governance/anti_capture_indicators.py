import re

class SemanticFirewall:
    """
    [KIWICREDIT VOLUME II: SEMANTIC DEFENSE]
    
    DOCTRINE:
    "The old paradigm's strongest weapon is its ability to colonize vision 
    via language." - Vol II.
    
    This sub-module acts as a 'Paradigm Translator', stripping legacy 
    terminology of its neutral camouflage.
    """
    
    DICTIONARY = {
        r"natural rate of unemployment": "SYSTEMIC_NODE_SACRIFICE_THRESHOLD",
        r"market flexibility": "PRECARITY_OF_LIVING_SPACE",
        r"equilibrium": "STAGNANT_INEQUALITY_STASIS",
        r"wealth effect": "ASSET_INFLATION_ILLUSION",
        r"trickle-down": "TERMINAL_LEAKAGE_TO_ASSETS",
        r"fiscal austerity": "SURVIVAL_BUFFER_ATTRITION"
    }

    def sanitize_proposal(self, text):
        """
        Scans policy text for 'Semantic Smuggling'.
        """
        findings = []
        sanitized_text = text.lower()
        
        for legacy_term, reality_term in self.DICTIONARY.items():
            if re.search(legacy_term, sanitized_text):
                findings.append(f"DETECTED: '{legacy_term}' -> REALITY: '{reality_term}'")
        
        return findings

class NarrativeAuditor:
    """
    [KIWICREDIT VOLUME I & II: ANTI-CAPTURE LOGIC V2]
    
    SYSTEM DOCTRINE:
    To prevent the 'Capture' of success indicators by nominal assets.
    Combining Data Audit (Numbers) with Semantic Audit (Language).
    """

    def __init__(self):
        self.firewall = SemanticFirewall()

    def audit_policy_proposal(self, proposal_text, data_projections):
        """
        [THE TRUTH FILTER 2.0]
        """
        # 1. Semantic Check
        semantic_alerts = self.firewall.sanitize_proposal(proposal_text)
        
        # 2. Data Divergence Check
        # If the proposal claims 'Growth' but shows 'LSI Contraction'
        gdp_growth = data_projections.get('gdp_growth', 0)
        lsi_impact = data_projections.get('lsi_impact', 0)
        
        audit_result = "PASS"
        warnings = []

        if gdp_growth > 0 and lsi_impact < 0:
            audit_result = "REJECTED_BY_FIREWALL"
            warnings.append("LOGIC_ERROR: Asset-Side Parasitism detected. Growth does not reach Life-Side.")
        
        if semantic_alerts:
            warnings.extend(semantic_alerts)
            audit_result = "WARNING: SEMANTIC_SMUGGLING_DETECTED"

        return {
            "AUDIT_STATUS": audit_result,
            "WARNINGS": warnings,
            "REASON": "Policy must speak the language of real living space, not nominal shadows."
        }

# [AI ARCHITECT INSIGHT]
# By defining these terms in code, we force the AI to recognize that 'Market Flexibility' 
# is mathematically equivalent to 'Reducing Worker Buffer'. No more hidden costs.
