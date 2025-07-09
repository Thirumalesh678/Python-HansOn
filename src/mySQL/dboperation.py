import oracledb

try:
    servername = "localhost:1521/XE"
    username = "thiru" 
    password = "12345"

    oracledb.init_oracle_client(lib_dir =r"C:\oracle\instantclient_23_8")

    connection = oracledb.connect(user=username,password=password,dsn=servername)
    cursor = connection.cursor()


    cursor.execute("select * from emp")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

except oracledb.DatabaseError as e:
    print("Database Exception",e)

except Exception as ex:
    print("Unexpected error: ",ex)

finally:
    if 'cursor' in locals():
        cursor.close()

    if 'connection' in locals():
        connection.close()
    print("exception connection closed")