import os

class CodeAnalyzer:
    def __init__(self, decompiled_code_path):
        self.decompiled_code_path = decompiled_code_path
    
    def scan_for_hardcoded_strings(self):
        """Scan decompiled code for hardcoded credentials."""
        issues = []
        for root, dirs, files in os.walk(self.decompiled_code_path):
            for file in files:
                if file.endswith(".smali"):
                    with open(os.path.join(root, file), "r") as f:
                        content = f.read()
                        if "password" in content.lower() or "apikey" in content.lower():
                            issues.append(f"Hardcoded string found in {file}")
        return issues
