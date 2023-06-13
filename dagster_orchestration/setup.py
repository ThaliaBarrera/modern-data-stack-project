from setuptools import find_packages, setup
import glob

setup(
    name="dagster_orchestration",
    packages=find_packages(exclude=["dagster_orchestration_tests"]),
    package_data={
        "dagster_orchestration": ["../" + path for path in glob.glob("dbt/big_star_collectibles/**", recursive=True)]
    },
    install_requires=[
        "dagster",
        "dagster-cloud[serverless]",
        "dagster-dbt",
        "pandas",
        "dbt-core",
        "dbt-bigquery",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
