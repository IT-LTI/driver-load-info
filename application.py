from flask import Flask, render_template, request
from aws_sql import *
from constants import *
import os

application = Flask(__name__)


@application.route('/update/<string:order_id>/<string:movement_id>/<string:stop_id>/<string:tractor_id>', methods=['GET', 'POST'])
def index(order_id, movement_id, stop_id, tractor_id):
    if request.method == 'POST':
        
        trailer_id = request.form['trailer_id']
        bol_numbers = request.form.getlist('bol_number')
        weights = request.form.getlist('weight')
        pieces = request.form.getlist('pieces')

        for idx, bol_number in enumerate(bol_numbers):
            print(idx)
            unique_id = f"{stop_id}-{idx+1}"
            
            print('THIS IS THE DATABASE PASSWORD' + os.environ[DB_SECRET_PASSWORD])
            
            insert_into_bol_table(stop_id, bol_numbers[idx], weights[idx], pieces[idx], idx+1, unique_id)

        return render_template('index.html', stop_id = stop_id, order_id = order_id, movement_id = movement_id, tractor_id = tractor_id)
        #return render_template('success.html', stop_id = stop_id, order_id = order_id, movement_id = movement_id, tractor_id = tractor_id)
    
    elif request.method == 'GET':
        return render_template('index.html', stop_id = stop_id, order_id = order_id, movement_id = movement_id, tractor_id = tractor_id)
    

if __name__ == '__main__':
    application.run()
