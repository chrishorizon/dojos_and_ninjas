from flask_app.config.mysqlcontroller import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_info(cls):
        query = 'SELECT * FROM dojos'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        
        for data in results:
            dojos.append(cls(data))
        return dojos

    @classmethod
    def add_dojo(cls,data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s)'
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result

    @classmethod
    def get_ninja(cls, data):
        query = 'SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s'

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        
        for ninja in results:
            user = {
                'id': ninja['ninjas.id'],
                'first_name': ninja['first_name'],
                'last_name': ninja['last_name'],
                'age': ninja['age'],
                'created_at': ninja['ninjas.created_at'],
                'updated_at': ninja['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(user))

        return dojo