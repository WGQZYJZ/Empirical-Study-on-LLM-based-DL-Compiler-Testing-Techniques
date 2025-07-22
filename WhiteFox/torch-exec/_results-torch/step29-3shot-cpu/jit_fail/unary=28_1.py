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

    def __init__(self, __min_value__, __max_value__):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, m.weight, m.bias)
        v2 = torch.clamp_max(v1, __max_value__)
        v3 = torch.clamp(__min_value__ + v2)
        return v3


__min_value__ = 1
__max_value__ = 1

func = Model(__min_value__, __max_value__).to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'm' is not defined

jit:
NameError: name 'm' is not defined

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''