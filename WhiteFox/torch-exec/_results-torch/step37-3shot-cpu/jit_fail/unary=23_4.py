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
        self.conv_transpose = torch.nn.ConvTranspose2d(2, 3, 7, stride=2, dilation=1, padding=0)

    def forward(self, x1):
        v1 = torch.tanh(self.conv_transpose(x1))
        return v1



func = Model().to('cpu')


x0 = torch.randn(1, 2, 8, 8)

x1 = torch.randn(2)

test_inputs = [x0, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''