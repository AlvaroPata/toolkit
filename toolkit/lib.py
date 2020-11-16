# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for toolkit Project
"""

from os.path import split
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import requests
from sklearn.compose import TransformerMixin, BaseEstimator

def fetch_url(url):
    '''returns url as df'''
    response = requests.get(url).json()
    return pd.DataFrame(response)

