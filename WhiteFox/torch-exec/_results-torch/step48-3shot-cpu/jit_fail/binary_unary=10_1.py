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
        self.linears = torch.nn.ModuleList([torch.nn.Linear(8 * 8 * 1, 128), torch.nn.Linear(128, 10)])

    def forward(self, x1):
        v1 = x1.reshape(x1.shape[0], -1)
        v2 = self.linears[0](v1)
        v3 = self.linears[1](v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 8, 8, 1)

x2 = torch.randn(1, 128)

y = torch.randn(1, 10)

test_inputs = [x1, x2, y]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''