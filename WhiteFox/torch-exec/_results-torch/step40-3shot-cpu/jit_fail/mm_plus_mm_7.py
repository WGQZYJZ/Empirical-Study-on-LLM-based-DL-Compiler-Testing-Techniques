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

    def forward(self, a):
        (a0, a1, a2, a3, a4) = torch.split(a, 5, dim=1)
        b0 = torch.stack((a0, a1), 0)
        b1 = torch.stack((a2, a3, a4), 0)
        x = torch.stack((b0, b1), 0)
        return x



func = Model().to('cpu')


input = torch.randn(4, 10)

test_inputs = [input]

# JIT_FAIL
'''
direct:
not enough values to unpack (expected 5, got 2)

jit:
not enough values to unpack (expected 5, got 2)
'''