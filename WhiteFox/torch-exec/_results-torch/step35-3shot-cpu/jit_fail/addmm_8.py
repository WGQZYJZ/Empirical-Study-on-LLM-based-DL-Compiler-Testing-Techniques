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

    def forward(self, x1, x3, inp):
        v1 = torch.mm(x1, x2)
        v3 = torch.sigmoid(v1)
        v2 = v3 + inp
        return v2



func = Model().to('cpu')


x1 = torch.randn(3, 3)

x2 = torch.randn(3, 3, requires_grad=True)

x3 = torch.randn(10, 3, 3)

inp = torch.randn(10, 3, 3, requires_grad=True)

test_inputs = [x1, x2, x3, inp]

# JIT_FAIL
'''
direct:
forward() takes 4 positional arguments but 5 were given

jit:
forward() takes 4 positional arguments but 5 were given
'''