from sqlite3.dbapi2 import connect
from flask import Flask, render_template, jsonify, request, redirect, session, g
import sqlite3
import os
from flask.helpers import url_for
from flask_restful import Api, Resource
from distutils.log import error
import json

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

app.secret_key = 'TEAM111'

api = Api(app)

@app.route("/customer/getOutcome/<string:name>",methods = ["GET"])
def out(name):
    if request.method == "GET":
        animal_id = int(name)
        connection = sqlite3.connect(currentdirectory + "/animals.db")
        cursor = connection.cursor()
        query_outcome = '''
        SELECT status_comment
        FROM status, animal
        WHERE animal.status_key = status.status_key
        AND animal.animal_id = ?
        '''
        args = [animal_id]
        cursor.execute(query_outcome,args)
        rows = cursor.fetchall()

        animal_outcome = rows[0][0]
        outcome = jsonify({name:animal_outcome})
        return outcome

@app.route("/student/requestVisit",methods = ["POST"])
def get():
    if request.method == "POST":
        connection = sqlite3.connect(currentdirectory + "/animals.db")
        cursor = connection.cursor()
        query = '''
        SELECT *
        FROM requests_visits
        '''
        cursor.execute(query)
        rows = cursor.fetchall()
        visit_id = rows[-1][0]
        visit_id = visit_id + 1

        req = request.get_json()
        print(req["animal_id"])
        print('00000000000000')
        an_id = int(req["animal_id"])
        cust_id = str(session['user_id'])

        query_request = '''
        INSERT INTO requests_visits VALUES(?,?,?);
        '''
        args = [visit_id,cust_id,an_id]

        cursor.execute(query_request,args)
        connection.commit()
        return ('', 204)
        
@app.route("/customer/makeDonation",methods = ["POST"])
def donate():
    if request.method == "POST":
        connection = sqlite3.connect(currentdirectory + "/animals.db")
        cursor = connection.cursor()

        query = '''
        SELECT *
        FROM donations
        '''
        cursor.execute(query)
        rows = cursor.fetchall()
        donation_id = rows[-1][0]
        donation_id = donation_id + 1

        req = request.get_json()
        print(req["donation_amount"])
        print('00000000000000')
        donation_amount = int(req["donation_amount"])
        cust_id = str(session['user_id'])

        query_shelter = '''
        SELECT shelter_key
        FROM shelter,customer       
        WHERE customer.customer_id = ?
        AND customer.city_key = shelter.city_key
        '''
        args_shelter = [cust_id]

        cursor.execute(query_shelter,args_shelter)

        rows_2 = cursor.fetchall()
        shelter_id = rows_2[0][0]

        query_donation = '''
        INSERT INTO donations VALUES(?,?,?,?);
        '''
        args = [donation_id,cust_id,shelter_id,donation_amount]

        cursor.execute(query_donation,args)
        connection.commit()
        return ('', 204)

class currDogs(Resource):
    def get(self):
        if 'user_id' in session:
            query_animal = '''
            SELECT animal_id,animal_type,animal_breed,animal_dob,animal.shelter_key,arrival_cause,status_key,date_enrolled
            FROM animal,customer,shelter
            WHERE customer_id = ?
            AND customer.city_key = shelter.city_key
            AND animal.shelter_key = shelter.shelter_key
            AND animal_type = 'Dog'
            '''
            args = session['user_id']
            connection = sqlite3.connect(currentdirectory + "/animals.db")
            cursor = connection.cursor()
            cursor.execute(query_animal,args)
            rows = cursor.fetchall()
            list_animals = []
            # retrieve all classes for the given student
            for cls in rows:
                list_animals.append([cls[0], cls[1], cls[2],cls[3],cls[4],cls[5],cls[6],cls[7]])
            json_data = json.loads("{}")

            # this is formatting the data to be sent out
            for cls in list_animals:
                num = 1
                json_data.update({cls[0]: {"animal_id": cls[0],
                                           "animal_breed": cls[2], 
                                           "animal_dob": cls[3], 
                                           "date_enrolled": cls[7]}})
                num += 1
            return json_data
        return error(400)

class currCats(Resource):
    def get(self):
        if 'user_id' in session:
            query_animal = '''
            SELECT animal_id,animal_type,animal_breed,animal_dob,animal.shelter_key,arrival_cause,status_key,date_enrolled
            FROM animal,customer,shelter
            WHERE customer_id = ?
            AND customer.city_key = shelter.city_key
            AND animal.shelter_key = shelter.shelter_key
            AND animal_type = 'Cat'
            '''
            args = session['user_id']
            connection = sqlite3.connect(currentdirectory + "/animals.db")
            cursor = connection.cursor()
            cursor.execute(query_animal,args)
            rows = cursor.fetchall()
            list_animals = []
            # retrieve all classes for the given student
            for cls in rows:
                list_animals.append([cls[0], cls[1], cls[2],cls[3],cls[4],cls[5],cls[6],cls[7]])
            json_data = json.loads("{}")

            # this is formatting the data to be sent out
            for cls in list_animals:
                num = 1
                json_data.update({cls[0]: {"animal_id": cls[0],
                                           "animal_breed": cls[2], 
                                           "animal_dob": cls[3], 
                                           "date_enrolled": cls[7]}})
                num += 1
            return json_data
        return error(400)

