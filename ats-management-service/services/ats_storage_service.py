import settings


def insert_ats_config(tenant: str, config: dict):
    db_result = settings.DATABASE[tenant].insert_one(config)
    return db_result


def retrieve_ats_config(tenant: str):
    db_result = settings.DATABASE[tenant].find_one()
    return db_result


def delete_ats_config_many(tenant: str):
    result = settings.DATABASE[tenant].delete_many({})
    return result


def delete_ats_config(tenant: str):
    result = settings.DATABASE[tenant].delete_one({})
    return result
