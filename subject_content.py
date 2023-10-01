import json

class SubjectContent:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.visited = False

    def to_json(self):
        content_dict = {"name" : self.name,
                        "priority" : self.priority,
                        "visited" : self.visited
        }

        return json.dumps(content_dict)