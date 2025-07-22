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
    kwargs = {'min_value': -0.5, 'max_value': 0.5}

    def forward(self, x1):
        v1 = F.linear(x1, (3072,))
        v2 = torch.clamp_max(v1, 0.9)
        v3 = torch.clamp_max(v2, 0.7)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear(): argument 'weight' (position 2) must be Tensor, not tuple

jit:
linear(): argument 'weight' (position 2) must be Tensor, not tuple
'''