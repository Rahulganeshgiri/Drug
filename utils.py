import pickle
import numpy as np
import sklearn 

def get_predict(Age , Sex, BP, Cholesterol, Na_to_K):
    with open('Drug.pkl','rb') as f:
        model = pickle.load(f)

    test_array = np.array([[Age , Sex, BP, Cholesterol, Na_to_K]])

    predicted_drug = model.predict(test_array)
    print("change for git")
    print("one more")

    return predicted_drug