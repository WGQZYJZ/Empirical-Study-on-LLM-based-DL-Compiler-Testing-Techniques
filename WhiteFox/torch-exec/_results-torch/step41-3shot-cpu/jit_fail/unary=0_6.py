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
        v1 = torch.exp(torch.neg(x1))
        v2 = torch.mul(v1, x1)
        v3 = torch.sin(v2)
        v4 = torch.mul(v3, v3)
        v5 = torch.asin(v4)
        v6 = torch.asinh(v1)
        v7 = torch.tanh(v6)
        return torch.sigmoid(-v2 * v5 * v7 * 0.48811819796455164)



func = Model().to('cpu')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
neg(): argument 'input' (position 1) must be Tensor, not int

jit:
neg(): argument 'input' (position 1) must be Tensor, not int
'''