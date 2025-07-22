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

    def __init__(self, out, in_features, bias=False):
        super().__init__()
        self.linear = torch.nn.Linear(in_features, out, bias=bias)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        return self.linear(v1)



out = 1
in_features = 1

func = Model(out, in_features).to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x2 and 1x1)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)),), **{}):
a and b must have same reduction dim, but got [2, 2] X [1, 1].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''