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

class Model2(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, None, bias=None)
        v2 = v1
        min_value = 0.5
        v3 = torch.clamp(v2, min_value)
        max_value = 0.7071067811865476
        v4 = torch.clamp(v3, max_value)
        return v4


func = Model2().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear(): argument 'weight' (position 2) must be Tensor, not NoneType

jit:
linear(): argument 'weight' (position 2) must be Tensor, not NoneType
'''