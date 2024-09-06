from lxml import etree

class ManifestAnalyzer:
    def __init__(self, manifest_path):
        # Load the XML manifest file and get the root element
        self.manifest = etree.parse(manifest_path).getroot()

    def analyze_permissions(self):
        """Analyze and report insecure permissions."""
        permissions = []
        # Use XPath to find all 'uses-permission' elements
        for permission in self.manifest.findall(".//uses-permission"):
            name = permission.get("{http://schemas.android.com/apk/res/android}name")
            if name in self.insecure_permissions():
                permissions.append(name)
        return permissions

    def insecure_permissions(self):
        """Return a list of insecure permissions."""
        return [
            "android.permission.INTERNET",
            "android.permission.WRITE_EXTERNAL_STORAGE",
            "android.permission.READ_SMS",
            # Add more as needed
        ]
