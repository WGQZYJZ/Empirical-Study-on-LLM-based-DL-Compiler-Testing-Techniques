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

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(v2, x2)
        v3 = torch.mm(v2, v2)
        v4 = torch.mm(v3, v2)
        return torch.cat([v1, v1, v3, v4, v1], 1)



func = Model().to('cpu')


x1 = torch.randn(5, 5)

x2 = torch.randn(5, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
local variable 'v2' referenced before assignment

jit:
local variable 'v2' referenced before assignment
'''