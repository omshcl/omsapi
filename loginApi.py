from cassandra.cluster import Cluster

class LoginApi:

    
    # constructor for login api
    # creates Cluster session and prepars sql statements
    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect('oms')
        self.user_lookup_stmt = self.session.prepare("SELECT *  FROM users where username = ? and password = ? ALLOW FILTERING;")
        self.is_admin_stmt = self.session.prepare("SELECT isAdmin from users where username = ?")

    def isUser(self,username,password):
        row = self.session.execute(self.user_lookup_stmt,[username,password])
        return  row.current_rows != []

    def isAdmin(self,username):
        row = self.session.execute(self.is_admin_stmt,[username])
        if not row:
            return False
        return row[0].isadmin
