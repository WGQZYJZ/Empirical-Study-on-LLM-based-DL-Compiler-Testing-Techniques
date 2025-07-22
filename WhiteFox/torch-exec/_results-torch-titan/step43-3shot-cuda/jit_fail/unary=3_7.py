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
        self.conv = torch.nn.Conv2d(1, 100, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(100, 12, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(12, 70, 2, stride=2, padding=0)
        self.conv4 = torch.nn.Conv2d(70, 82, 5, stride=1, padding=2)
        self.conv5 = torch.nn.Conv2d(82, 3, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = torch.tanh(v6)
        v8 = self.conv2(v7)
        v9 = torch.atanh(v8)
        v10 = self.conv3(v9)
        v11 = (v10 * 0.5)
        v12 = self.conv4(v11)
        v13 = (v12 * 0.7071067811865476)
        v14 = torch.erf(v13)
        v15 = (v14 + 1)
        v16 = (v11 * v15)
        return v16




func = Model().to('cuda')



x1 = torch.randn(1, 1, 45, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (70) must match the size of tensor b (82) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 70, 22, 16)), FakeTensor(..., device='cuda:0', size=(1, 82, 22, 16))), **{}):
Attempting to broadcast a dimension of length 82 at -3! Mismatching argument at index 1 had torch.Size([1, 82, 22, 16]); but expected shape should be broadcastable to [1, 70, 22, 16]

from user code:
   File "<string>", line 41, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''