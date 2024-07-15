"""
Actualiza este archivo para implementar los siguientes métodos ya declarados:
- add_member: Debería agregar un miembro a la lista self._members
- delete_member: Debería eliminar un miembro de la lista self._members
- update_member: Debería actualizar un miembro de la lista self._members
- get_member: Debería devolver un miembro de la lista self._members
"""

from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [
            {   "id": 1,
                "first_name": "john",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "first_name": "jane",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 3,
                "first_name": "jimmy",
                "age": 5,
                "lucky_numbers": [7]
            }
        ]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if not member.get("id"):
            member["id"] = self._generateId()  
        self._members.append(member) 

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)  

    def update_member(self, id, member):
        for family_member in self._members:
            if family_member["id"] == id:
                self._members.remove(family_member) 
                member["id"] = id 
                self._members.append(member)  
            

    def get_member(self, id):
        for family_member in self._members:
            if family_member["id"] == id:
                return family_member  

    def get_all_members(self):
        return self._members  