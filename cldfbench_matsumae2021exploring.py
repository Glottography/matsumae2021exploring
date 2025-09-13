import pathlib

import pyglottography


class Dataset(pyglottography.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "matsumae2021exploring"
