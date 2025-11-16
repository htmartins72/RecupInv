import sqlite3
import sys
import time
import os

def main():
    if len(sys.argv) != 2:                                              # It must have 2 args 
        print("Usage: python recup_inventarios.py <database.db>")       # Some Help using this shit
        sys.exit(1)                                                     # Stops exectution 

    db_path = sys.argv[1]                                               # defines path to db file
    sql_path = os.path.splitext(db_path)[0] + ".sql"                    # define outfile path

    print(f"Início do Ficheiro {db_path}")                              # Some info on screen

    start_time = time.perf_counter()                                    # Starts the timer 

    with open(sql_path, 'w', encoding='utf-8') as output:               # Open output stream
        try:                                                            # try block
            conn = sqlite3.connect(db_path)                             # connect to sqlite3 db
            conn.row_factory = sqlite3.Row                              # Allows column access by name
            cursor = conn.cursor()                                      # create cursor

            cursor.execute("SELECT * FROM InventoryDetails WHERE Picado = '1'") # the query

            for row in cursor:                                          # Begin the loop 
                inv_id = row[0]                                         # First column: id
                qty = row[9]                                            # 10th column: QTY (0-indexed)
                update_sql = (
                    f"Update Ekanban.Inventario_det "
                    f"Set Qt_inventariada = '{qty}', picado = '1' "
                    f"where id = {inv_id} and Picado !='1'"
                )                                                       # The update sql to save
                output.write(update_sql + "\n")                         # Add the sql to the stream

            conn.close()                                                # Close connection to sqlite3
        except sqlite3.Error as e:                                      # SQLite3 Error handling
            print(f"Database error: {e}")                               # Error message
            sys.exit(1)
        except Exception as e:                                          # Error handling
            print(f"Error: {e}")                                        # Error message
            sys.exit(1)

    elapsed_ms = (time.perf_counter() - start_time) * 1000              # Stop the timer

    print(f"Total execution time: {int(elapsed_ms)} ms")                # Exec time
    print(f"Precise time: {elapsed_ms:.2f} ms")                         # Exec time precise
    print(f"Concluído no ficheiro {sql_path}")                          # output file 

    input("Press Enter to exit...")                                     # Wait for input

if __name__ == "__main__":                                              # Is this the main func?
    main()                                                              # Run this shit