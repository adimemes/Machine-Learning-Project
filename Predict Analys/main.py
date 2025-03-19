import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns


url = 'https://github.com/tidyverse/ggplot2/tree/main/data-raw'
diamond = pd.read_csv(url)
print(diamond.head)
