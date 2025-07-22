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

class LRelu(torch.nn.Module):

    def __init__(self, negative_slope):
        super().__init__()
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.weight, self.bias)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


negative_slope = 1
func = LRelu(0.5).to('cpu')


x1 = torch.randn(1, 32, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'LRelu' object has no attribute 'weight'

jit:
'LRelu' object has no attribute 'weight'
'''