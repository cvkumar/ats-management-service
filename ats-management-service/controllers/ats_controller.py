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
    return {"id": insert_id, "data_stored": request.json}, 200


# TODO: Add methods for all operations in swagger yaml

# def get_ats() -> Tuple[Dict, int]:
#     db_result = settings.DATABASE[ATS_TABLE].insert_one(request_data)
#     insert_id = str(db_result.inserted_id)
#     return {
#                'id': insert_id,
#                'data_stored': request.json
#            }, 200
