
import psycopg2
class ServerDAO():
    def connect(self):
        return psycopg2.connect("dbname=ds2Mail user=postgres host=localhost")

    def login(self, email, password):
        conn = self.connect()
        cur = conn.cursor()

        try:
            cur.execute('SELECT * FROM "user" WHERE email = %s and password = %s', [email, password])
            result = cur.fetchall()
            
            conn.close()
            cur.close()
            return result
        except IndexError: 
             return None
        except BaseException:
             return None

    def subscribe(self, email):
        conn = self.connect()
        cur = conn.cursor()

        try:
            cur.execute('INSERT INTO "subscribe" (email) VALUES(%s)', [email])
            conn.commit()

            conn.close()
            cur.close()
            return True
        except IndexError:
            return None
        except BaseException:
            return None

    def send(self, email, message):
        conn = self.connect()
        cur = conn.cursor()

        try:
            cur.execute('INSERT INTO "public" (email, message) VALUES(%s, %s)', [email, message])
            conn.commit()

            conn.close()
            cur.close()
            return True
        except IndexError: 
            return None
        except BaseException:
            return None

    def search(self):
        conn = self.connect()
        cur = conn.cursor()
        
        cur.execute('SELECT * FROM "subscribe"')
        result = cur.fetchall()

        emails = []
        for user in result:
            emails.append(user[1])
        return emails

        conn.close()
        cur.close()

    def message(self):
        conn = self.connect()
        cur = conn.cursor()

        cur.execute('SELECT * FROM "public"')
        result = cur.fetchall()

        emails = []
        msg = []
        for user in result:
            emails.append(user[1])
            msg.append(user[2])
        return [emails, msg]

        conn.close()
        cur.close()
