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
        empname=d['name']
        empid= d['id']
        cursor.execute("insert into Contacts (id,name,company,username,email,address,zip,state,country,phone,photo) " \
        "values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)",(d['id'],d['name'],d['company'],d['username'],d['email'],d['address'],d['zip'],d['state'],d['country'],d['phone'],d['photo']))
        connection.commit()
        print()

else:
    print("not successfull! you may check with your admin!")

