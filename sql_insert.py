import psycopg2

# Connection details
hostname = "" #add hostname of your database server
database = ""   #add database name you want to connect to
port = ""                   #add port number of your database server
username = ""   #add username for your database
password = "" #add password for your database user

# Establishing the connection
conn = psycopg2.connect(
    database=database,
    user=username,
    password=password,
    host=hostname,
    port=port
)
cursor = conn.cursor()
print("✅ Connected to database")

# Step 1: Create schema
cursor.execute("CREATE SCHEMA IF NOT EXISTS ecommerce;")
print("✅ Schema 'ecommerce' created")

# Step 2: Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ecommerce.orders (
        order_id SERIAL PRIMARY KEY,
        customer_name VARCHAR(100),
        order_amount DECIMAL(10, 2),
        order_date DATE
    );
""")
print("✅ Table 'ecommerce.orders' created")

# Step 3: Insert sample data modify accordingly
cursor.execute("""
    INSERT INTO ecommerce.orders (customer_name, order_amount, order_date) VALUES
    ('Alice', 120.50, '2024-07-01'),
    ('Bob', 80.00, '2024-07-02'),
    ('Charlie', 200.00, '2024-07-03'),
    ('Diana', 150.25, '2024-07-04'),
    ('Eve', 60.00, '2024-07-05')
    ON CONFLICT DO NOTHING;
""")
print("✅ Sample records inserted")

# Commit changes
conn.commit()

# Step 4: Query and display inserted data
cursor.execute("SELECT * FROM ecommerce.orders;")
rows = cursor.fetchall()
print("\n📦 Orders Table Data:")
for row in rows:
    print(row)

# Closing the connection
cursor.close()
conn.close()
print("\n🔚 Connection closed.")
