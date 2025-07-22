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
        self.linear = torch.nn.Linear(12, 16)
        self.other = other

    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + self.other
        v3 = torch.relu(v2)
        return v3


other = torch.randn(16, 16)

func = Model(other).to('cpu')


x = torch.randn(16, 12)

other = torch.randn(16, 16)

test_inputs = [x, other]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''