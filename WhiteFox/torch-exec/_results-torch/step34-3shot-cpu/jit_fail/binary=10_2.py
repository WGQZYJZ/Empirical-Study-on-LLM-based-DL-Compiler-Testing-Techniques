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
        self.linear = torch.nn.Linear(3, 3)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + x1
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 3)

__other__ = torch.randn(1, 3, requires_grad=True)

test_inputs = [x1, __other__]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''