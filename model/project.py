class Project:

    def __init__(self, id=None, name=None, description=None, status=None, view_status=None):
        self.name = name
        self.description = description
        self.status = status
        self.view_status = view_status
        self.id = id

    def __repr__(self):
        return "%s;%s" % (self.name, self.description)

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description

    def name_key(self):
        if self.name:
            return self.name
