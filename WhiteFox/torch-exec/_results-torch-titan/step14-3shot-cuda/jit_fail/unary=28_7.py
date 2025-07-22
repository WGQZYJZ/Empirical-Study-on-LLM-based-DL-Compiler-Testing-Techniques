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
        self.linear = torch.nn.Linear(64, 3)

    def forward(self, x1, min_op=0.5, max_op=1.5):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_op)
        v3 = torch.clamp_max(v2, max_op)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 64)



x2 = torch.randn(1, 16)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (16) at non-singleton dimension 1

jit:
Failed running call_function <built-in method clamp_min of type object at 0x73ab102699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3)), FakeTensor(..., device='cuda:0', size=(1, 16))), **{}):
Attempting to broadcast a dimension of length 16 at -1! Mismatching argument at index 1 had torch.Size([1, 16]); but expected shape should be broadcastable to [1, 3]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''