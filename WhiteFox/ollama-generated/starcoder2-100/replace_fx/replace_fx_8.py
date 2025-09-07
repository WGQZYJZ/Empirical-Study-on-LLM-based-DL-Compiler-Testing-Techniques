
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.rand_like(x1)  # generate a random tensor with the same size as input
        v3 = torch.nn.functional.linear(v2, self.weight, self.bias)
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3)
m(x1)

# We can then generate a valid graph by adding dropout to our graph with this inputs:
import torch
import torch.nn as nn
import functools as ft
import operator

class MyModel(torch.nn.Module):
    def __init__(self, f1 = 30, f2=4):
        super().__init__()
        self.linear1 = torch.nn.Linear(f1, f2)

    def forward(self, x1):
        v1 = x1 / (x1 - 1) * 30 + 5  # generate a random tensor with the same size as input
        v2 = ft.reduce(v1, operator.mul, initializer=7) 
        v3 = torch.nn.functional.dropout(v1, f1-f2)   # This line will be replaced by a lowmem dropout in the graph
        return self.linear1(v2 + 40 - v3 / 8 * (9))

# Initializing our model
m = MyModel()

# We can then generate a valid graph by adding dropout to our graph with this inputs:
import torch
import torch.nn as nn
import functools as ft
import operator


class MyModel(torch.nn.Module):
    def __init__(self, f1= 30, f2 = 4):
        super().__init__()
        self.linear1 = torch.nn.Linear(f1, f2)

    def forward(self, x1): 
        v1 = torch.rand_like(x1)   # generate a random tensor with the same size as input
        v2 = ft.reduce(v1, operator.mul, initializer=7)  # This line will be replaced by rand like in the graph
        
        return self.linear1(v3 + x4 / 8 * (9))


# Initializing our model
m = MyModel()

