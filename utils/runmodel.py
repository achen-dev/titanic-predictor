import numpy
from joblib import dump, load
from sklearn.naive_bayes import CategoricalNB

MODEL = "../cnbmodel"


def runmodel(inputdict):
    model = load(MODEL)
    predictions = model.predict_proba([[1,0,0,1,2,0,0]])
    survivalchance = str(predictions[0][1])[:5]
    return "Your chances of survival is " + survivalchance + " %"


if __name__ == "__main__":
    print(runmodel("1"))