from flask import Flask, render_template, redirect, request, flash,url_for
from model import acquire,count,insert,fetch,updation,deletion
from controller import acquirenewinfo, updatefetch
app = Flask(__name__)
app.secret_key="Hello World"
temp=None
@app.route("/") 
def base():
    mssqltips = []
    acquire(mssqltips)
    return render_template("base.html", mssqltips=mssqltips)
@app.route("/addemp", methods=['GET','POST'])
def addemp():
    if request.method=='GET':
        return render_template("Add.html")
    if request.method=='POST':
        EMPID,EMPNAME,DESIGNATION,DEPT,COMID,flag=acquirenewinfo()
        if(flag==1):
            flash("The EMPID filled in is incorrect please start with character E and make sure it doesn't exceed 10 characters")
            return redirect('/addemp')
        if(flag==2):
            flash("Please don't fill the text boxes just with blank spaces")
            return redirect('/addemp')
        if(flag==3):
            flash("The COMID filled in is incorrect please start with character C and make sure it doesn't exceed 10 characters")
            return redirect('/addemp')
        result,result1=count(EMPID,COMID)
        if(result[0]>0):
            flash("The entered EmpID is currently in use please try another EmpID")
            return redirect('/addemp')
        elif(result1[0]>0):
            flash("Entered COMID already exists please try a different one")
            return redirect('/addemp')
        else:
            insert(EMPID,EMPNAME,DESIGNATION,DEPT,COMID)
            return redirect('/')
@app.route('/updatemp/<string:id>',methods=['GET','POST'])
def update(id):
    cr=[]
    if request.method=='GET':
        fetch(cr,id)
        return render_template("update.html",tip=cr[0])
    if request.method=='POST':
        EMPNAME,DESIGNATION,DEPT,flag=updatefetch()
        if(flag==1):
            flash("Please don't fill the text boxes just with blank spaces")
            return redirect('/')
        updation(EMPNAME,DESIGNATION,DEPT,id)
        return redirect('/')
@app.route("/go_to_popup-box/<string:id>")
def popup(id):
    global temp
    temp=id
    return redirect(url_for('base')+'#popup-box')
@app.route('/delemp')
def delete():
    deletion(temp)
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)
