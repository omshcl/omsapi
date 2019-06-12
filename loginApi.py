from cassandra.cluster import Cluster

class LoginApi:

    
    # constructor for login api
    # creates Cluster session and prepars sql statements
    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect('oms')
        self.user_lookup_stmt = self.session.prepare("SELECT *  FROM users where username = ? and password = ? ALLOW FILTERING;")

    def checkUserPass(self,username,password):
        print("sesssion created")
        row = self.session.execute(self.user_lookup_stmt,[username,password])
        print(row.current_rows())
        z = row is None
        print(z)

    