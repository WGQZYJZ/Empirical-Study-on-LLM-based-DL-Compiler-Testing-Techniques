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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 2, (3, 4), True)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tanh(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 1, 10, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'stride' (position 4) must be tuple of ints, but found element of type bool at pos 0

jit:
conv_transpose2d(): argument 'stride' (position 4) must be tuple of ints, but found element of type bool at pos 0
'''