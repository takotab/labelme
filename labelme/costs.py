import json
from pathlib import Path
import numpy as np


def ifnone(a, b):
    return a if a is not None else b

class Cost(Object):
    def __init__(self,path=None, aanames=None):
    path = ifnone(path, Path("data/"))
    aanames = ifnone(aanames, json.load(open(path / "aannames.json", "r")))

    def calc_costs(self, data=None):
        if data is None:
            data = json.load(open(list(path.glob("*.json"))[0], "r"))
        for shape in data["shapes"]:
            if shape["label"] in self.aanames:
                self._calc_cols_shape(shape)


    def _calc_cols_shape(self, shape):
        length = calc_length(*shape["points"])
        cost_p_lenght = get_cost_p_lenght(shape["label"], get_true_key(shape["flags"]))

    def get_cost_p_lenght(self, label, flag):
        return self.aanames[label][flag]



def get_true_key(dct: dict, i=0):
    return [k for k, v in dct.items() if v][0]

def calc_length(a, b):
    return np.numpy.linalg.norm(np.array(a) - np.array(b))


if __name__ == "__main__":
    Cost().calc_costs()
