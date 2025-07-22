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
        self.linear = torch.nn.Linear(4, 5)

    def forward(self, x0, other=torch.Tensor([1, 2, 3, 4])):
        v0 = self.linear(x0)
        v1 = v0 + other
        v2 = torch.relu(v1)
        v3 = torch.erf(v2)
        return (v3, v2)



func = Model().to('cpu')

x0 = 1

test_inputs = [x0]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
linear(): argument 'input' (position 1) must be Tensor, not int
'''