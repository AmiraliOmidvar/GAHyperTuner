import numpy as np
from exceptions import GaParamsException, MParamsException


class GaHypertuner:
    default_ga_parameters = {"pop_size": 20, "fscale": 0.5, "gmax": 50, "stop_value": 0.99, "direction": "max",
                             "cp": 0.5}

    def tune(self, ga_parameters: dict, model_parameters: dict
                 , boundaries: dict):
        self._check_ga_params(ga_parameters)
        self._check_m_parameters(model_parameters, boundaries)
        # self._check_ga_hypertuner_parameters(stop_criteria, stop_value, verbosity, stratified, show_progress_plot)

    @staticmethod
    def _check_ga_params(ga_parameters):
        ga_parameters_range = {"pop_size": [5, np.Inf], "fscale": [0, np.inf], "gmax": [1, np.Inf],
                               "direction": ["min", "max"], "cp": [0, 1]}
        for k in list(ga_parameters.keys()):
            r = ga_parameters_range[k]
            if k != "direction":
                if type(ga_parameters[k]) is not int and type(ga_parameters[k]) is not float:
                    raise GaParamsException(GaParamsException.PARAMETER_WRONG_TYPE, k, "int or float")
                if not r[0] < ga_parameters[k] < r[1]:
                    raise GaParamsException(GaParamsException.PARAMETER_OUT_OF_RANGE, k, str(r))
            else:
                if ga_parameters["direction"] != "max" and ga_parameters["direction"] != "min":
                    raise GaParamsException(GaParamsException.PARAMETER_OUT_OF_RANGE, k, str(r))

        if "pop_size" not in list(ga_parameters.keys()):
            raise GaParamsException(GaParamsException.PARAMETER_SHOULD_EXIST, "pop_size")
        if "fscale" not in list(ga_parameters.keys()):
            raise GaParamsException(GaParamsException.PARAMETER_SHOULD_EXIST, "fscale")
        if "gmax" not in list(ga_parameters.keys()):
            raise GaParamsException(GaParamsException.PARAMETER_SHOULD_EXIST, "gmax")
        if "direction" not in list(ga_parameters.keys()):
            raise GaParamsException(GaParamsException.PARAMETER_SHOULD_EXIST, "direction")
        if "cp" not in list(ga_parameters.keys()):
            raise GaParamsException(GaParamsException.PARAMETER_SHOULD_EXIST, "cp")

    @staticmethod
    def _check_m_parameters(model_parameters, boundaries):
        if set(model_parameters) != set(boundaries):
            raise MParamsException(MParamsException.KEYS_NOT_EQUAL)

        for k in list(boundaries.keys()):
            if len(boundaries[k]) != 2:
                raise MParamsException(MParamsException.BOUNDARY_VALUE, k)

        for k in list(model_parameters.keys()):
            if len(model_parameters[k]) != 2:
                raise MParamsException(MParamsException.PARAMETER_WRONG_FORMAT, k)
            if type(model_parameters[k]) != list:
                raise MParamsException(MParamsException.PARAMETER_WRONG_FORMAT, k)
            if type(model_parameters[k][1]) != type:
                raise MParamsException(MParamsException.PARAMETER_WRONG_FORMAT, k)
            if model_parameters[k][0] is not None and type(model_parameters[k][0]) != model_parameters[k][1]:
                raise MParamsException(MParamsException.PARAMETER_WRONG_FORMAT, k)

    @staticmethod
    def _check_ga_hypertuner_parameters(stop_criteria, stop_value, verbosity, stratified, show_progress_plot):
        if type(stop_criteria) != bool:
            raise GaHypertunerParamException("stop_criteria", "bool")
        if type(stop_value) != float:
            raise GaHypertunerParamException("stop_value", "float")
        if type(verbosity) != int:
            raise GaHypertunerParamException("verbosity", "int")
        if type(stratified) != bool:
            raise GaHypertunerParamException("stratified", "bool")
        if type(show_progress_plot) != bool:
            raise GaHypertunerParamException("show_progress_plot", "bool")


ga_hypertuner = GaHypertuner()
mp = {"eta": [1.0, float], "min_child_weight": [None, float], "colsample_bytree": [None, float],
      "n_estimators": [None, int], "alpha": [None, float], "gamma": [None, float]}
b = {"eta": [0, 1], "min_child_weight": [0, 5], "colsample_bytree": [0, 1],
      "n_estimators": [100, 1000], "alpha": [0,-1], "gamma": [0, 1]}
ga_hypertuner.tune({"pop_size": 20, "fscale": 1.5, "gmax": 50, "direction": "max", "cp": 0.5}, mp, b)