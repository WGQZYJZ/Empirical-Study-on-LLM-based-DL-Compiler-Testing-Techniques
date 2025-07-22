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
        self.conv_transpose = torch.nn.ConvTranspose2d(256, 128, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.relu(v1)
        v3 = torch.max_pool2d(v2, 3, stride=2, padding=1)
        v4 = v4 + 3
        v5 = torch.clamp_min(v4, 0)
        v6 = torch.clamp_max(v5, 6)
        v7 = v6 / 6
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 256, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
local variable 'v4' referenced before assignment

jit:
local variable 'v4' referenced before assignment
'''