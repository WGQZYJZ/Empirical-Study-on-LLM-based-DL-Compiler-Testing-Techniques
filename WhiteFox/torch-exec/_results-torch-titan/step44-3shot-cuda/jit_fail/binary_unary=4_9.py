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

    def __init__(self, other=None):
        super().__init__()
        self.other = other
        self.linear = torch.nn.Linear(64, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + self.other)
        v3 = torch.nn.functional.relu(v2)
        return v3



func = Model(other).to('cuda')



other = torch.randn(1, 8)



x1 = torch.randn(1, 64)


test_inputs = [other, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''