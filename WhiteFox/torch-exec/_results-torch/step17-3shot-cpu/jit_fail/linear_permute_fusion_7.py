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

    def forward(self, x1, x2):
        v4 = torch.permute(x1, 1, 2)
        v1 = torch.nn.functional.linear(v4, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 1, 3, 2)
        v3 = torch.nn.functional.linear(x2, self.linear.weight, self.linear.bias)
        return (v1, v2, v3)



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2, 3, device='cpu')

x2 = torch.randn(1, 2, 2, device='cpu')

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
permute() takes 2 positional arguments but 3 were given

jit:
permute() takes 2 positional arguments but 3 were given
'''