from flask import make_response, jsonify, request
from json import loads
from base64 import b64encode, b64decode
from data.db_session import create_session
from data.types import Object, ObjectGroup, Field, Relation
from config import TOKENS


def get_object(object_id=None):
    if not object_id:
        try:
            object_id = int(request.args.get('id'))
        except Exception:
            return make_response(jsonify({'error': 'Id invalid'}), 400)
    session = create_session()
    obj = session.query(Object).get(object_id)
    session.close()
    if not obj:
        return make_response(jsonify({'error': 'Not found'}), 404)
    answer = {"id": obj.id,
              "name": obj.name,
              "fields": [__field_to_json(el) for el in obj.fields],
              "relations": [__relation_to_json(el) for el in obj.relations]}
    return jsonify(answer)


def get_object_group(group_id=None):
    if not group_id:
        try:
            group_id = int(request.args.get('id'))
        except Exception:
            return make_response(jsonify({'error': 'Name invalid'}), 400)
    session = create_session()
    obj_group = session.query(ObjectGroup).get(group_id)
    session.close()
    if not obj_group:
        return make_response(jsonify({'error': 'Not found'}), 404)
    answer = {"id": obj_group.id,
              "name": obj_group.name,
              "description": obj_group.description,
              "objects_id": obj_group.objects_id}
    return jsonify(answer)


def new_object():
    token = request.args.get('token')
    name = request.args.get('name')
    fields = request.args.get('fields')
    relations = request.args.get('relations')
    if token not in TOKENS:
        return make_response(jsonify({'error': 'Token invalid'}), 401)
    if not name:
        return make_response(jsonify({'error': 'Name invalid'}), 400)
    try:
        obj_fields = __fields_from_json(fields)
    except Exception:
        return make_response(jsonify({'error': 'Fields invalid'}), 400)
    try:
        obj_relations = __relations_from_json(relations)
    except Exception:
        return make_response(jsonify({'error': 'Fields invalid'}), 400)
    session = create_session()
    obj = Object(name=name, fields=obj_fields, relations=obj_relations)
    session.add(obj)
    session.commit()
    obj_id = obj.id
    session.close()
    return get_object(obj_id)


def new_object_group():
    token = request.args.get('token')
    name = request.args.get('name')
    description = request.args.get('description')
    objects = request.args.get('objects')
    if token not in TOKENS:
        return make_response(jsonify({'error': 'Token invalid'}), 401)
    if not name:
        return make_response(jsonify({'error': 'Name invalid'}), 400)
    try:
        objects = loads(objects)
    except Exception:
        return make_response(jsonify({'error': 'Objects list invalid'}), 400)
    session = create_session()
    obj_group = ObjectGroup(name=name, description=str(description), objects_id=objects)
    session.add(obj_group)
    session.commit()
    obj_group_id = obj_group.id
    session.close()
    return get_object_group(obj_group_id)


def __field_to_json(field: Field) -> dict:
    return {"name": field.name,
            "data_type": field.data_type,
            "data": b64encode(bytes(field.data, encoding="utf-8")).decode("utf-8")}


def __relation_to_json(rel: Relation) -> dict:
    return {"name": rel.name,
            "type": rel.type,
            "target_id": rel.target_id}


def __fields_from_json(json_str: str) -> list:
    return [Field(name=el["name"], data_type=el["data_type"], data=b64decode(el["data"]).decode("utf-8")) for el in
            loads(json_str)]


def __relations_from_json(json_str: str) -> list:
    session = create_session()
    res = []
    for el in loads(json_str):
        if el["type"] == "Object":
            res.append(Relation(name=el["name"], target=session.query(Object).get(el["target_id"])))
        elif el["type"] == "ObjectGroup":
            res.append(Relation(name=el["name"], target=session.query(ObjectGroup).get(el["target_id"])))
    session.close()
    return res
