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
        self.linear = torch.nn.Linear(3, 8)
        self.v1 = other

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.v1
        return v2


other = torch.randn(1, 8)

func = Model(other).to('cpu')


other = torch.randn(1, 8)

x = torch.randn(1, 3)

test_inputs = [other, x]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''