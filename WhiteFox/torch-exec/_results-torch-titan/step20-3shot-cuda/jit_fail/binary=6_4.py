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
        self.linear = torch.nn.Linear(8, 16, bias=False)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 - 1)
        v3 = v2[0][0]
        v4 = v2[1][2]
        v5 = (v3 + v4)
        v6 = (v5 + 2)
        return v6



func = Model().to('cuda')



x1 = torch.randn(1, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
index 1 is out of bounds for dimension 0 with size 1

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(1, 16)), 1), **{}):
index 1 is out of bounds for dimension 0 with size 1

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''