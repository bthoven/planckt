# -*- coding: utf-8 -*-
"""
Contains the Planck's 2018 results for the base-LCDM model from table 2 of
arXiv:1807.06209.

"""

__all__ = ["Planck18Param"]
__author__ = "Beethoven Santos (thovensantos@gmail.com)"
__version__ = "18.12.01"


class Planck18Param(object):

    """Class for the Planck params."""

    def __init__(self, name, analysis):
        self.name = name
        self.analysis = analysis
        self.units = planck_2018_LCDM_dict[name]["units"]
        self.value = planck_2018_LCDM_dict[name][analysis]["value"]
        limits68 = planck_2018_LCDM_dict[name][analysis]["limits68"]
        if str(limits68[0]) == str(limits68[1]):
            self.limit68 = limits68[0]
        else:
            self.limit68 = limits68
            print("ATENTION: The inferior and superior 68% limits are not "
                  "equal. Please treat them with caution.")


# Here are some conventions applied to the names of the keys describing the
# variables:
#
# - A multiplication signal between two variables is showed by a double
#   underscore "__". There is no multiplication symbol between a number and a
#   variable.
# - Superscripts are separated from the variable by the symbol "^" unless the
#   superscript is a number. In that case, the number and the variable are
#   joined together.
# - Subscripts are separated from the variable single underscores "_".
# - 68% limits are showed in the form [inferior, superior].
#
planck_2018_LCDM_dict = {
    "Omega_b__h2": {
        "TT+lowE": {"value": 0.02212, "limits68": [0.00022, 0.00022]},
        "TE+lowE": {"value": 0.02249, "limits68": [0.00025, 0.00025]},
        "EE+lowE": {"value": 0.0240, "limits68": [0.0012, 0.0012]},
        "TT,TE,EE+lowE": {"value": 0.02236, "limits68": [0.00015, 0.00015]},
        "TT,TE,EE+lowE+lensing": {"value": 0.02237,
                                  "limits68": [0.00015, 0.00015]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.02242,
                                      "limits68": [0.00014, 0.00014]},
        "units": "adimensional"
    },

    "Omega_c__h2": {
        "TT+lowE": {"value": 0.1206, "limits68": [0.0021, 0.0021]},
        "TE+lowE": {"value": 0.1177, "limits68": [0.002, 0.002]},
        "EE+lowE": {"value": 0.1158, "limits68": [0.0046, 0.0046]},
        "TT,TE,EE+lowE": {"value": 0.1202, "limits68": [0.0014, 0.0014]},
        "TT,TE,EE+lowE+lensing": {"value": 0.12, "limits68": [0.0012, 0.0012]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.11933,
                                      "limits68": [0.00091, 0.00091]},
        "units": "adimensional"
    },

    "100theta_MC": {
        "TT+lowE": {"value": 1.04077, "limits68": [0.00047, 0.00047]},
        "TE+lowE": {"value": 1.04139, "limits68": [0.00049, 0.00049]},
        "EE+lowE": {"value": 1.03999, "limits68": [0.00089, 0.00089]},
        "TT,TE,EE+lowE": {"value": 1.0409, "limits68": [0.00031, 0.00031]},
        "TT,TE,EE+lowE+lensing": {"value": 1.04092,
                                  "limits68": [0.00031, 0.00031]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 1.04101,
                                      "limits68": [0.00029, 0.00029]},
        "units": "adimensional"
    },

    "tau": {
        "TT+lowE": {"value": 0.0522, "limits68": [0.008, 0.008]},
        "TE+lowE": {"value": 0.0496, "limits68": [0.0085, 0.0085]},
        "EE+lowE": {"value": 0.0527, "limits68": [0.009, 0.009]},
        "TT,TE,EE+lowE": {"value": 0.0544, "limits68": [0.0081, 0.007]},
        "TT,TE,EE+lowE+lensing": {"value": 0.0544,
                                  "limits68": [0.0073, 0.0073]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.0561,
                                      "limits68": [0.0071, 0.0071]},
        "units": "adimensional"
    },

    "ln(10^10A_s)": {
        "TT+lowE": {"value": 3.040, "limits68": [0.016, 0.016]},
        "TE+lowE": {"value": 3.018, "limits68": [0.018, 0.02]},
        "EE+lowE": {"value": 3.052, "limits68": [0.022, 0.022]},
        "TT,TE,EE+lowE": {"value": 3.045, "limits68": [0.016, 0.016]},
        "TT,TE,EE+lowE+lensing": {"value": 3.044, "limits68": [0.014, 0.014]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 3.047,
                                      "limits68": [0.014, 0.014]},
        "units": "adimensional"
    },

    "n_s": {
        "TT+lowE": {"value": 0.9626, "limits68": [0.0057, 0.0057]},
        "TE+lowE": {"value": 0.967, "limits68": [0.011, 0.011]},
        "EE+lowE": {"value": 0.980, "limits68": [0.015, 0.015]},
        "TT,TE,EE+lowE": {"value": 0.9649, "limits68": [0.0044, 0.0044]},
        "TT,TE,EE+lowE+lensing": {"value": 0.9649,
                                  "limits68": [0.0042, 0.0042]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.9665,
                                      "limits68": [0.0038, 0.0038]},
        "units": "adimensional"
    },

    "H_0": {
        "TT+lowE": {"value": 66.88, "limits68": [0.92, 0.92]},
        "TE+lowE": {"value": 68.44, "limits68": [0.91, 0.91]},
        "EE+lowE": {"value": 69.9, "limits68": [2.7, 2.7]},
        "TT,TE,EE+lowE": {"value": 67.27, "limits68": [0.6, 0.6]},
        "TT,TE,EE+lowE+lensing": {"value": 67.36, "limits68": [0.54, 0.54]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 67.66,
                                      "limits68": [0.42, 0.42]},
        "units": "km/s/Mpc"
    },

    "Omega_Lambda": {
        "TT+lowE": {"value": 0.679, "limits68": [0.013, 0.013]},
        "TE+lowE": {"value": 0.699, "limits68": [0.012, 0.012]},
        "EE+lowE": {"value": 0.711, "limits68": [0.026, 0.033]},
        "TT,TE,EE+lowE": {"value": 0.6834, "limits68": [0.0084, 0.0084]},
        "TT,TE,EE+lowE+lensing": {"value": 0.6847,
                                  "limits68": [0.0073, 0.0073]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.6889,
                                      "limits68": [0.0056, 0.0056]},
        "units": "adimensional"
    },

    "Omega_m": {
        "TT+lowE": {"value": 0.321, "limits68": [0.013, 0.013]},
        "TE+lowE": {"value": 0.301, "limits68": [0.012, 0.012]},
        "EE+lowE": {"value": 0.289, "limits68": [0.033, 0.026]},
        "TT,TE,EE+lowE": {"value": 0.3166, "limits68": [0.0084, 0.0084]},
        "TT,TE,EE+lowE+lensing": {"value": 0.3153,
                                  "limits68": [0.0073, 0.0073]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.3111,
                                      "limits68": [0.0056, 0.0056]},
        "units": "adimensional"
    },

    "Omega_m__h2": {
        "TT+lowE": {"value": 0.1434, "limits68": [0.002, 0.002]},
        "TE+lowE": {"value": 0.1408, "limits68": [0.0019, 0.0019]},
        "EE+lowE": {"value": 0.1404, "limits68": [0.0039, 0.0034]},
        "TT,TE,EE+lowE": {"value": 0.1432, "limits68": [0.0013, 0.0013]},
        "TT,TE,EE+lowE+lensing": {"value": 0.143,
                                  "limits68": [0.0011, 0.0011]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.1424,
                                      "limits68": [0.00087, 0.00087]},
        "units": "adimensional"
    },

    "Omega_m__h3": {
        "TT+lowE": {"value": 0.09589, "limits68": [0.00046, 0.00046]},
        "TE+lowE": {"value": 0.09635, "limits68": [0.00051, 0.00051]},
        "EE+lowE": {"value": 0.0981, "limits68": [0.0018, 0.0016]},
        "TT,TE,EE+lowE": {"value": 0.09633, "limits68": [0.00029, 0.00029]},
        "TT,TE,EE+lowE+lensing": {"value": 0.09633,
                                  "limits68": [0.0003, 0.0003]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.09635,
                                      "limits68": [0.0003, 0.0003]},
        "units": "adimensional"
    },

    "sigma_8": {
        "TT+lowE": {"value": 0.8118, "limits68": [0.0089, 0.0089]},
        "TE+lowE": {"value": 0.793, "limits68": [0.011, 0.011]},
        "EE+lowE": {"value": 0.796, "limits68": [0.018, 0.018]},
        "TT,TE,EE+lowE": {"value": 0.812, "limits68": [0.0073, 0.0073]},
        "TT,TE,EE+lowE+lensing": {"value": 0.8111, "limits68": [0.006, 0.006]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.8102,
                                      "limits68": [0.006, 0.006]},
        "units": "adimensional"
    },

    "S_8": {
        "TT+lowE": {"value": 0.84, "limits68": [0.024, 0.024]},
        "TE+lowE": {"value": 0.794, "limits68": [0.024, 0.024]},
        "EE+lowE": {"value": 0.781, "limits68": [0.06, 0.052]},
        "TT,TE,EE+lowE": {"value": 0.834, "limits68": [0.016, 0.016]},
        "TT,TE,EE+lowE+lensing": {"value": 0.832, "limits68": [0.013, 0.013]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.825,
                                      "limits68": [0.011, 0.011]},
        "units": "adimensional"
    },

    "sigma_8__Omega_m^0.25": {
        "TT+lowE": {"value": 0.611, "limits68": [0.012, 0.012]},
        "TE+lowE": {"value": 0.587, "limits68": [0.012, 0.012]},
        "EE+lowE": {"value": 0.583, "limits68": [0.027, 0.027]},
        "TT,TE,EE+lowE": {"value": 0.609, "limits68": [0.0081, 0.0081]},
        "TT,TE,EE+lowE+lensing": {"value": 0.6078,
                                  "limits68": [0.0064, 0.0064]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.6051,
                                      "limits68": [0.0058, 0.0058]},
        "units": "adimensional"
    },

    "z_re": {
        "TT+lowE": {"value": 7.5, "limits68": [0.82, 0.82]},
        "TE+lowE": {"value": 7.11, "limits68": [0.75, 0.91]},
        "EE+lowE": {"value": 7.1, "limits68": [0.73, 0.87]},
        "TT,TE,EE+lowE": {"value": 7.68, "limits68": [0.79, 0.79]},
        "TT,TE,EE+lowE+lensing": {"value": 7.67, "limits68": [0.73, 0.73]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 7.82, "limits68": [0.71, 0.71]},
        "units": "adimensional"
    },

    "10^9A_s": {
        "TT+lowE": {"value": 2.092, "limits68": [0.034, 0.034]},
        "TE+lowE": {"value": 2.045, "limits68": [0.041, 0.041]},
        "EE+lowE": {"value": 2.116, "limits68": [0.047, 0.047]},
        "TT,TE,EE+lowE": {"value": 2.101, "limits68": [0.034, 0.031]},
        "TT,TE,EE+lowE+lensing": {"value": 2.1, "limits68": [0.03, 0.03]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 2.105,
                                      "limits68": [0.03, 0.03]},
        "units": "adimensional"
    },

    "10^9A_s__e^-2tau": {
        "TT+lowE": {"value": 1.884, "limits68": [0.014, 0.014]},
        "TE+lowE": {"value": 1.851, "limits68": [0.018, 0.018]},
        "EE+lowE": {"value": 1.904, "limits68": [0.024, 0.024]},
        "TT,TE,EE+lowE": {"value": 1.884, "limits68": [0.012, 0.012]},
        "TT,TE,EE+lowE+lensing": {"value": 1.883, "limits68": [0.011, 0.011]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 1.881,
                                      "limits68": [0.01, 0.01]},
        "units": "adimensional"
    },

    "Age": {
        "TT+lowE": {"value": 13.83, "limits68": [0.037, 0.037]},
        "TE+lowE": {"value": 13.761, "limits68": [0.038, 0.038]},
        "EE+lowE": {"value": 13.64, "limits68": [0.14, 0.16]},
        "TT,TE,EE+lowE": {"value": 13.8, "limits68": [0.024, 0.024]},
        "TT,TE,EE+lowE+lensing": {"value": 13.797, "limits68": [0.023, 0.023]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 13.787,
                                      "limits68": [0.020, 0.020]},
        "units": "Gyr"
    },

    "z_*": {
        "TT+lowE": {"value": 1090.3, "limits68": [0.41, 0.41]},
        "TE+lowE": {"value": 1089.57, "limits68": [0.42, 0.42]},
        "EE+lowE": {"value": 1087.8, "limits68": [1.7, 1.6]},
        "TT,TE,EE+lowE": {"value": 1089.95, "limits68": [0.27, 0.27]},
        "TT,TE,EE+lowE+lensing": {"value": 1089.92, "limits68": [0.25, 0.25]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 1089.8,
                                      "limits68": [0.21, 0.21]},
        "units": "adimensional"
    },

    "r_*": {
        "TT+lowE": {"value": 144.46, "limits68": [0.48, 0.48]},
        "TE+lowE": {"value": 144.95, "limits68": [0.48, 0.48]},
        "EE+lowE": {"value": 144.29, "limits68": [0.64, 0.64]},
        "TT,TE,EE+lowE": {"value": 144.39, "limits68": [0.3, 0.3]},
        "TT,TE,EE+lowE+lensing": {"value": 144.43, "limits68": [0.26, 0.26]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 144.57,
                                      "limits68": [0.22, 0.22]},
        "units": "Mpc"
    },

    "100theta_*": {
        "TT+lowE": {"value": 1.04097, "limits68": [0.00046, 0.00046]},
        "TE+lowE": {"value": 1.04156, "limits68": [0.00049, 0.00049]},
        "EE+lowE": {"value": 1.04001, "limits68": [0.00086, 0.00086]},
        "TT,TE,EE+lowE": {"value": 1.04109, "limits68": [0.0003, 0.0003]},
        "TT,TE,EE+lowE+lensing": {"value": 1.0411,
                                  "limits68": [0.00031, 0.00031]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 1.04119,
                                      "limits68": [0.00029, 0.00029]},
        "units": "adimensional"
    },

    "z_drag": {
        "TT+lowE": {"value": 1059.39, "limits68": [0.46, 0.46]},
        "TE+lowE": {"value": 1060.03, "limits68": [0.54, 0.54]},
        "EE+lowE": {"value": 1063.2, "limits68": [2.4, 2.4]},
        "TT,TE,EE+lowE": {"value": 1059.93, "limits68": [0.3, 0.3]},
        "TT,TE,EE+lowE+lensing": {"value": 1059.94, "limits68": [0.3, 0.3]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 1060.01,
                                      "limits68": [0.29, 0.29]},
        "units": "adimensional"
    },

    "r_drag": {
        "TT+lowE": {"value": 147.21, "limits68": [0.48, 0.48]},
        "TE+lowE": {"value": 147.59, "limits68": [0.49, 0.49]},
        "EE+lowE": {"value": 146.46, "limits68": [0.7, 0.7]},
        "TT,TE,EE+lowE": {"value": 147.05, "limits68": [0.3, 0.3]},
        "TT,TE,EE+lowE+lensing": {"value": 147.09, "limits68": [0.26, 0.26]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 147.21,
                                      "limits68": [0.23, 0.23]},
        "units": "Mpc"
    },

    "k_D": {
        "TT+lowE": {"value": 0.14054, "limits68": [0.00052, 0.00052]},
        "TE+lowE": {"value": 0.14043, "limits68": [0.00057, 0.00057]},
        "EE+lowE": {"value": 0.1426, "limits68": [0.0012, 0.0012]},
        "TT,TE,EE+lowE": {"value": 0.14090, "limits68": [0.00032, 0.00032]},
        "TT,TE,EE+lowE+lensing": {"value": 0.14087,
                                  "limits68": [0.0003, 0.0003]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.14078,
                                      "limits68": [0.00028, 0.00028]},
        "units": "1/Mpc"
    },

    "z_eq": {
        "TT+lowE": {"value": 3411., "limits68": [0.48, 0.48]},
        "TE+lowE": {"value": 3349., "limits68": [0.46, 0.46]},
        "EE+lowE": {"value": 3340., "limits68": [0.92, 0.81]},
        "TT,TE,EE+lowE": {"value": 3407., "limits68": [0.31, 0.31]},
        "TT,TE,EE+lowE+lensing": {"value": 3402., "limits68": [0.26, 0.26]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 3387.,
                                      "limits68": [0.21, 0.21]},
        "units": "adimensional"
    },

    "k_eq": {
        "TT+lowE": {"value": 0.01041, "limits68": [0.00014, 0.00014]},
        "TE+lowE": {"value": 0.01022, "limits68": [0.00014, 0.00014]},
        "EE+lowE": {"value": 0.01019, "limits68": [0.00028, 0.00025]},
        "TT,TE,EE+lowE": {"value": 0.010398, "limits68": [0.000094, 0.000094]},
        "TT,TE,EE+lowE+lensing": {"value": 0.010384,
                                  "limits68": [0.000081, 0.000081]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.010339,
                                      "limits68": [0.000063, 0.000063]},
        "units": "1/Mpc"
    },

    "100theta_s,eq": {
        "TT+lowE": {"value": 0.4483, "limits68": [0.0046, 0.0046]},
        "TE+lowE": {"value": 0.4547, "limits68": [0.0045, 0.0045]},
        "EE+lowE": {"value": 0.4562, "limits68": [0.0092, 0.0092]},
        "TT,TE,EE+lowE": {"value": 0.449, "limits68": [0.003, 0.003]},
        "TT,TE,EE+lowE+lensing": {"value": 0.4494,
                                  "limits68": [0.0026, 0.0026]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 0.4509,
                                      "limits68": [0.002, 0.002]},
        "units": "adimensional"
    },

    "f_2000^143": {
        "TT+lowE": {"value": 31.2, "limits68": [3., 3.]},
        "TT,TE,EE+lowE": {"value": 29.5, "limits68": [2.7, 2.7]},
        "TT,TE,EE+lowE+lensing": {"value": 29.6, "limits68": [2.8, 2.8]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 29.4, "limits68": [2.7, 2.7]},
        "units": "adimensional"
    },

    "f_2000^143x217": {
        "TT+lowE": {"value": 33.6, "limits68": [2., 2.]},
        "TT,TE,EE+lowE": {"value": 32.2, "limits68": [1.9, 1.9]},
        "TT,TE,EE+lowE+lensing": {"value": 32.3, "limits68": [1.9, 1.9]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 32.1, "limits68": [1.9, 1.9]},
        "units": "adimensional"
    },

    "f_2000^217": {
        "TT+lowE": {"value": 108.2, "limits68": [1.9, 1.9]},
        "TT,TE,EE+lowE": {"value": 107., "limits68": [1.8, 1.8]},
        "TT,TE,EE+lowE+lensing": {"value": 107.1, "limits68": [1.8, 1.8]},
        "TT,TE,EE+lowE+lensing+BAO": {"value": 106.9, "limits68": [1.8, 1.8]},
        "units": "adimensional"
    },
}
