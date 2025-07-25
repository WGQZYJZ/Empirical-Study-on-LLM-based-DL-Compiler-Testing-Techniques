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
        self.conv = torch.nn.Conv2d(3, 10, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(10, 100, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(100, 4, 5, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        v8 = v7 * 0.5
        v9 = v7 * 0.7071067811865476
        v10 = torch.erf(v9)
        v11 = v10 + 1
        v12 = v8 * v11
        v13 = self.conv3(v13)
        return v13



func = Model().to('cpu')


x1 = torch.randn(1, 3, 20, 20)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
local variable 'v13' referenced before assignment

jit:
local variable 'v13' referenced before assignment
'''