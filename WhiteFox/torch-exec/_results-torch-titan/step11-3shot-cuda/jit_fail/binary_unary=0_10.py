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
        self.conv = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.pool = torch.nn.AvgPool2d(3, 3)

    def forward(self, x1, x2, x3):
        v1 = self.conv(x1)
        v2 = (v1 + x2)
        v3 = torch.relu(v2)
        v4 = self.pool(v3)
        v5 = self.conv(v4)
        v6 = (v5 + x3)
        v7 = torch.relu(v6)
        v8 = self.pool(v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 16, 64, 64)



x3 = torch.randn(1, 16, 64, 64)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (21) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 21, 21)), FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 64, 64]); but expected shape should be broadcastable to [1, 16, 21, 21]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''