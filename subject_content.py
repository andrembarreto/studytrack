import json

class SubjectContent:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.visited = False

    def __eq__(self, __value: object):
        return isinstance(__value, SubjectContent) and self.name == __value.name

    def mark_as_visited(self):
        self.visited = True

    def to_json(self):
        content_dict = {"name" : self.name,
                        "priority" : self.priority,
                        "visited" : self.visited
        }

        return json.dumps(content_dict)
    
    @staticmethod
    def from_json(json_obj):
        json_obj = json.loads(json_obj)
        content = SubjectContent(name=json_obj.get('name'), priority=json_obj.get('priority'))
        if json_obj['visited']:
            content.mark_as_visited()

        return content