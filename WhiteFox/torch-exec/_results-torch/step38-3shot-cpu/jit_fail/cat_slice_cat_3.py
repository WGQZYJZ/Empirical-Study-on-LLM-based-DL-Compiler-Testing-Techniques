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

    def __init__(self, size):
        super().__init__()
        self.size = size

    def forward(self, x):
        y1 = torch.cat([x[0], x[1], x[2]], dim=1)
        x0 = y1.narrow(1, 0, 9223372036854775807)
        c1 = x0.narrow(1, 0, self.size)
        c2 = x0.narrow(1, 0, self.size // 2)
        c3 = x0.narrow(1, 1024, self.size)
        z0 = torch.cat([y1, c1, c2, c3], dim=1)
        return z0


size = 1

func = Model(size).to('cpu')


x1 = torch.randn(1, 3, 2048, 2048)

x2 = torch.randn(1, 3, 2048, 2048)

x3 = torch.randn(1, 3, 2048, 2048)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''