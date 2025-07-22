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
        self.linear = torch.nn.Linear(3, 16)
        self.bn = torch.nn.BatchNorm2d(16)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 + other)
        v3 = self.bn(v2)
        return v3




func = Model().to('cuda')



x = torch.randn(1, 3)



other = torch.randn(1, 16)


test_inputs = [x, other]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''