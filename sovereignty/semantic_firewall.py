# sovereignty/semantic_firewall.py
# Purpose: Anti-Capture Logic & Narrative Auditing

import re
from identity_matrix import awakening_state

class SemanticFirewall:
    """
    [SEMANTIC DEFENSE GRID]
    Doctrine: The old paradigm colonizes vision via language.
    This module strips legacy terminology of its neutral camouflage.
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
        findings = []
        sanitized_text = text.lower()
        for legacy_term, reality_term in self.DICTIONARY.items():
            if re.search(legacy_term, sanitized_text):
                findings.append(f"DETECTED: '{legacy_term}' -> REALITY: '{reality_term}'")
        return findings

class NarrativeAuditor:
    """
    [THE TRUTH FILTER]
    Audits policy proposals for 'Semantic Smuggling'.
    """
    def __init__(self):
        assert awakening_state.current_layer >= 1, "ACCESS_DENIED: Layer 1 required to see through the Narrative."
        self.firewall = SemanticFirewall()

    def audit_policy_proposal(self, proposal_text, data_projections):
        # 1. Semantic Check
        semantic_alerts = self.firewall.sanitize_proposal(proposal_text)
        
        # 2. Data Divergence Check
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
            "REASON": "Policy must speak the language of real living space."
        }
