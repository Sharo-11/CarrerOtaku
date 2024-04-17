import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('F:/Authentication-System-Flask/instance/database.db')  

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

try:
    # Query the campus for students with first_name 'hina'
    cursor.execute("SELECT st_campus FROM student WHERE first_name = 'hinata';")
    
    # Fetch the result
    result = cursor.fetchone()
    
    if result:
        campus = result[0]
        print("Campus for student with first_name 'hina':", campus)
    else:
        print("No student found with first_name 'hina'")

except sqlite3.Error as e:
    print("Error:", e)

# Close the cursor and the connection
cursor.close()
conn.close()