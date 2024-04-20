import pandas as pd
from flask import Flask, request, jsonify
import joblib
import psycopg2 
import json




app = Flask(__name__)
model = joblib.load('iris_model.pkl')



@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"

def get_students():
    conn = psycopg2.connect(database="dpu_database",
                            user="postgres",
                            host='localhost',
                            password="admin",
                            port=5432)
    cur = conn.cursor()
    cur.execute('SELECT * FROM public.studens_new ORDER BY id ASC;')
    rows = cur.fetchall()
    conn.close()
    return rows
@app.route('/All_result', methods=['GET'])
def getData():
    students = get_students()
    student_list = []
    for student in students:
        student_dict = {
            'ID': student[0],
            'Name': student[1],
            'Sex': student[2]
        }
        student_list.append(student_dict)
    response = {
        "status": "200",
        "message": "success",
        "data": student_list
    }

    return jsonify(response)



def create_student(name, last_name):
    conn = psycopg2.connect(database="dpu_database",
                            user="postgres",
                            host='localhost',
                            password="admin",
                            port=5432)
    cur = conn.cursor()
    cur.execute('INSERT INTO public.studens_new (name, last_name) VALUES (%s, %s)', (name, last_name))
    conn.commit()
    conn.close()

def update_student(id, name, last_name):
    conn = psycopg2.connect(database="dpu_database",
                            user="postgres",
                            host='localhost',
                            password="admin",
                            port=5432)
    cur = conn.cursor()
    cur.execute('UPDATE public.studens_new SET name = %s, last_name = %s WHERE id = %s', (name, last_name, id))
    conn.commit()
    conn.close()


    
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        sepal_length = data['Sepal length']
        sepal_width = data['Sepal width']
        petal_length = data['Petal length']
        petal_width = data['Petal width']
        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
        
        return jsonify({'predicted_species': prediction})
    except Exception as e:
        return jsonify({'error': 'Prediction error: ' + str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True , port = 8000)