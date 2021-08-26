from flask import make_response, jsonify
from base64 import b64encode, b64decode
from data.db_session import create_session
from data.types import Object, ObjectGroup, Field, Relation


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


def get_object_group(group_id: int):
    session = create_session()
    obj_group = session.query(ObjectGroup).get(group_id)
    if not obj_group:
        return make_response(jsonify({'error': 'Not found'}), 404)
    answer = {"id": obj_group.id,
              "name": obj_group.name,
              "description": obj_group.description,
              "objects_id": obj_group.objects_id}
    return jsonify(answer)


def __field_to_json(field: Field) -> dict:
    return {"name": field.name,
            "data_type": field.data_type,
            "data": b64encode(field.data)}


def __relation_to_json(rel: Relation) -> dict:
    return {"name": rel.name,
            "type": rel.type,
            "target": rel.target_id}
