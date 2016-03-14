import pandas as pd
import statsmodels.api as sm
from quantreg.qr import quantreg

data = pd.DataFrame(sm.datasets.engel.load_pandas().data)
qr_model = quantreg()
qr_model.fit_pogs(data[['foodexp', ]], data['income'], 0.3)