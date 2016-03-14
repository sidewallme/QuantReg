QuantReg 
=========

a Python library that makes it easy to access and parse data from quantreg in R programming language.

**Installation**

.. code:: python

  >>> from quantreg.qr import quantreg
  >>> import statsmodels.api as sm
  >>> import pandas as pd
  
  >>> data = pd.DataFrame(sm.datasets.engel.load_pandas().data)
  >>> qr_model = quantreg()
  >>> fit = qr_model.fit_pogs(data[['foodexp', ]], data['income'], 0.3)
  >>> print(fit)
  # {'Coefficients': {'Intercept': 11.195980483128324, 'foodexp': 1.378005107774296}, 'Time (s)': 0.01637101173400879}
  
**Documentation**

**License**

**Credit**

