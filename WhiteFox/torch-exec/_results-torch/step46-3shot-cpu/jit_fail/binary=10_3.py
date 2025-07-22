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

    def __init__(self, linear):
        super().__init__()
        self.linear = linear

    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other
        return v2


linear = 1
func = Model(torch.nn.Linear(4, 5)).to('cpu')


x3 = torch.randn(1, 3, 64, 64)

other = torch.ones(1, 2, 4, 4)

test_inputs = [x3, other]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''