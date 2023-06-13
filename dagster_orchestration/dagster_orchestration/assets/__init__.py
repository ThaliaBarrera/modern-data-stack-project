import os
from dagster import file_relative_path
from dagster_dbt import load_assets_from_dbt_project
from dagster_airbyte import load_assets_from_airbyte_instance
from dagster_airbyte import AirbyteResource

airbyte_instance = AirbyteResource(
    host="localhost",
    port="8000",
    # If using basic auth, include username and password:
    username="airbyte",
    password=os.getenv("AIRBYTE_PASSWORD")
)

airbyte_assets = load_assets_from_airbyte_instance(airbyte_instance, key_prefix=["raw_data"])

DBT_PROJECT_PATH = file_relative_path(__file__, "../../../dbt/big_star_collectibles")
DBT_PROFILES = file_relative_path(__file__, "../../../dbt/big_star_collectibles/config")

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH, profiles_dir=DBT_PROFILES, key_prefix=["big_star_collectibles"]
)
