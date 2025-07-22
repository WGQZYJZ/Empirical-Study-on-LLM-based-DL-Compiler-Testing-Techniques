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
        self.linear = torch.nn.Linear(16, 10, bias=False)
        other_weight = torch.randn(10, 16)
        self.linear.weight.data.copy_(other_weight)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 + other)
        return v2



func = Model().to('cuda')



other = torch.randn(10, 16)



x = torch.randn(16, 16)


test_inputs = [other, x]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''