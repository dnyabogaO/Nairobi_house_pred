import json
import pickle
import numpy as np


__locations = None
__data_columns = None
__model = None

def get_estimated_price(Region,Bedrooms,Bathrooms,total_sqft):
    try:
        loc_index = __data_columns.index(Region.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Bedrooms
    x[1] = Bathrooms
    x[2] = total_sqft
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)


def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artefact/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open("./artefact/nairobi_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts ...done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Brookside',2,2,600))
    print(get_estimated_price('Imara Daima', 2, 2, 600))
    print(get_estimated_price('Riruta', 2, 2, 600))
    print(get_estimated_price('Kinoo', 2, 2, 600))