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
        self.layernorm = torch.nn.LayerNorm([1, 2, 2])

    def forward(self, x1):
        v1 = torch.nn.functional.layer_norm(x1, self.layernorm.weight, self.layernorm.bias, 1e-05, 1e-05)
        v2 = v1.reshape(2, 2)
        v1 = self.layernorm(x1)
        return v1



func = Model().to('cuda')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
layer_norm(): argument 'normalized_shape' (position 2) must be tuple of ints, not Parameter

jit:
layer_norm(): argument 'normalized_shape' (position 2) must be tuple of ints, not Parameter
'''