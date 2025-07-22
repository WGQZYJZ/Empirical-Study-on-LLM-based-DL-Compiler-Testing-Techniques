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

    def forward(self, x1):
        out = F.linear(x1, 4, 3, 1)
        out = F.hardsigmoid(out, offset=3, slope=0.2)
        out = F.hardsigmoid(out, offset=0, slope=1)
        return out


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear() takes from 2 to 3 positional arguments but 4 were given

jit:
linear() takes from 2 to 3 positional arguments but 4 were given
'''