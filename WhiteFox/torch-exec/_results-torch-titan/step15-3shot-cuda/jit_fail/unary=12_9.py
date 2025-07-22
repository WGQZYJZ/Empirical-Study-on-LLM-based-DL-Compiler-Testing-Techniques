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
        self.conv1 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 32, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = F.hardtanh(v1)
        v3 = torch.mul(v1, v2)
        v4 = self.conv2(v3)
        v5 = F.hardtanh(v4)
        v6 = torch.mul(v4, v5)
        v7 = (v5 * v6)
        v8 = self.conv3(v7)
        v9 = torch.mul(v8, v7)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (70) must match the size of tensor b (68) at non-singleton dimension 3

jit:
Failed running call_function <built-in method mul of type object at 0x7f91b9a699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 70, 70)), FakeTensor(..., device='cuda:0', size=(1, 32, 68, 68))), **{}):
Attempting to broadcast a dimension of length 68 at -1! Mismatching argument at index 1 had torch.Size([1, 32, 68, 68]); but expected shape should be broadcastable to [1, 32, 70, 70]

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''