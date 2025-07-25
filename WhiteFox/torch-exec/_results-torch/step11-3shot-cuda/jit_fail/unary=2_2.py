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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 1, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        return v9



func = Model().to('cuda')


x1 = torch.tensor(2.0, requires_grad=True)

x2 = torch.tensor(2.0, requires_grad=True)

x3 = torch.tensor(2.0, requires_grad=True)

x4 = torch.tensor(3.0, requires_grad=True)

x5 = torch.tensor(2.0, requires_grad=True)

x6 = torch.tensor(2.0, requires_grad=True)

x7 = torch.tensor(2.0, requires_grad=True)

x8 = torch.tensor(3.0, requires_grad=True)

x9 = torch.tensor(2.0, requires_grad=True)

x10 = torch.tensor(2.0, requires_grad=True)

x11 = torch.tensor(1.0, requires_grad=True)

x12 = torch.tensor(1.0, requires_grad=True)

x13 = torch.tensor(1.0, requires_grad=True)

test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 14 were given

jit:
forward() takes 2 positional arguments but 14 were given
'''