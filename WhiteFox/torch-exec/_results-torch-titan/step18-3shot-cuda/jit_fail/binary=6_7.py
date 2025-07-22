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
        self.linear = torch.nn.Sequential(torch.nn.Linear(256, 128), torch.nn.BatchNorm1d(128))

    def forward(self, x1):
        (v1, _) = self.linear(x1)
        v2 = (v1 - other)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
not enough values to unpack (expected 2, got 1)

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(1, 128)), 1), **{}):
index 1 is out of bounds for dimension 0 with size 1

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''