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

    def __init__(self, n):
        super().__init__()
        self.convs = torch.nn.ModuleList()
        for _ in range(n):
            self.convs.append(nn.Conv2d(4, 4, 3, stride=2, padding=1))

    def forward(self, x):
        v1 = self.convs[0](x)
        v2 = self.convs[1](v1)
        v3 = v2 > 0
        v4 = v2 * -0.001
        v5 = torch.where(v3, v2, v4)
        v6 = self.conv[1](v5)
        return v6


n = 2

func = Model(n).to('cpu')


x1 = torch.randn(1, 4, 448, 448)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'conv'

jit:
'Model' object has no attribute 'conv'
'''