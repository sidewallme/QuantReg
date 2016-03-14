from rpy2.robjects import pandas2ri
from rpy2.robjects import r
from rpy2 import rinterface
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage
from quantreg.qr_pogs import qr_pogs
import time
import warnings

import pandas as pd

class quantreg():
    """
    rq(formula, tau=.5, data, subset, weights, na.action,
    method="br", model = TRUE, contrasts, ...)
    """

    def __init__(self):
        pandas2ri.activate()
        r.library("quantreg")
        r.library("pogs")
        warnings.filterwarnings("ignore")
        pass

    def fit(self, X, y, tau = 0.5, method = "pogs", na_action = None):
        """
        Fit a quantile regression

        :param X:
        :param y:
        :param tau:
        :param method:
        :param na_action:
        :return:
        """
        if method == "pogs" :
            return self.fit_pogs(X, y, tau)

        formula = self.formula_generator(X, y)
        data = pd.concat([X, y.to_frame()], axis=1, join_axes=[X.index])

        t0 = time.time()
        ret = r.lm(r(formula), data = data)
        t1 = time.time()

        output = {"Coefficients":{}, "Time (s)":t1-t0}
        output["Coefficients"]["Intercept"] = ret[0][0]

        for i in range(0, len(list(X.columns.values))):
            column = list(X.columns.values)[i]
            output["Coefficients"][column] = ret[0][i+1]

        return output

    def fit_pogs(self, X, y, tau = 0.5):
        """
        Using POGS for quantile regression

        :param X: independent variables
        :param y: response variable
        :param tau: quantile
        :return: coefficients
        """
        X["Intercept"] = 1
        qr_pogs_model = qr_pogs()
        pb = SignatureTranslatedAnonymousPackage(qr_pogs_model.qr_pogs_def, "powerpack")

        t0 = time.time()
        ret = pb.qr_pogs(X= X, y =y, tau = tau)
        t1 = time.time()

        output = {"Coefficients":{}, "Time (s)":t1-t0}

        for i in range(0,len(list(X.columns.values))):
            column = list(X.columns.values)[i]
            output["Coefficients"][column] = ret[i]

        return output

    def formula_generator(self, X, y):
        """
        Generate formula string by matrix X and column y

        :param X: independent variablee
        :param y: response variable
        :return: forumla string
        """
        _independent_vars = list(X.columns.values)
        _response_vars = list(y.to_frame().columns.values)

        formula = _response_vars[0] + " ~ " + " + ".join(_independent_vars)

        return formula
