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
        super(Model, self).__init__()
        self.m = torch.nn.Linear(2, 7)

    def forward(input, x1):
        v1 = torch.mm(x1, x4)
        v2 = torch.mm(x3, x2)
        v3 = v1 + v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(2, 2)

x2 = torch.randn(2, 2)

x3 = torch.randn(2, 2)

x4 = torch.randn(2, 2)

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 5 were given

jit:
forward() takes 2 positional arguments but 5 were given
'''