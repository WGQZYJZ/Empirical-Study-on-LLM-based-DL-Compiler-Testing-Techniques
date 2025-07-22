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

    def __init__(self, t5):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
        self.other = t5

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.add(v1, self.other)
        return v2


t5 = torch.randn(1, 16)
func = Model(t5).to('cpu')


t5 = torch.randn(1, 16)

x1 = torch.randn(1, 8)

test_inputs = [t5, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''