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
        self.linear = torch.nn.Linear(2, 2).cuda()
        self.relu = torch.nn.ReLU().cuda()

    def forward(self, x1):
        (v1, v3) = x1
        a0 = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias)
        v2 = a0.permute(0, 2, 1)
        a1 = self.relu(v2)
        v4 = (a1, a0)
        return v4



func = Model().to('cpu')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
cannot unpack non-iterable int object

jit:
cannot unpack non-iterable int object
'''