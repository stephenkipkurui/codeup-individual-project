
    
# Import main libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from acquire import get_police_shootings_data
from prepare import prepare_police_shootings_data, prepare_modeling_data
from sklearn.model_selection import train_test_split
import tabulate

# Import classification modules
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Stats libraries
import statsmodels.api as sm
import scipy.stats as stats


# plotting defaults
plt.rc('figure', figsize=(13, 5))
plt.style.use('seaborn-whitegrid')
plt.rc('font', size=16)

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Set alpha /confidence level 
alpha = 0.05