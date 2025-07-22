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
        self.linear = torch.nn.Linear(8, 64)

    def forward(x2, **kwargs):
        v1 = self.linear(x2, **kwargs)
        v2 = torch.clamp(v1, min_value=kwargs['min_value'], max_value=kwargs['max_value'])
        return v2


min_value = 1
max_value = 1

func = Model(min_value, max_value).to('cpu')


x2 = torch.randn(1, 8)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 2 were given

jit:
forward() takes 1 positional argument but 2 were given
'''