class underFive(Resource):
    def get(self):
        if 'user_id' in session:
            query_animal = '''
            SELECT animal_id,animal_type,animal_breed,animal_dob,animal.shelter_key,arrival_cause,status_key,date_enrolled
            FROM animal,customer,shelter
            WHERE customer_id = ?
            AND customer.city_key = shelter.city_key
            AND animal.shelter_key = shelter.shelter_key
            AND strftime('%Y',animal_dob) > '2016-12-04'
            '''
            args = session['user_id']
            connection = sqlite3.connect(currentdirectory + "/animals.db")
            cursor = connection.cursor()
            cursor.execute(query_animal,args)
            rows = cursor.fetchall()
            list_animals = []
            # retrieve all classes for the given student
            for cls in rows:
                list_animals.append([cls[0], cls[1], cls[2],cls[3],cls[4],cls[5],cls[6],cls[7]])
            json_data = json.loads("{}")

            # this is formatting the data to be sent out
            for cls in list_animals:
                num = 1
                json_data.update({cls[0]: {"animal_id": cls[0],
                                           "animal_type": cls[1],
                                           "animal_breed": cls[2], 
                                           "animal_dob": cls[3], 
                                           "date_enrolled": cls[7]}})
                num += 1
            return json_data
        return error(400)

class overFive(Resource):
    def get(self):
        if 'user_id' in session:
            query_animal = '''
            SELECT animal_id,animal_type,animal_breed,animal_dob,animal.shelter_key,arrival_cause,status_key,date_enrolled
            FROM animal,customer,shelter
            WHERE customer_id = ?
            AND customer.city_key = shelter.city_key
            AND animal.shelter_key = shelter.shelter_key
            AND strftime('%Y',animal_dob) < '2016-12-04'
            '''
            args = session['user_id']
            connection = sqlite3.connect(currentdirectory + "/animals.db")
            cursor = connection.cursor()
            cursor.execute(query_animal,args)
            rows = cursor.fetchall()
            list_animals = []
            # retrieve all classes for the given student
            for cls in rows:
                list_animals.append([cls[0], cls[1], cls[2],cls[3],cls[4],cls[5],cls[6],cls[7]])
            json_data = json.loads("{}")

            # this is formatting the data to be sent out
            for cls in list_animals:
                num = 1
                json_data.update({cls[0]: {"animal_id": cls[0],
                                           "animal_type": cls[1],
                                           "animal_breed": cls[2], 
                                           "animal_dob": cls[3], 
                                           "date_enrolled": cls[7]}})
                num += 1
            return json_data
        return error(400)
    
api.add_resource(currDogs, '/customer/currDogs')
api.add_resource(currCats, '/customer/currCats')
api.add_resource(underFive, '/customer/underFive')
api.add_resource(overFive, '/customer/overFive')


# api.add_resource(requestVisits, '/student/requestVisit')


@app.before_request
def before_request():
    g.user = None
    # session.pop('user_id', None)
    if 'user_id' in session:
        query = '''
        SELECT customer_id, customer_name
        FROM customer 
        WHERE customer_id = ?
        '''
        args = session['user_id']
        print('before request')
        print(session['user_id'])
        print(args)
        connection = sqlite3.connect(currentdirectory + "/animals.db")
        cursor = connection.cursor()
        cursor.execute(query,args)
        rows = cursor.fetchall()
        if query is None:
            query = '4'
        g.user = rows[0][1]

@app.route('/customer')
def customer_logged():
    if not g.user:
        return redirect(url_for('login_post'))
    return render_template('customer.html')

@app.route("/")
def main():
    return render_template("login.html")

@app.route('/', methods=['GET', 'POST'])
def login_post():
    if request.method == 'POST':
        # session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        connection = sqlite3.connect(currentdirectory + "/animals.db")
        cursor = connection.cursor()
        query = '''
        SELECT customer_id, customer_name
        FROM customer 
        WHERE customer_id = ?
        AND customer_name = ?
        '''
        c_key = str(username)
        c_name = str(password)
        
        args = [c_key,c_name]

        cursor.execute(query,args)
        rows = cursor.fetchall()
        
        print(c_key)
        print(c_name)
        print(rows)
        # print(session['user_id'])
        if not rows:
                return redirect(url_for('login_post'))
        else:
            session['user_id'] = c_key
            # connection.close()
            g.user = rows[0][1]
            return redirect(url_for('customer_logged'))

        query2 = '''
        SELECT assistant_id, assistant_name
        FROM shelter_assistant 
        WHERE assistant_id = ?
        AND assistant_name = ?
        '''
        a_key = str(username)
        a_name = str(password)

        args2 = [a_key,a_name]
        cursor.execute(query2,args2)
        rows2 = cursor.fetchall()
        if rows2[0][0] == None and rows2[0][1] == None:
                print("There are no results for this query")
        else:
            print("TRUE")
    return render_template('login.html')

@app.route('/my-link/')
def my_link():
    #  pop the user fro the current session then redirect to login
    session.pop('user_id', None)
    return redirect(url_for('login_post'))

if __name__ == '__main__':
    app.run(debug=True)
    