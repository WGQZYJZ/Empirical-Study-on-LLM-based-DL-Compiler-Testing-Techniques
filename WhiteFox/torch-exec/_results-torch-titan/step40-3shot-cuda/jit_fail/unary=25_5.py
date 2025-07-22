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
        v1 = torch.nn.functional.linear(x1, weight=None, bias=None)
        v2 = (v1 > 0)
        v3 = (v1 * self.negative_slope)
        v4 = torch.where(v2, v1, v3)
        return v4



negative_slope = 1
func = Model(0.05).to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear(): argument 'weight' must be Tensor, not NoneType

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),), **{'weight': None, 'bias': None}):
linear(): argument 'weight' must be Tensor, not NoneType

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''