from setuptools import setup, find_packages

setup(
    name="android-static-analysis",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "androguard"
    ],
    entry_points={
        "console_scripts": [
            "analyze-apk=src.main:main"
        ]
    },
)
