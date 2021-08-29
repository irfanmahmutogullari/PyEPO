#!/usr/bin/env python
# coding: utf-8
"""
Knapsack problem
"""

import gurobipy as gp
from gurobipy import GRB

from spo.model.grb import optGRBModel


class knapsackModel(optGRBModel):
    """
    This class is optimization model for knapsack problem

    Args:
        weights (ndarray): weights of items
        capacity (ndarray): total capacity
    """

    def __init__(self, weights, capacity):
        self.weights = weights
        self.capacity = capacity
        self.items = list(range(self.weights.shape[1]))
        super().__init__()

    @property
    def num_cost(self):
        return len(self.items)

    def _getModel(self):
        """
        A method to build Gurobi model
        """
        # ceate a model
        m = gp.Model("knapsack")
        # turn off output
        m.Params.outputFlag = 0
        # varibles
        self.x = m.addVars(self.items, name="x", vtype=GRB.BINARY)
        # sense
        m.modelSense = GRB.MINIMIZE
        # constraints
        for i in range(len(self.capacity)):
            m.addConstr(gp.quicksum(self.weights[i,j] * self.x[j]
                        for j in self.items) <= self.capacity[i])
        return m

    def relax(self):
        """
        A method to relax model
        """
        # copy
        model_rel = knapsackModelRel(self.weights, self.capacity)
        return model_rel


class knapsackModelRel(knapsackModel):
    """
    This class is relaxed optimization model for knapsack problem.
    """

    def _getModel(self):
        """
        A method to build Gurobi
        """
        # ceate a model
        m = gp.Model("knapsack")
        # turn off output
        m.Params.outputFlag = 0
        # varibles
        self.x = m.addVars(self.items, name="x", ub=1)
        # sense
        m.modelSense = GRB.MINIMIZE
        # constraints
        for i in range(len(self.capacity)):
            m.addConstr(gp.quicksum(self.weights[i,j] * self.x[j]
                        for j in self.items) <= self.capacity[i])
        return m

    def relax(self):
        """
        A forbidden method to relax MIP model
        """
        raise RuntimeError("Model has already been relaxed.")