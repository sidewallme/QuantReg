QuantReg 
=========

A Python wrapper for quantreg in R programming language.

Installation
------------

Example
------------

.. code:: python

  >>> from quantreg.qr import quantreg
  >>> import statsmodels.api as sm
  >>> import pandas as pd
  
  >>> data = pd.DataFrame(sm.datasets.engel.load_pandas().data)
  >>> qr_model = quantreg()
  >>> fit = qr_model.fit_pogs(data[['foodexp', ]], data['income'], tau = 0.3)
  >>> print(fit)
  # {'Coefficients': {'Intercept': 11.195980483128324, 'foodexp': 1.378005107774296}, 'Time (s)': 0.01637101173400879}
  
Documentation
------------

Read the docs at https://cran.r-project.org/web/packages/quantreg/quantreg.pdf

-  `POGS <https://github.com/foges/pogs>`__

.. code:: python

  >>> # to use pogs, add method = "pogs" parameter
  >>> fit = qr_model.fit_pogs(data[['foodexp', ]], data['income'], tau = 0.3, method = "pogs")
  
License
------------

Credit
------------

