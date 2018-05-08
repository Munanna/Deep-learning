# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Placeholder():
	def __init__(self):
		self.output_noders = []
		_default_graph.placeholders.append(self)

class Variable():
	def __init__(self, initial_value=None):
		self.value = initial_value
		self.output_nodes = []
		_default_graph.variables.append(self)

class Graph():
	def __init__(self):
		self.operations = []
		self.placeholders = []
		self.variables = []

	def set_as_default(self):
		global _default_graph
		_default_graph = self