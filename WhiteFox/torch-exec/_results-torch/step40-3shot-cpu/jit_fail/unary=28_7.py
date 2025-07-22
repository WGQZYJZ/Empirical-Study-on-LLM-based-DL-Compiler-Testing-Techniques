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
        self.min_value = min_value
        self.max_value = max_value

    def clamp_min(self, x):
        return torch.clamp(x, min=self.min_value)

    def clamp_max(self, x):
        return torch.clamp(x, max=self.max_value)

    def forward(self, x):
        t1 = self.linear(x)
        return self.clamp_max(self.clamp_min(t1))


min_value = 1
max_value = 1
func = Model(-10, 10).to('cpu')


x = torch.randn(1, 4, 1, 1)

test_inputs = [x]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'linear'

jit:
'Model' object has no attribute 'linear'
'''