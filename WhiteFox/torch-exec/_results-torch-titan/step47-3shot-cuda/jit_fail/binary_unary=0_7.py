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
        self.conv1 = torch.nn.Conv2d(16, 64, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(64, 128, 3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(128, 16, 3, stride=2, padding=1)

    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v3 = (v1 * x2)
        v4 = torch.relu(v3)
        v5 = (v1 + v4)
        v6 = torch.relu(v5)
        v7 = (v1 + v6)
        v8 = self.conv2(v7)
        v10 = (v8 * x3)
        v11 = torch.relu(v10)
        v12 = (v8 + v11)
        v13 = torch.relu(v12)
        v14 = (v8 + self.conv3(v13))
        v16 = (v14 * x1)
        v17 = torch.relu(v16)
        v18 = (v14 + v17)
        v19 = torch.relu(v18)
        return v19




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 64, 32, 64)



x3 = torch.randn(1, 128, 32, 32)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (32) at non-singleton dimension 2

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 64, 32, 64))), **{}):
Attempting to broadcast a dimension of length 32 at -2! Mismatching argument at index 1 had torch.Size([1, 64, 32, 64]); but expected shape should be broadcastable to [1, 64, 64, 64]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''