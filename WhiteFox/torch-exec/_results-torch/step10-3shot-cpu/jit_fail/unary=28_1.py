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

    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(8, 8)

    def forward(self, x1):
        v1 = torch.clamp_min(x1, min_value)
        v2 = torch.clamp_max(v1, max_value)
        return v2


min_value = torch.randn(1, 1)
max_value = torch.randn(1, 1)

func = Model(min_value, max_value).to('cpu')


min_value = torch.randn(1, 1)

max_value = torch.randn(1, 1)

x1 = torch.randn(1, 8)

test_inputs = [min_value, max_value, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''