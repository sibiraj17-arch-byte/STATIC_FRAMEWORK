class ReportGenerator:
    def __init__(self, output_file):
        self.output_file = output_file
    
    def generate_report(self, findings):
        """Generate a text report."""
        with open(self.output_file, "w") as f:
            for finding in findings:
                f.write(f"{finding}\n")
