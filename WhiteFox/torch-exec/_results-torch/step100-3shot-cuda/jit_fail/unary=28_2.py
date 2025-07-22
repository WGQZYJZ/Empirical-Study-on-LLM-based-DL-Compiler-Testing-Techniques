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

    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=0.5)
        v3 = torch.clamp_max(v2, max_value=-0.1)
        return v3


min_value = 1
max_value = 1

func = Model(min_value, max_value).to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
linear(): argument 'input' (position 1) must be Tensor, not int
'''