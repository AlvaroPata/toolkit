# -*- coding: UTF-8 -*-

# Import from standard library
import os
import toolkit
import pandas as pd
# Import from our lib
from toolkit.lib import *
import pytest

def test_fetch_url():
    url = 'http://iex.lewagon.com/stable/stock/'
    assert type(fetch_url(url)) == 'pandas.core.frame.DataFrame'