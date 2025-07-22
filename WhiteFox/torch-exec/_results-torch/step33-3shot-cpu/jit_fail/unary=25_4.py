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

    def __init__(self, negative_slope):
        super().__init__()
        self.linear_ = torch.nn.Linear(8, 1)

    def forward(self, x1):
        v1 = self.linear_(x1)
        v2 = self.linear_(x1)
        v3 = v2 > 0
        v4 = v1 * self.negative_slope
        v5 = torch.where(v3, v1, v4)
        return v5


negative_slope = 1

func = Model(negative_slope).to('cpu')


x1 = torch.randn(1, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'negative_slope'

jit:
'Model' object has no attribute 'negative_slope'
'''