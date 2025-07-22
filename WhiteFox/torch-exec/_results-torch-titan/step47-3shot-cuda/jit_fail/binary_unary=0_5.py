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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv4 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x1, x2, x3, x4):
        v1 = self.conv1(x1)
        v2 = (v1 + x2)
        v3 = self.conv3(v2)
        v4 = (v3 + x3)
        v5 = (v4 + x4)
        v6 = self.conv2(v5)
        v7 = (v6 + v1)
        v8 = torch.relu(v7)
        v9 = self.conv4(v8)
        v10 = (v9 + v1)
        v11 = torch.relu(v10)
        return v11




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 16, 64, 64)



x3 = torch.randn(1, 16, 16, 16)



x4 = torch.randn(1, 16, 32, 32)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (16) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 16, 16, 16))), **{}):
Attempting to broadcast a dimension of length 16 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 16, 16]); but expected shape should be broadcastable to [1, 16, 64, 64]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''