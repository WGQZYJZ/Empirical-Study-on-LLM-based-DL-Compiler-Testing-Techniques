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
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, torch.randn(50))
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


negative_slope = 1
func = Model(0.1).to('cpu')


x1 = torch.randn(10, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
size mismatch, got input (1920), mat (1920x64), vec (50)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(10, 3, 64, 64)), FakeTensor(..., size=(50,))), **{}):
size mismatch, got input (1920x64), vec (50)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''