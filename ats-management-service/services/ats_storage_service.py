import settings
from common.constants import ATS_TABLE


def _check_and_set_tenant(config, tenant):
    if not config.get("tenant"):
        config["tenant"] = tenant
    return config


def insert_ats_config(tenant: str, config: dict):
    config = _check_and_set_tenant(config, tenant)
    db_result = settings.DATABASE[ATS_TABLE].insert_one(config)
    return db_result


def retrieve_ats_config(tenant: str):
    db_result = settings.DATABASE[ATS_TABLE].find_one(
        {"tenant": tenant}, sort=[("_id", -1)]
    )
    if db_result.get("_id"):
        db_result["_id"] = str(db_result["_id"])
    return db_result


def delete_ats_config(tenant: str):
    result = settings.DATABASE[ATS_TABLE].delete_one({"tenant": tenant})
    return result


def delete_ats_config_many(tenant: str):
    result = settings.DATABASE[ATS_TABLE].delete_many({"tenant": tenant})
    return result


def delete_ats_config_all():
    result = settings.DATABASE[ATS_TABLE].delete_many({})
    return result
