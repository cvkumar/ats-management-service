from typing import Dict, Tuple
from connexion import request

import settings
from common.constants import ATS_TABLE

import copy


def post_ats() -> Tuple[Dict, int]:
    request_data = copy.deepcopy(request.json)
    print(f"Creating ATS with: {request_data}")
    db_result = settings.DATABASE[ATS_TABLE].insert_one(request_data)
    insert_id = str(db_result.inserted_id)
    return {"_id": insert_id, "ats_stored": request.json}, 200


def get_ats() -> Tuple[Dict, int]:
    db_result = settings.DATABASE[ATS_TABLE].find_one()
    if db_result:
        insert_id = str(db_result.get("_id"))
        del db_result["_id"]
        return {"_id": insert_id, "ats_stored": db_result}, 200

    return {}, 200


def put_ats() -> Tuple[Dict, int]:
    request_data = copy.deepcopy(request.json)
    print(f"Updating ATS with: {request_data}")
    if not settings.DATABASE[ATS_TABLE].find_one():
        settings.DATABASE[ATS_TABLE].insert_one(request_data)
    else:
        settings.DATABASE[ATS_TABLE].replace_one({}, request_data)
    return {"ats_stored": request.json}, 200


def patch_ats() -> Tuple[Dict, int]:
    ats_data = settings.DATABASE[ATS_TABLE].find_one()
    if ats_data:
        del ats_data["_id"]
        ats_data.update(request.json)
        settings.DATABASE[ATS_TABLE].replace_one({}, ats_data)

        return {"ats_stored": ats_data}, 200
    else:
        return {"error": "No ATS configured"}, 400


def delete_ats() -> Tuple[Dict, int]:
    result = settings.DATABASE[ATS_TABLE].delete_many({})
    return {"deleted": result.deleted_count}, 200
