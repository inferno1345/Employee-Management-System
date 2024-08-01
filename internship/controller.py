from flask import Flask, render_template, redirect, request, flash, url_for

def acquirenewinfo():
    flag=0
    EMPID=request.form["EMPID"]
    EMPNAME=request.form["EMPNAME"]
    DESIGNATION=request.form["DESIGNATION"]
    DEPT=request.form["DEPT"]
    COMID=request.form["COMID"]
    EMPID=EMPID.upper()
    EMPNAME=EMPNAME.upper()
    DESIGNATION=DESIGNATION.upper()
    DEPT=DEPT.upper()
    COMID=COMID.upper()
    if(EMPID[0]!='E' or len(EMPID)>10):
        flag=1
        return EMPID,EMPNAME,DESIGNATION,DEPT,COMID,flag
    if(EMPNAME.isspace()==True or DESIGNATION.isspace()==True or DEPT.isspace()==True or COMID.isspace()==True):
        flag=2
        return EMPID,EMPNAME,DESIGNATION,DEPT,COMID,flag
    if(COMID[0]!='C' or len(COMID)>10):
        flag=3
        return EMPID,EMPNAME,DESIGNATION,DEPT,COMID,flag
    else:
        return EMPID,EMPNAME,DESIGNATION,DEPT,COMID,flag
    
def updatefetch():
    flag=0
    EMPNAME=request.form["EMPNAME"]
    DESIGNATION=request.form["DESIGNATION"]
    DEPT=request.form["DEPT"]
    EMPNAME=EMPNAME.upper()
    DESIGNATION=DESIGNATION.upper()
    DEPT=DEPT.upper()
    if(EMPNAME.isspace()==True or DESIGNATION.isspace()==True or DEPT.isspace()==True):
        flag=1
        return EMPNAME,DESIGNATION,DEPT,flag
    else:
        return EMPNAME,DESIGNATION,DEPT,flag