import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql=""" 
        CREATE TABLE IF NOT EXISTS employees(
            id integer Primary key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    #Insert Function:
    def insert (self, name, age, doj, email, gender, contact, address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                         (name, age, doj, email, gender, contact, address))
        self.con.commit()

    #Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows=self.cur.fetchall()
        #print(rows)
        return rows

    #Delete a Record in DB
    def remove(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()

    #update a Record in DB
    def update(self, id, name, age, doj, email, gender, contact, address ):
        self.cur.execute("update employees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?",
                         (name, age, doj, email, gender, contact, address,id))
        self.con.commit()


#o=Database("Employee.db")
#o.insert("Imran","22","15-08-1991","imran777@gmail.com","male","964682148","USA")
#o.fetch()
#o.remove("5")
#o.update("2","Imran Khan","30","16-10-2020","Imranusa@gmail.com","Male","9994556677","Newyork")