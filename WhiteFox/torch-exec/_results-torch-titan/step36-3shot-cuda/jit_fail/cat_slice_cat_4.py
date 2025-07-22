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

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        _start = (v1.shape[1] - 9223372036854775807)
        _end = v1.shape[1]
        v2 = v1[:, _start:_end]
        v3 = v2[:, 0, 512, 512]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 1, 8, 24)



x2 = torch.randn(1, 1, 8, 24)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
index 512 is out of bounds for dimension 2 with size 8

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 8, 24)), (slice(None, None, None), 0, 512, 512)), **{}):
index 512 is out of bounds for dimension 2 with size 8

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''