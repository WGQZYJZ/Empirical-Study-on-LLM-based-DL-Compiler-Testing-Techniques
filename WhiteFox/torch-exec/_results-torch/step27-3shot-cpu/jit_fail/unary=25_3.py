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

    def __init__(self, negative_slope):
        super().__init__()
        self.__out_features = negative_slope

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, None)
        v2 = v1 > 0
        v3 = v1 * self.__out_features
        v4 = torch.where(v2, v1, v3)
        return v4


negative_slope = 1

func = Model(negative_slope).to('cpu')


x1 = torch.randn(2, 2, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear(): argument 'weight' (position 2) must be Tensor, not NoneType

jit:
linear(): argument 'weight' (position 2) must be Tensor, not NoneType
'''