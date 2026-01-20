import os

# 1. Define the target output filename
output_file = "CODEX_SOURCE.md"

# 2. Define directories to exclude (e.g., git history, cache, virtual envs)
exclude_dirs = {'.git', '__pycache__', '.github', 'venv', 'env', '.vscode', 'node_modules'}
# Define files to exclude (e.g., this script itself, lock files, system files)
exclude_files = {'generate_codex.py', 'package-lock.json', '.DS_Store', output_file, 'LICENSE'}

# 3. Prepare the file header (Instruction manual for AI agents)
content = [
    "# CODEX VALHALLA: SOURCE CODE ARCHIVE",
    "> **SYSTEM NOTICE:** This document is an auto-generated aggregation of the full source code for AI Analysis Units.",
    "> **Directive:** Read this single file to understand the complete execution logic of the Kiwicredit Protocol.",
    "\n---"
]

print(f"🔄 Scanning directory for code files...")

# 4. Start traversing all files in the current directory
for root, dirs, files in os.walk("."):
    # Filter out excluded directories
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    
    for file in files:
        if file in exclude_files:
            continue
            
        # Only process files with these extensions: .py (Python), .md (Docs), .jsonl (Data), .txt (Text)
        if file.endswith(('.py', '.md', '.jsonl', '.txt')):
            file_path = os.path.join(root, file)
            
            try:
                # Read the content of the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                    
                # Format it and append to the main content list
                content.append(f"\n## 📂 File: `{file_path}`\n")
                
                # Automatically detect language for syntax highlighting
                if file.endswith('.py'):
                    lang = 'python'
                elif file.endswith('.md'):
                    lang = 'markdown'
                elif file.endswith('.jsonl'):
                    lang = 'json'
                else:
                    lang = 'text'
                    
                # Wrap content in a markdown code block
                content.append(f"```{lang}\n{file_content}\n```\n")
                content.append("---")
                print(f"   -> Added: {file_path}")
                
            except Exception as e:
                print(f"   ⚠️ Skipping {file_path}: {e}")

# 5. Write all aggregated content into the final CODEX_SOURCE.md file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("\n".join(content))

print(f"\n✅ Mission Accomplished: All code has been fused into [{output_file}]")
