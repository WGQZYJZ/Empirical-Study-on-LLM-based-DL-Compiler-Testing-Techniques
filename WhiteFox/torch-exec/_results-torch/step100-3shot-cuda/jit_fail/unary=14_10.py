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
        self.conv_transpose_32 = torch.nn.ConvTranspose2d(60, 8, (3, 3), stride=1, padding=((1, 1), (1, 1)))

    def forward(self, x1):
        v1 = self.conv_transpose_32(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3



func = Model().to('cuda')


x1 = torch.randn(1, 60, 5, 5)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'padding' (position 5) must be tuple of ints, but found element of type tuple at pos 0

jit:
conv_transpose2d(): argument 'padding' (position 5) must be tuple of ints, but found element of type tuple at pos 0
'''