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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 8, 1, stride=2)

    def forward(self, x1):
        v1 = F.relu(self.conv_transpose(x1))
        v2 = v1 + 0.1
        v3 = torch.clamp(v2, min=-1)
        v4 = torch.clamp(v3, max=1)
        v5 = v1 * v4
        v6 = v5 / 10
        return v6



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