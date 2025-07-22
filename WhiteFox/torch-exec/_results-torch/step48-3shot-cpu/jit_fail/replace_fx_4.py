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

    def __init__(self):
        super().__init__()

    def forward(self, x, bias=None):
        y1 = F.linear(x, 200, bias=bias)
        y2 = F.linear(x, 200, bias=bias)
        y3 = y1 * y2
        return y3



func = Model().to('cpu')



x = torch.randn(10, 2, 32, 200, dtype=torch.float)

test_inputs = [x]

# JIT_FAIL
'''
direct:
linear(): argument 'weight' (position 2) must be Tensor, not int

jit:
linear(): argument 'weight' (position 2) must be Tensor, not int
'''