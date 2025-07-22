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
        self.conv = torch.nn.Conv2d(4, 1, 3, stride=2, padding=3)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3




min_value = torch.randn(1, 1, 1, 1)


max_value = torch.randn(1, 1, 1, 1)


func = Model(min_value, max_value).to('cuda')



min_value = torch.randn(1, 1, 1, 1)



max_value = torch.randn(1, 1, 1, 1)



x1 = torch.randn(1, 4, 32, 32)


test_inputs = [min_value, max_value, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''