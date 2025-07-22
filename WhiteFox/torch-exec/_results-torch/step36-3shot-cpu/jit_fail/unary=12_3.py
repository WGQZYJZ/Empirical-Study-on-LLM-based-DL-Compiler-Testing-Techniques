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
        self.conv = torch.nn.Conv2d(3, 3, 63, stride=1, padding=0)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = torch.mul(v1, v2)
        v4 = self.conv(x2)
        v5 = torch.sigmoid(v4)
        v6 = torch.mul(v4, v5)
        v7 = torch.mul(v3, v6)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

x3 = torch.randn(1, 256, 213, 231)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''