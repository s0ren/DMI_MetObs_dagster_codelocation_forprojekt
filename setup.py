from setuptools import find_packages, setup

setup(
    name="DMI_MetObs",
    packages=find_packages(exclude=["DMI_MetObs_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-duckdb"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
