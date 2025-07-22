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
        self.linear = torch.nn.Linear(1280, 1280)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, 0)
        v3 = torch.clamp_max(v2, 0.8)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 1280)


min_value = torch.full((1,), -10, out=torch.Tensor())


max_value = torch.full((1,), 10, out=torch.Tensor())

test_inputs = [x1, min_value, max_value]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''