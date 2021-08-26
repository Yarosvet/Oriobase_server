from flask import make_response, jsonify
from base64 import b64encode, b64decode
from data.db_session import create_session
from data.types import Object, Field, Relation


def get_object(object_id: int):
    session = create_session()
    obj = session.query(Object).get(object_id)
    if not obj:
        return make_response(jsonify({'error': 'Not found'}), 404)
    answer = {"id": obj.id,
              "name": obj.name,
              "fields": [__field_to_json(el) for el in obj.fields],
              "relations": [__relation_to_json(el) for el in obj.relations]}
    return jsonify(answer)


def __field_to_json(field: Field) -> dict:
    return {"name": field.name,
            "data_type": field.data_type,
            "data": b64encode(field.data)}


def __relation_to_json(rel: Relation) -> dict:
    return {"name": rel.name,
            "type": rel.type,
            "target": rel.target_id}
