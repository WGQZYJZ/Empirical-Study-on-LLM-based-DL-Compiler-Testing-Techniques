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

    def forward(self, x1):
        d1 = self.conv(x1)
        d2 = d1 * 0.5
        d3 = d1 * 0.7071067811865476
        d4 = torch.erf(d3)
        d5 = d4 + 1
        d6 = d2 * d5
        c2 = torch.Tensor()
        for i in range(num):
            c2 = torch.cat([c2, d6])
        c1 = c2[0:9223372036854775807]
        s1 = c1[0:size]
        c3 = torch.Tensor()
        for j in range(num):
            c3 = torch.cat([c3, c1, s1])
        return c3


func = Model().to('cuda')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''