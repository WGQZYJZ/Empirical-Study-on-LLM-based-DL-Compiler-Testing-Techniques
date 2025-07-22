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
        self.linear = torch.nn.Linear(8, 64)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v2 > 0
        v3 = v1 * 0.01
        v4 = torch.where(v2, v1, v3)
        return v


func = Model().to('cpu')


x1 = torch.randn(1, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
local variable 'v2' referenced before assignment

jit:
local variable 'v2' referenced before assignment
'''