import os
from dagster import Definitions, load_assets_from_modules
from dagster_dbt import DbtCliClientResource


from .assets import DBT_PROFILES, DBT_PROJECT_PATH

resources = {
    "dbt": DbtCliClientResource(
        project_dir=DBT_PROJECT_PATH,
        profiles_dir=DBT_PROFILES,
    ),

}

defs = Definitions(assets=load_assets_from_modules([assets]), resources=resources)
