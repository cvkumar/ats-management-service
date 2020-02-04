from typing import Dict, Tuple
from connexion import request

import copy

from services.ats_storage_service import insert_ats_config, retrieve_ats_config


def post_ats_config(tenant: str) -> Tuple[Dict, int]:
    request_data = copy.deepcopy(request.json)

    result = insert_ats_config(tenant, request_data)
    insert_id = str(result.inserted_id)
    response_dict = {"_id": str(insert_id), "tenant": tenant}
    response_dict.update(request.json)
    return response_dict, 200


def get_ats_config(tenant: str) -> Tuple[Dict, int]:
    db_result = retrieve_ats_config(tenant)
    if db_result:
        insert_id = str(db_result.get("_id"))
        del db_result["_id"]
        response_dict = {"_id": insert_id, "tenant": tenant}
        response_dict.update(db_result)
        return response_dict, 200

    return {}, 200
