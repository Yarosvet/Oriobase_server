class Object:
    def __init__(self, name: str, fields: list, relations: list):
        self.name = name
        self.fields = fields
        self.relations = relations


class Field:
    def __init__(self, field_type: str, name: str):
        self.field_type = field_type
        self.name = name


class Relation:
    def __init__(self, name: str):
        self.name = name


class ObjectGroup:
    def __init__(self, name: str, objects: list):
        self.name = name
