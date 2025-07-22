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
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1[0] - 4)
        v3 = (v1[1] - 4)
        v4 = torch.max(v2, v3)
        v5 = ((v1[0] * v1[1]) * v4)
        return v5



func = Model().to('cuda')



x1 = torch.randn(2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
index 1 is out of bounds for dimension 0 with size 1

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(1,)), 1), **{}):
index 1 is out of bounds for dimension 0 with size 1

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''