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

    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(888, 1234)
        self.other = other

    def forward(self, x2):
        v7 = self.linear(x2)
        v8 = v7 + self.other
        v9 = torch.relu(v8)
        return v9


other = torch.randn(1234)
func = Model(other).to('cpu')


other = torch.randn(1234)

x2 = torch.randn(1234, 888)

test_inputs = [other, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''