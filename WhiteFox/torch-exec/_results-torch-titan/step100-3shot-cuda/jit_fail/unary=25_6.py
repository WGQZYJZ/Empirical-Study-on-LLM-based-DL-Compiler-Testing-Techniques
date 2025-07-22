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

    def __init__(self, nelements, negative_slope):
        super().__init__()
        self.linear = torch.nn.Linear(nelements, 1, bias=False)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0)
        v3 = (v1 * self.negative_slope)
        v4 = torch.where(v2, v1, v3)
        return v4




nelements = (640 * 3072)


negative_slope = 0.1

func = Model(nelements, negative_slope).to('cuda')



x1 = torch.randn(1, 640, 3072)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (640x3072 and 1966080x1)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 640, 3072)),), **{}):
a and b must have same reduction dim, but got [640, 3072] X [1966080, 1].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''