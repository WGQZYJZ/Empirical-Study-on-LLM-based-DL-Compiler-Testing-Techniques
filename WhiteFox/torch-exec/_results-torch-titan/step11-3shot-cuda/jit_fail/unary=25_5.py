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
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = self.linear(input)
        v2 = (v1.detach() > 0)
        v3 = (v1 * negative_slope)
        v4 = torch.where(v2, v1, v3)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not builtin_function_or_method

jit:
linear(): argument 'input' (position 1) must be Tensor, not builtin_function_or_method
'''