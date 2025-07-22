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
        self.linear = torch.nn.Linear(10, 5)
        self.other = other

    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = (v1 + self.other)
        return v3



other = 1

func = Model(other).to('cuda')



o1 = torch.zeros(5)



o2 = torch.ones(5)



x1 = torch.randn(10, 10)


test_inputs = [o1, o2, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''