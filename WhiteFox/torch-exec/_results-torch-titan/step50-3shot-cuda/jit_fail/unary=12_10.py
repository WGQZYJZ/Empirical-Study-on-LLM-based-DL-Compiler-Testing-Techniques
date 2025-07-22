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
        self.linear_1 = torch.nn.Linear(256, 128)
        self.linear_2 = torch.nn.Linear(128, 64)
        self.linear_3 = torch.nn.Linear(64, 32)

    def forward(self, x1):
        v1 = self.linear_1(x1)
        v2 = F.relu(v1)
        v3 = self.linear_2(v2)
        v4 = F.relu(v3)
        v5 = self.linear_3(v4)
        v6 = F.relu(v5)
        v7 = (v1 * v5)
        v8 = (((v2 + v4) + v6) + v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (128) must match the size of tensor b (32) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 128)), FakeTensor(..., device='cuda:0', size=(1, 32))), **{}):
Attempting to broadcast a dimension of length 32 at -1! Mismatching argument at index 1 had torch.Size([1, 32]); but expected shape should be broadcastable to [1, 128]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''