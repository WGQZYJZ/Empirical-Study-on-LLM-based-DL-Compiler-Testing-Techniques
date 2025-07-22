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

    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, v2)
        v2 = v1 + inp
        return v2



func = Model().to('cpu')


x1 = torch.randn(3, 3, requires_grad=True)

x2 = torch.randn(3, 3, requires_grad=True)

inp = torch.randn(3, 3, requires_grad=True)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
local variable 'v2' referenced before assignment

jit:
local variable 'v2' referenced before assignment
'''