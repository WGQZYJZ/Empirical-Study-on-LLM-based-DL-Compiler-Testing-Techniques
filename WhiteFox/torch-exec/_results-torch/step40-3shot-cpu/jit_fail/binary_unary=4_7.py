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
        self.linear = torch.nn.Linear(28 * 28, 128)

    def forward(self, **x1):
        v1 = self.linear(x1['input'])
        v2 = v1 + x1['other']
        v3 = torch.relu(v2)
        return v3


func = Model().to('cpu')


x1 = torch.randn(10, 28 * 28)

o1 = torch.randn(10, 28 * 28)

test_inputs = [x1, o1]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 3 were given

jit:
forward() takes 1 positional argument but 3 were given
'''