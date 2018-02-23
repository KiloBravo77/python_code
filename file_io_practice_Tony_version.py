import csv
import pyodbc
emails = dict()
prog_name_id_list = []
ids = {}
found = False
def validate_name(id,program_name):
    if id == "PK":
        print "invalid id"
        return    
    with pyodbc.connect("Driver=SQL Server;SERVER=192.168.100.97;DATABASE=clincard;UID=ETL_User;PWD=jJk9O1snsN8DaCsjXi6z") as c:

        rs = c.execute("select id,name from core_program where id={}".format(id))

        for x in rs:
            if x[1] != program_name:
                print "{} is db name {} is in the file, does not match!".format(row[1],program_name)

                
if __name__ == "__main__":                
    with open("in.csv","rb") as file:
        read = csv.reader(file, delimiter="|")
        for row in read:
            
            if row[0]  not in emails.keys():
                emails[row[0]] = []
                ids[row[0]] = row[1]
            else:
                if ids[row[0]] != row[1]:
                    print "DUPLICATE KEY FOR {} and {}".format(ids[row[0]],row[1])
                    found = True
            emails[row[0]].append(row[4])
            validate_name(row[0],row[1])


    if not found:
        with open("out.txt","w") as o:
            for x in emails.keys():
                o.write(";".join(emails[x])+'\n')
    else:
        print "please fix the duplicates before you move forward"