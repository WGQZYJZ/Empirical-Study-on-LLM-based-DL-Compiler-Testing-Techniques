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

    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)

    def forward(self, x1):
        t1 = self.linear(x1)
        t2 = (t1 + other)
        t3 = torch.relu(t2)
        return t3




other = torch.rand(64, 32)


func = Model(other).to('cuda')



x1 = torch.randn(64, 32)



other = torch.rand(64, 32)


test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''