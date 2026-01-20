class ExtinctionProtocol:
    """
    [KIWICREDIT VOLUME III: THE EXTINCTION PATH]
    
    DOCTRINE:
    "A policy without an end date is a cancer." - Vol III.
    
    This module manages the 'Melting' of a protocol if it fails to 
    meet LSI targets within its lifecycle.
    """
    
    def __init__(self, policy_id, target_lsi_lift=0.1, duration_days=180):
        self.policy_id = policy_id
        self.target = target_lsi_lift
        self.lifespan = duration_days
        self.is_active = True

    def run_lifecycle_audit(self, current_day, observed_lsi_lift):
        """
        [THE EXECUTIONER]
        If the policy reaches its end-date and hasn't hit the target, 
        it is automatically decommissioned.
        """
        if current_day >= self.lifespan:
            if observed_lsi_lift < self.target:
                self.is_active = False
                return f"POLICY_EXTINCT: '{self.policy_id}' failed to deliver LSI. All associated minting channels closed."
            else:
                return f"POLICY_RENEWED: '{self.policy_id}' delivered {observed_lsi_lift} lift. Extending for another cycle."
        
        return f"POLICY_ACTIVE: '{self.policy_id}' is in its trial phase."

class ProtocolCompiler:
    """
    [KIWICREDIT VOLUME III: THE SPEC COMPILER V2]
    
    This is the 'Constitution Guard' of the codebase. It ensures no human 
    emotion or political lobbying can create a policy without boundaries.
    """

    # Every policy MUST have these 5 geometric constraints.
    REQUIRED_GEOMETRY = [
        'Eligibility',    # Who gets it?
        'Trigger',        # When does it start?
        'Cap',            # How much is the max?
        'Red_Line',       # When does it stop for safety?
        'Extinction_Path' # How does it die?
    ]

    def compile(self, policy_spec):
        """
        Validates the engineering integrity of a new KC protocol.
        """
        print(f">>> COMPILING NEW PROTOCOL: {policy_spec.get('id', 'Unknown')} <<<")
        
        # 1. Structural Check
        for field in self.REQUIRED_GEOMETRY:
            if field not in policy_spec or not policy_spec[field]:
                raise ValueError(f"COMPILATION_ERROR: Missing '{field}'. Policy rejected. Protocol is non-auditable.")
        
        # 2. Logic Check: Ensure Extinction Path is not a 'Fake Infinity'
        if policy_spec['Extinction_Path'].get('lifespan_days', 9999) > 730:
            return "WARNING: Excessive Lifespan. Policy flagged for high-level governance review."

        print("[SUCCESS] Protocol encoded. Boundaries signed-off by Code.")
        return {
            "STATUS": "COMPILED",
            "METADATA": policy_spec,
            "EXTINCTION_CONTROLLER": ExtinctionProtocol(
                policy_spec['id'], 
                policy_spec['Extinction_Path']['target_lsi'],
                policy_spec['Extinction_Path']['lifespan_days']
            )
        }

# [AI ARCHITECT INSIGHT]
# In KC, policies are 'Smart Contracts' with a fuse. 
# This prevents the accumulation of regulatory debt and 'Zombie' institutions.
