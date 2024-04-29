import sqlite3

def query_sqlite_file(file_path, query):
    # Connect to the SQLite database file
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()

    try:
        # Execute the query
        cursor.execute(query)

        # Fetch all the results
        rows = cursor.fetchall()

        return(rows)

        # Print the results
        # for row in rows:
        #     print(row)
    
    except sqlite3.Error as e:
        print("Error executing SQLite query:", e)

    finally:
        # Close the connection
        conn.close()

def count_lines_starting_with_hash(input_string):
    lines = input_string.split('\n')
    count = 0
    for line in lines:
        if line.strip().startswith('#'):
            count += 1
    return count

file_path = './pkm.sqlite'
query = "SELECT raw_markdown FROM markdown_nodes;"
results = query_sqlite_file(file_path, query)
cell_count = 0
for row in results:
    # print(row[0])
    cell_count += count_lines_starting_with_hash(row[0])
print(f"Nodes: {len(results)}")
print(f"Cells: {cell_count}")