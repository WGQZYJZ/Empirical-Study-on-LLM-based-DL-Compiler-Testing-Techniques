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

    def __init__(self, min_value=3, max_value=-8):
        super().__init__()
        self.Tanh = torch.nn.Tanh()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=2)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.Tanh(v3)
        return v4



func = Model().to('cpu')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int

jit:
conv_transpose2d(): argument 'input' (position 1) must be Tensor, not int
'''