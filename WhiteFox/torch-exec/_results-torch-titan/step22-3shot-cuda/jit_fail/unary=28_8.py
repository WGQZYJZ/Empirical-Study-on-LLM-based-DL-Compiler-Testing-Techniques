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
        self.linear = torch.nn.Linear(3, 16, bias=False)

    def forward(self, x1, min_v, max_v):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_v)
        v3 = torch.clamp_max(v2, max_v)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 3)



x2 = torch.randn(1, 3)

min_v = 1

test_inputs = [x1, x2, min_v]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in method clamp_min of type object at 0x7a0b8ec699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 16)), FakeTensor(..., device='cuda:0', size=(1, 3))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([1, 3]); but expected shape should be broadcastable to [1, 16]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''