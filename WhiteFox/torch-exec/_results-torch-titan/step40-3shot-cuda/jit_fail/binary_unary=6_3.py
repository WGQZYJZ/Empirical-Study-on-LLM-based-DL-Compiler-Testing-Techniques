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

    def __init__(self, weight, bias):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)
        self.linear.weight = torch.nn.Parameter(weight)
        self.linear.bias = torch.nn.Parameter(bias)

    def forward(self, x1):
        v1 = self.linear(x1)
        other = 1
        v2 = (v1 - other)
        v3 = F.relu(v2)
        return v3




weight = torch.randn(2, 1, requires_grad=True)


bias = torch.randn(1, requires_grad=True)

func = Model(weight, bias).to('cuda')



weight = torch.randn(2, 1, requires_grad=True)



bias = torch.randn(1, requires_grad=True)



x1 = torch.randn(1, 2)


test_inputs = [weight, bias, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''