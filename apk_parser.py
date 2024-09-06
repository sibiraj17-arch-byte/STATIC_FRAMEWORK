import subprocess
import os
from androguard.core.bytecodes.apk import APK

class APKParser:
    def __init__(self, apk_path):
        self.apk_path = apk_path
        self.decompiled_dir = None
        self.apk = APK(apk_path)
    
    def decompile_apk(self, output_dir):
        """Decompile the APK using APKTool."""
        self.decompiled_dir = output_dir
        subprocess.run([r"C:\Users\VEDHA\apktool\apktool.bat", "d", self.apk_path, "-o", output_dir], check=True)
    
    def get_manifest(self):
        """Return the AndroidManifest.xml."""
        return self.apk.get_android_manifest_xml()
    
    def get_permissions(self):
        """Return the list of permissions."""
        return self.apk.get_permissions()
    
    def get_decompiled_code(self):
        """Return the path to decompiled code."""
        return os.path.join(self.decompiled_dir, "smali")
