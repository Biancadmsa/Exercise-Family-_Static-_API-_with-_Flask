from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        }, {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        }, {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)

    def delete_member(self, id):
        self._members = [member for member in self._members if member["id"] != id]

    def update_member(self, id, member):
        for i, existing_member in enumerate(self._members):
            if existing_member["id"] == id:
                self._members[i] = member
                break

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member

    def get_all_members(self):
        return self._members