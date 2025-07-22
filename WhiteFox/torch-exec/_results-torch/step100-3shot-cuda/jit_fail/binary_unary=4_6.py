import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg

class Model(torch.nn.Module):

    def __init__(self, linear_weights, linear_bias):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
        self.linear.weight = torch.nn.Parameter(linear_weights)
        self.linear.bias = torch.nn.Parameter(linear_bias)

    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        v2 = v1
        if other is not None:
            v2 = v2 + other
        v3 = torch.relu(v2)
        return v3


linear_weights = torch.randn(2, 3)
linear_bias = torch.randn(2)
func = Model(linear_weights, linear_bias).to('cuda')


linear_weights = torch.randn(2, 3)

linear_bias = torch.randn(2)

x1 = torch.randn(1, 3)

test_inputs = [linear_weights, linear_bias, x1]

# JIT_FAIL
'''
direct:
forward() takes from 2 to 3 positional arguments but 4 were given

jit:
forward() takes from 2 to 3 positional arguments but 4 were given
'''