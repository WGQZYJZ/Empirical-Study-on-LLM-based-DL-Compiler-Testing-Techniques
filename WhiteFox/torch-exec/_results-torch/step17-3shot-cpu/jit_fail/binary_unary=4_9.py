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

    def __init__(self, x):
        super().__init__()
        self.linear = torch.nn.Linear(x ** 2, x)

    def forward(self, x1, **kwargs):
        v1 = self.linear(x1)
        v2 = v1 + kwargs['x2']
        v3 = torch.relu(v2)
        return v3


x = 1
func = Model(1).to('cpu')


x1 = torch.randn(1, 1, 2, 2)

x2 = torch.rand(1, 1, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''