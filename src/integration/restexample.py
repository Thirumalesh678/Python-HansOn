import requests as rq
import oracledb

servername = "localhost:1521/XE"
username = "thiru" 
password = "12345"

oracledb.init_oracle_client(lib_dir =r"C:\oracle\instantclient_23_8")

connection = oracledb.connect(user=username,password=password,dsn=servername)
cursor = connection.cursor()

endpointurl = "https://fake-json-api.mock.beeceptor.com/users"
response = rq.get(endpointurl)
print("Response Code: ",response.status_code)

if response.status_code==200:
    print("successfull")
    data = response.json()
    print("data in json :",data)

    for d in data:
        print("insert data element d ",d['country'])
      #  cursor.execute("insert into emp(empno,ename) values(:1,:2,)",(d['id'],d['name']))
        empname=d['name']
        empid= d['id']
        cursor.execute("insert into emp(empno,ename) values(:1,:2)",(empid,empname))
        connection.commit()
        print()

else:
    print("not successfull! you may check with your admin!")

