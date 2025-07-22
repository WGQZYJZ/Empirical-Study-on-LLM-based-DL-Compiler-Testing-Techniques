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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(torch.reshape(x1, (1, 2, 2)), torch.reshape(self.linear.weight, (2, 2)), torch.reshape(self.linear.bias, 2))
        v2 = v1.permute(0, 2, 1)
        return torch.reshape(v2, (2, 2, 2))



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
reshape(): argument 'shape' (position 2) must be tuple of ints, not int

jit:
reshape(): argument 'shape' (position 2) must be tuple of ints, not int
'''