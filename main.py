from apk_analysis.apk_parser import APKParser
from apk_analysis.manifest_analysis import ManifestAnalyzer
from apk_analysis.code_analysis import CodeAnalyzer
from apk_analysis.report_generator import ReportGenerator
from db.vulnerability_db import VulnerabilityDatabase

def main(apk_path):
    # Step 1: APK Parsing
    apk_parser = APKParser(apk_path)
    apk_parser.decompile_apk("output")
    
    # Step 2: Manifest Analysis
    manifest_path = "output/AndroidManifest.xml"  # Ensure the correct path to the manifest file
    manifest_analyzer = ManifestAnalyzer(manifest_path)
    insecure_permissions = manifest_analyzer.analyze_permissions()
    
    # Step 3: Code Analysis
    code_analyzer = CodeAnalyzer(apk_parser.get_decompiled_code())
    hardcoded_strings = code_analyzer.scan_for_hardcoded_strings()
    
    # Step 4: Combine Findings
    findings = insecure_permissions + hardcoded_strings
    
    # Step 5: Report Generation
    report_generator = ReportGenerator("report.txt")
    report_generator.generate_report(findings)
    print("Report generated at report.txt")

if __name__ == "__main__":
    apk_path = r"C:\Users\VEDHA\Downloads\F-Droid.apk"
    main(apk_path)

