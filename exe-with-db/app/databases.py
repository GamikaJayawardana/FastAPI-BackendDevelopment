import sqlite3
from typing import Any

from app.schemas import ShipmentCreate, ShipmentUpdate

class ShipmentsDatabase:
    def connect_db(self):
        self.conn = sqlite3.connect('sqlite.db', check_same_thread=False)
        self.cur = self.conn.cursor()   

    def create_table(self):
        self.cur.execute ("""
            CREATE TABLE IF NOT EXISTS shipment (
                id INTEGER PRIMARY KEY, 
                content TEXT, 
                weight REAL, 
                status TEXT
            )
        """)
        self.conn.commit()
        
    def create (self, shipment: ShipmentCreate):
        self.cur.execute("""
            SELECT MAX(id) FROM shipment
        """)
        result = self.cur.fetchone()
        new_id = result[0] + 1

        self.cur.execute("""
            INSERT INTO shipment
            VALUES (:id, :content, :weight, :status)       
        """, 
            {
                "id": new_id,
                **shipment.model_dump(),
                "status": "placed"
            }
        )
        self.conn.commit()

    def get(self, id) -> dict[str, Any] | None:
        self.cur.execute("""
            SELECT * FROM shipment 
            WHERE id = :id
        """, {"id": id})
        raw = self.cur.fetchone()
        return {
            "id": raw[0],
            "content": raw[1],
            "weight": raw[2],
            "status": raw[3]
        } if raw else None
    

    def update(self, id: int, shipment: ShipmentUpdate) -> dict[str, Any] | None:
        self.cur.execute("""
            UPDATE shipment 
            SET status = :status 
            WHERE id = :id
        """, {
            "id": id,
            **shipment.model_dump()

        })
        self.conn.commit()
        return self.get(id)
    
    def delete(self, id) -> None:
        self.cur.execute("""
            DELETE FROM shipment 
            WHERE id = :id
        """, {"id": id})
        self.conn.commit()

    def close(self):
        self.conn.close()

    def __enter__(self):
        self.connect_db()
        self.create_table()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


# Create a connection to the SQLite database
# connection = sqlite3.connect('sqlite.db')
# cursor = connection.cursor()

# Create a table named 'shipment' if it doesn't already exist
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS shipment (
#         id INTEGER PRIMARY KEY, 
#         content TEXT, 
#         weight REAL, 
#         status TEXT
#     )
# """)

# Drop the 'shipment' table if it exists
# cursor.execute("""DROP TABLE shipment""")
# connection.commit()

# cursor.execute("""
#     INSERT INTO shipment
#     VALUES (12703, 'Bears', 24.5, 'In Transit')       
# """)
# connection.commit()

# Fetch all records from the 'shipment' table and print them
# cursor.execute("""
#     SELECT * FROM shipment    
# """)

# Fetch only the first record from the executed query and print it
# cursor.execute("""
#     SELECT status FROM shipment 
#     WHERE id = 12703 
# """)

# Delete the record with id 12703 from the 'shipment' table
# cursor.execute("""
#     DELETE FROM shipment 
#     WHERE id = 12703
# """)


# Update the status of the record with id 12703 to 'Delivered' in the 'shipment' table
# cursor.execute("""
#     UPDATE shipment 
#     SET status = 'Delivered' 
#     WHERE id = 12703
# """)
# connection.commit()

# id = "12703"
# status = 'Delivered'

# cursor.execute("""
#     UPDATE shipment 
#     SET status = :status 
#     WHERE id = :id
# """, {"status": status, "id": id})
# connection.commit()


# Fetch all results from the executed query and print them
# result = cursor.fetchall() 

# Fetch only the first two records from the executed query and print them
# result = cursor.fetchmany(2)
# print(result)

# connection.close()