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
    __constant_size0__ = 9223372036854775807
    __constant_size1__ = 9223372036854775807
    __constant_size2__ = 9223372036854775807

    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2, x3], dim=1)
        v2 = v1[:, Model.__constant_size0__:]
        v3 = v2[:, Model.__constant_size1__:]
        return torch.cat([v1, v3], dim=1)


func = Model().to('cpu')

x1 = 1
x2 = 1
x3 = 1

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got int

jit:
expected Tensor as element 0 in argument 0, but got int
'''