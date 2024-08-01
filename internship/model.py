import sqlalchemy as sa
from sqlalchemy import create_engine,text
import urllib

DRIVER_NAME = "SQL SERVER"
SERVER_NAME = r"ENTER SERVER NAME FOR SQL SERVER"
DATABASE_NAME = "EMPLOYER"

connection_string = (
    "Driver={SQL Server};"
    "Server=ENTER SERVER NAME FOR SQL SERVER"
    "Database=EMPLOYER;"
    "Trusted_Connection=yes;"
)
connection_url = urllib.parse.quote_plus(connection_string)

coxn = create_engine(f"mssql+pyodbc:///?odbc_connect={connection_url}")
print("Connection passed")

def acquire(mssqltips=[]):
    with coxn.connect() as connection:
        result = connection.execute(text("SELECT EMP_ID, EMP_NAME, DESIGNATION, DEPT FROM EMPLOYEE"))
        for row in result.fetchall():
            mssqltips.append({
                "EMPID": row[0], 
                "EMPNAME": row[1], 
                "DESIGNATION": row[2], 
                "DEPT": row[3],
            })
    return mssqltips
def count(EMPID,COMID):
    conn=coxn.raw_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM EMPLOYEE WHERE EMP_ID=?",EMPID)
    result=cursor.fetchone()
    cursor.execute("SELECT COUNT(*) FROM EMPLOYEE WHERE COM_ID=?",COMID)
    result1=cursor.fetchone()
    cursor.close()
    conn.close()
    return result, result1
def insert(EMPID,EMPNAME,DESIGNATION,DEPT,COMID):
    conn=coxn.raw_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO EMPLOYER.dbo.EMPLOYEE (EMP_ID, EMP_NAME, DESIGNATION, DEPT, COM_ID) VALUES (?,?,?,?,?)",(EMPID,EMPNAME,DESIGNATION,DEPT,COMID))
    cursor.commit()
    cursor.close()
    conn.close()
    return
def fetch(cr=[],id=""):
    conn=coxn.raw_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM EMPLOYER.dbo.EMPLOYEE WHERE EMP_ID=?",id)
    for row in cursor.fetchall():
        cr.append({"EMPID":row[0],"EMPNAME":row[1],"DESIGNATION":row[2],"DEPT":row[3],"COMID":row[4]})
    conn.close()
    return cr
def updation(EMPNAME="",DESIGNATION="",DEPT="",id=""):
    conn=coxn.raw_connection()
    cursor=conn.cursor()
    cursor.execute("UPDATE EMPLOYER.dbo.EMPLOYEE SET EMP_NAME=?, DESIGNATION=?, DEPT=? WHERE EMP_ID=?",EMPNAME,DESIGNATION,DEPT,id)
    cursor.execute("UPDATE EMPLOYER.dbo.EMPLOYEE SET DEPT=? WHERE EMP_ID=?", DEPT,id)
    conn.commit()
    conn.close()
    return
def deletion(id=""):
    conn=coxn.raw_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM EMPLOYER.dbo.COMMUNICATION WHERE EMP_ID=?",id)
    cursor.execute("DELETE FROM EMPLOYER.dbo.PROJECT_SALARY WHERE EMP_ID=?",id)
    cursor.execute("DELETE FROM EMPLOYER.dbo.EMPLOYEE WHERE EMP_ID=?",id)
    conn.commit()
    conn.close()
    return
