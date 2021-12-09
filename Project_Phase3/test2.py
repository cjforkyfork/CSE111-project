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

# Check variables for customer/assistant
checkS = False
checkA = False

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
        # print(req["animal_id"])
        # print('00000000000000')
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
        # print(req["donation_amount"])
        # print(req)
        # print('00000000000000')
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

@app.route("/assistant/myanimals", methods=["GET"])
def myanimals():
    if request.method == "GET":
        connection = sqlite3.connect(currentdirectory + "/animals.db")
        animals = []
        json_data = json.loads("{}")

        query = '''
        SELECT animal.animal_id, animal_type, animal_breed, animal_dob, arrival_cause, status_comment, date_enrolled
        FROM animal
            INNER JOIN status ON status.status_key = animal.status_key
            INNER JOIN animals_assistant ON animals_assistant.animal_id = animal.animal_id
            INNER JOIN shelter_assistant ON shelter_assistant.assistant_id = animals_assistant.assistant_id
        WHERE shelter_assistant.assistant_id = ?
        '''
        arg = session['user_id']
        # print("xxxxxxxxxx")
        # print(arg)
        # print("xxxxxxxxxx")

        cursor = connection.cursor()
        cursor.execute(query, arg)
        rows = cursor.fetchall()

        for i in rows:
            animals.append([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
        
        for i in animals:
            json_data.update({i[0]: {"animal_id": i[0],
                                    "animal_type": i[1], 
                                    "animal_breed": i[2], 
                                    "animal_dob": i[3],
                                    "arrival_cause": i[4],
                                    "status_comment": i[5],
                                    "date_enrolled": i[6]}
                                    })
        return json_data   


@app.route("/assistant/addvisits", methods=['GET', 'POST'])
def addvisit():
    if request.method == "POST":
        json_data = request.get_json()
        customerID = str(json_data["customer"])
        animalID = int(json_data["animal"])
        visitComment = str(json_data["comment"])
        statusKey = int(json_data["status"])


        connection = sqlite3.connect(currentdirectory + "/animals.db")
        cursor = connection.cursor()
        assistant = session['user_id']

        query = '''
        SELECT visit_key
        FROM visits
        ORDER BY visit_key DESC
        LIMIT 1
        '''
        cursor.execute(query)
        row = cursor.fetchall()
        auxVis = row[-1][0]
        auxVis += 1

        # query2 = '''
        # SELECT status_key
        # FROM animal
        # WHERE animal_id = ?
        # '''
        # arg = [animalID]
        # cursor.execute(query2, arg)
        # row2 = cursor.fetchall()
        # auxS = row2[0][0]

        insert = '''
        INSERT INTO visits
        VALUES (?, ?, ?, ?, ?)
        '''
        args = [auxVis, animalID, statusKey, assistant, visitComment]
        cursor.execute(insert, args)

        query2 = '''
        DELETE FROM requests_visits
        WHERE customer_id = ?
        '''
        arg = [customerID]
        cursor.execute(query2, arg)

        connection.commit()
        return ('', 204)
        


@app.route("/assistant/fill/<string:name>", methods=["POST", "GET"])
def fill(name):
    if request.method == "GET":
        # json_data = request.get_json() # only works with POST request
        # animalID = str(json_data["animal"])

        animal = []

        auxanimalID = int(name)
        connection = sqlite3.connect(currentdirectory + "/animals.db")
        cursor = connection.cursor()

        json_data = json.loads("{}")

        query = '''
        SELECT animal_breed, animal_dob, arrival_cause, status_key, date_enrolled
        FROM animal
        WHERE animal_id = ?
        '''
        arg = [auxanimalID]
        cursor.execute(query, arg)
        row = cursor.fetchall()

        for i in row:
            animal.append([i[0], i[1], i[2], i[3], i[4]])

        for i in animal:
            json_data.update({"animal_breed": i[0],
                                "animal_dob": i[1],
                                "arrival_cause": i[2],
                                "status_key": i[3],
                                "date_enrolled": i[4]}
                                )

        return json_data

@app.route("/assistant/editanimal", methods=["GET", "POST"])
def editanimal():
    if request.method == "POST":
        json_data = request.get_json()
        animalID = str(json_data["animalID"])
        animalBreed = str(json_data["animalBreed"])
        dob = str(json_data["dob"])
        arrivalCause = str(json_data["arrivalCause"])
        status = str(json_data["status"])
        dateEnrolled = str(json_data["dateEnrolled"])

        connection = sqlite3.connect(currentdirectory + "/animals.db")
        cursor = connection.cursor()

        query = '''
        UPDATE animal
        SET animal_breed = ?,
            animal_dob = DATE(?),
            arrival_cause = ?,
            status_key = ?,
            date_enrolled = DATE(?)
        WHERE animal_id = ?
        '''

        # print(animalID)
        args = [animalBreed, dob, arrivalCause, status, dateEnrolled, animalID]
        cursor.execute(query, args)
        connection.commit()
        return ('', 204)

@app.route("/assistant/status", methods=["GET"])
def checkstatus():
    if request.method == "GET":
        connection = sqlite3.connect(currentdirectory + "/animals.db")
        requests = []
        json_data = json.loads("{}")

        query = '''
        SELECT *
        FROM status
        '''

        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        for i in rows:
            requests.append([i[0], i[1]])

        for i in requests:
            json_data.update({i[0]: {"status": i[0],
                                    "comment": i[1]}
                                    })
        return json_data

@app.route("/assistant/requests", methods=["GET"])
def checkrequests():
    if request.method == "GET":
        connection = sqlite3.connect(currentdirectory + "/animals.db")
        requests = []
        json_data = json.loads("{}")

        query = '''
        SELECT request_id, customer_name, animal_id, customer.customer_id
        FROM requests_visits
            INNER JOIN customer ON customer.customer_id = requests_visits.customer_id,
            shelter_assistant
        WHERE shelter_assistant.assistant_id = ? AND
            animal_id IN
                    (SELECT animal_id
                    FROM animals_assistant
                    WHERE assistant_id = ?)
        '''
        arg = session['user_id']

        cursor = connection.cursor()
        cursor.execute(query, (arg, arg))
        rows = cursor.fetchall()

        for i in rows:
            requests.append([i[0], i[1], i[2], i[3]])

        for i in requests:
            json_data.update({i[0]: {"request_id": i[0],
                                    "customer_name": i[1],
                                    "animal_id": i[2],
                                    "customer_id": i[3]}
                                    })
        return json_data

@app.route("/assistant/donations", methods=["GET"])
def checkdonations():
    if request.method == "GET":
        connection = sqlite3.connect(currentdirectory + "/animals.db")
        requests = []
        json_data = json.loads("{}")

        query = '''
        SELECT DISTINCT customer_name, SUM(money)
        FROM donations
            INNER JOIN customer ON customer.customer_id = donations.customer_id
            INNER JOIN shelter_assistant ON shelter_assistant.shelter_key = donations.shelter_key
        WHERE assistant_id = ?
        '''
        arg = session['user_id']

        cursor = connection.cursor()
        cursor.execute(query, arg)
        rows = cursor.fetchall()

        for i in rows:
            requests.append([i[0], i[1]])

        for i in requests:
            j = 1
            json_data.update({i[0]: {"count": j,
                                    "customer_name": i[0],
                                    "money": i[1]}
                                    })
            j += 1
        return json_data
        
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
            # retrieves the information
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
        # Checking if global variable changed correctly
        # print("--------")
        # print(checkA)
        # print("--------")

        if checkS:
            query = '''
            SELECT customer_id, customer_name
            FROM customer 
            WHERE customer_id = ?
            '''
            args = session['user_id']
            # print('before request')
            # print(session['user_id'])
            # print(args)
            connection = sqlite3.connect(currentdirectory + "/animals.db")
            cursor = connection.cursor()
            cursor.execute(query,args)
            rows = cursor.fetchall()
            if query is None:
                query = '4'
            g.user = rows[0][1]
        elif checkA:
            query = '''
            SELECT assistant_id, assistant_name
            FROM shelter_assistant 
            WHERE assistant_id = ?
            '''

            args = session['user_id']
            connection = sqlite3.connect(currentdirectory + "/animals.db")
            cursor = connection.cursor()
            cursor.execute(query,args)
            rows = cursor.fetchall()
            g.user = rows[0][1]

@app.route('/customer')
def customer_logged():
    if not g.user:
        return redirect(url_for('login_post'))
    return render_template('customer.html')

@app.route('/assistant')
def assistant_logged():
    if not g.user:
        return redirect(url_for('login_post'))
    return render_template('assistant.html')

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

        # print(c_key)
        # print(c_name)
        # print(rows)
        # print(session['user_id'])

        cursor.execute(query,args)
        rows = cursor.fetchall()

        query2 = '''
        SELECT assistant_id, assistant_name
        FROM shelter_assistant 
        WHERE assistant_id = ?
        AND assistant_name = ?
        '''

        a_key = str(username)
        a_name = str(password)
        args2 = [a_key,a_name]

        cursor.execute(query2, args2)
        rows2 = cursor.fetchall()
        
        if rows:
            # Checks if the user is a customer
            global checkS
            checkS = True
            
            session['user_id'] = c_key
            # connection.close()
            g.user = rows[0][1]
            return redirect(url_for('customer_logged'))
        elif rows2:
            # Checks if the user is a assistant
            global checkA
            # print("Before:")
            # print(checkA)
            checkA = True
            # print("After:")
            # print(checkA)

            session['user_id'] = a_key
            g.user = rows2[0][1]
            return redirect(url_for('assistant_logged'))
        elif not rows:
                return redirect(url_for('login_post'))

    return render_template('login.html')

@app.route('/my-link/')
def my_link():
    #  pop the user fro the current session then redirect to login
    session.pop('user_id', None)
    return redirect(url_for('login_post'))

if __name__ == '__main__':
    app.run(debug=True)
    