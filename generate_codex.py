import os

# 1. Define output file
output_file = "CODEX_SOURCE.md"

# 2. Exclusions
exclude_dirs = {'.git', '__pycache__', '.github', 'venv', 'env', '.vscode', 'node_modules'}
exclude_files = {'generate_codex.py', 'package-lock.json', '.DS_Store', output_file, 'LICENSE'}

# 3. Header
content = [
    "# CODEX VALHALLA: SOURCE CODE ARCHIVE",
    "> **SYSTEM NOTICE:** This document is an auto-generated aggregation of the full source code for AI Analysis Units.",
    "> **Directive:** Read this single file to understand the complete execution logic of the Kiwicredit Protocol.",
    "\n---"
]

print(f"🔄 Scanning and prioritizing artifacts...")

# --- ⚡ PRIORITY INJECTION (The VIP List) ---
# We force these files to appear FIRST so AI reads them before hitting token limits.
priority_files = [
    "./WHITEPAPER.md",
    "./core/decay_engine.py",
    "./sovereignty/circuit_breaker.py",
    "./core/minting_protocol.py",
    "./identity_matrix.py",
    "./main.py"
]

processed_files = set()

# Process VIP files first
for file_path in priority_files:
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            
            content.append(f"\n## 🌟 PRIORITY ARTIFACT: `{file_path}`\n")
            
            lang = 'python' if file_path.endswith('.py') else 'markdown'
            content.append(f"```{lang}\n{file_content}\n```\n")
            content.append("---")
            print(f"   -> 🚀 Injected Priority: {file_path}")
            processed_files.add(os.path.abspath(file_path))
        except Exception as e:
            print(f"   ⚠️ Error reading priority file {file_path}: {e}")

# --- STANDARD SCAN (The Rest) ---
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    
    for file in files:
        if file in exclude_files:
            continue
            
        if file.endswith(('.py', '.md', '.jsonl', '.txt')):
            file_path = os.path.join(root, file)
            abs_path = os.path.abspath(file_path)
            
            # Skip if already processed in VIP list
            if abs_path in processed_files:
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                
                content.append(f"\n## 📂 File: `{file_path}`\n")
                
                if file.endswith('.py'): lang = 'python'
                elif file.endswith('.md'): lang = 'markdown'
                elif file.endswith('.jsonl'): lang = 'json'
                else: lang = 'text'
                    
                content.append(f"```{lang}\n{file_content}\n```\n")
                content.append("---")
                print(f"   -> Added: {file_path}")
                
            except Exception as e:
                print(f"   ⚠️ Skipping {file_path}: {e}")

# Write output
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("\n".join(content))

print(f"\n✅ Mission Accomplished: Optimized Codex generated at [{output_file}]")
