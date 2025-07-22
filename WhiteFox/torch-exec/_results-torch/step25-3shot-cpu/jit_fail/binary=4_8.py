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
        self.lin = torch.nn.Linear(3, 8)

    def forward(self, x1, x2):
        v1 = self.lin(x1)
        v2 = v1 + x2
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 8, 64, 64)

__other__ = torch.randn(1)

test_inputs = [x1, x2, __other__]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''