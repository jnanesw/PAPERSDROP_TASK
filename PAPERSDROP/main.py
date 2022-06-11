
"""No data is there to share.Just entered the Random values"""

from flask import Flask,request,jsonify
from mongoengine import *
app=Flask(__name__)

client=connect(db="PAPERSDROP", username='JnaneswarRao', password='MongoDb', host='mongodb+srv://JnaneswarRao:MongoDb@cluster0.b16ec.mongodb.net/?retryWrites=true&w=majority')

db1=client["PAPERSDROP"]
coll1=db1["books"]

class Books(Document):
    Book_Name=StringField(required=True)
    Author=StringField()
    Language=StringField(required=True)
    Pages=IntField()
    Country=StringField()
    Year=IntField(required=True)

    def insert(Book_Name,Author,Language,Pages,Country,Year):
        a=Books()
        a.Book_Name=Book_Name
        a.Author = Author
        a.Language=Language
        a.Pages=Pages
        a.Country=Country
        a.Year=Year
        a.save()

@app.route("/AddNewBook",methods=["POST"])
def AddNewBook():
    if(request.method=="POST"):
        Book_Name=request.json["Book_Name"]
        Author=request.json["Author"]
        Language=request.json["Language"]
        Pages=request.json["Pages"]
        Country=request.json["Country"]
        Year=request.json["Year"]
        Books.insert(Book_Name,Author,Language,Pages,Country,Year)
        return jsonify(str({"Successfully Inserted Documnet of the book : ", Book_Name}))

@app.route("/BookDetails",methods=["GET"])
def BookDetails():
    if(request.method=="GET"):
        Details=[]
        for i in coll1.find({}):
            Details.append(i)
        return jsonify(str(Details))



@app.route("/UpdateBook",methods=["POST"])
def UpdateBook():
    Book_Name=request.json["Book_Name"]
    Author=request.json["Author"]

    new_Book_Name = request.json["new_Book_Name"]
    new_Author=request.json["new_Author"]
    new_Language=request.json["new_Language"]
    new_Pages_No=request.json["new_Pages_No"]
    new_Country=request.json["new_Country"]
    new_Year=request.json["new_Year"]
    Books.insert(new_Book_Name,new_Author,new_Language,new_Pages_No,new_Country,new_Year)
    coll1.find_one_and_delete({"Book_Name": Book_Name, "Author": Author})
    return jsonify(str({"Successfully Updated"}))

@app.route("/DeleteBooks",methods=["POST"])
def DeleteBooks():
    Book_Name=request.json["Book_Name"]
    Author=request.json["Author"]
    for i in coll1.find():
        if(i["Book_Name"]==Book_Name and i["Author"]==Author):
            coll1.find_one_and_delete({"Book_Name":Book_Name,"Author":Author})
    return jsonify(str({"Successfully deleted the details of the {} book".format(Book_Name)}))


if(__name__=="__main__"):
    app.run()


