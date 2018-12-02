# -*- coding: utf-8 -*-
"""
Contains the PlanckT's classes and functions (if any).

"""

__all__ = ["Param"]


class Param(object):

    """Class to store all info about a single parameter in Planck results."""

    def __init__(self, name, analysis, model="lcdm"):
        self.name = name
        self.analysis = analysis
        self.model = model
        self._validate_model()
        self._get_results()

    def _validate_model(self):
        """Get ``params_dict`` from the chosen model."""
        if self.model == "lcdm":
            from planckt.lcdm import params_dict
        else:
            raise ValueError("The model ``{}`` is not available."
                             .format(self.model))
        self.params_dict = params_dict

    def _get_results(self):
        """
        Create new properties (``units``, ``value`` and ``limit68``) from
        ``params_dict``.
        """
        self.units = self.params_dict[self.name]["units"]

        self.value = self.params_dict[self.name][self.analysis]["value"]

        limits68 = self.params_dict[self.name][self.analysis]["limits68"]
        if str(limits68[0]) == str(limits68[1]):
            self.limit68 = limits68[0]
        else:
            self.limit68 = limits68
            print("ATENTION: Returning the 68% limits as a list of the form "
                  "[inferior, superior]. Use them with caution.")
