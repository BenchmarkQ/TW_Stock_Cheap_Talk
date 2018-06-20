import hmmlearn.hmm import GaussianHMM
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

n = 3 #suppose three states
dl = bk.DataLoader()
data = dl.get_stock_data('0050', 2005, 1)


