import numpy
import pandas
import statsmodels.api as sm

def custom_heuristic(file_path):
    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
    	if(passenger['Sex'] == 'female'  or (passenger['Age'] < 18 and passenger['Pclass'] ==1)):
    		predictions[passenger_id] = 1
    	elif(passenger['Sex'] == 'male' and passenger['Pclass'] > 1 and 
    	passenger['Age'] <= 9 and passenger['SibSp'] <= 2):
            predictions[passenger_id] = 1
    	else:
    		predictions[passenger_id] = 0	

    return predictions