import sqlite3
import json

def get_all_orders():
    # Connect to the database
    with sqlite3.connect('kneeldiamonds.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        # Execute SQL query
        db_cursor.execute("SELECT * FROM Orders")
        
        # Fetch all results
        query_results = db_cursor.fetchall()
    
    # Initialize an empty list and then add each dictionary to it
    orders = []

    # provide orders info   
    for row in query_results:
        order = {
            "metal_id": row['metal_id'],
            "size_id": row['size_id'],
            "style_id": row['style_id'],
            "id": row["id"]
        }
        orders.append(order)  

    # Serialize Python list to JSON encoded string
    orders_json = json.dumps(orders)

    return orders_json  
