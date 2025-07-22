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
        self.linear1 = torch.nn.Linear(16, 32)
        self.linear2 = torch.nn.Linear(32, 64)

    def forward(self, v, x):
        v1 = self.linear1(v)
        v2 = v1 + x
        return v2


func = Model().to('cuda')


v = torch.randn(1, 32)

x1 = torch.randn(1, 16)

x2 = torch.randn(1, 16)

test_inputs = [v, x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''