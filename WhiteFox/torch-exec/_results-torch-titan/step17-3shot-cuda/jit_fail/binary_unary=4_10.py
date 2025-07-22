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
        self.linear = torch.nn.Linear(10, 10)

    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = (v1 + other)
        v4 = torch.relu(v3)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 10)



other = torch.randn(1, 10)


test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''