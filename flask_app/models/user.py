from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name='users'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
       # self.username = data['username']
       # self.password = data['password']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    # might need to do some stuff to this to make it match the db
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name, email, created_at, updated_at ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW())"
        return connectToMySQL('users').query_db( query, data )

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"
        return connectToMySQL('users').query_db(query, data)

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET full_name=%(full_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users').query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s";
        result = connectToMySQL('users').query_db(query,data)
        return cls(result[0])



