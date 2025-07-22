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
        self.conv = torch.nn.Conv2d(2, 256, 3, stride=3, padding=3)

    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if padding1 == None:
            padding1 = [0, 0, 0, 0]
        v2 = F.conv2d(v1, weight=other, stride=1, padding=padding1)
        v3 = v2 + other
        return v3



func = Model().to('cpu')


x1 = torch.randn(2, 2, 512, 512)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
local variable 'padding1' referenced before assignment

jit:
local variable 'padding1' referenced before assignment
'''