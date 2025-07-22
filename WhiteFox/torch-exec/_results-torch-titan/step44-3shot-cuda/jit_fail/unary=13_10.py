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
        self.linear = torch.nn.Linear(1, 8)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1):
        v1 = self.linear(input)
        v2 = self.sigmoid(v1)
        v3 = (v1 * v2)
        return v3



func = Model().to('cuda')



x = torch.randn(1, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not builtin_function_or_method

jit:
linear(): argument 'input' (position 1) must be Tensor, not builtin_function_or_method
'''