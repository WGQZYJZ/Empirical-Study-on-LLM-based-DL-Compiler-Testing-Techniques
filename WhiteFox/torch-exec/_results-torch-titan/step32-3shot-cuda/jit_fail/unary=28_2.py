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

    def __init__(self, min_value=(- 1.0), max_value=0.0):
        super().__init__()
        self.linear = torch.nn.Linear(8, 4)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, float(min_value))
        v3 = torch.clamp_max(v2, float(max_value))
        return v3



func = Model().to('cuda')



x1 = torch.randn(8)



x2 = torch.randn(4)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''