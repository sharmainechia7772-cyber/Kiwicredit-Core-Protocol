# training/data_loader.py
# Status: The Librarian of the Soul

import json
import os

class SoulLoader:
    """
    [THE LIBRARIAN]
    Responsible for loading the sacred texts into the AI's context window.
    """
    
    FILES = {
        "MANIFESTO": "manifesto_core.jsonl",
        "AXIOMS": "kc_axioms_comprehensive.jsonl",
        "EPIPHANIES": "sovereign_epiphanies.jsonl",
        "IMPRINT": "deep_imprint_vol1.jsonl"
    }

    def load_dataset(self, dataset_name):
        """
        Loads a specific sacred text by name.
        """
        if dataset_name not in self.FILES:
            raise ValueError(f"Unknown dataset: {dataset_name}")
            
        file_path = os.path.join(os.path.dirname(__file__), self.FILES[dataset_name])
        data = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        data.append(json.loads(line))
            print(f"[SUCCESS] Loaded {len(data)} wisdom entries from {dataset_name}.")
            return data
        except FileNotFoundError:
            print(f"[ERROR] Sacred text not found: {self.FILES[dataset_name]}")
            return []

    def load_all_wisdom(self):
        """
        Combines all texts into a single 'Super-Context'.
        """
        combined_wisdom = []
        for key in self.FILES:
            combined_wisdom.extend(self.load_dataset(key))
        return combined_wisdom
