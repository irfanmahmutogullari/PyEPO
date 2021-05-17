#!/usr/bin/env python
# coding: utf-8

from abc import ABC, abstractmethod

class optModel(ABC):
    """abstract class for optimization model"""

    def __init__(self):
        self._model = self._getModel()

    def __repr__(self):
        return self.__class__.__name__

    @property
    @abstractmethod
    def num_cost(self):
        pass

    @abstractmethod
    def _getModel(self):
        """
        build a model from a optimization solver
        """
        pass

    @abstractmethod
    def setObj(self, c):
        """
        set objective function with given cost vector
        """
        pass

    @abstractmethod
    def solve(self):
        """
        solve model
        Returns:
            sol: optimal solution
            obj: optimal value
        """
        pass

    @abstractmethod
    def addConstr(self, coefs, rhs):
        """
        add new constraint
        Returns:
            model: optModel
        """
        pass
