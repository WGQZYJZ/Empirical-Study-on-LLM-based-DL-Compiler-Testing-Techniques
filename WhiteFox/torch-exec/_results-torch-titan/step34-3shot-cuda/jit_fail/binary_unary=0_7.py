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
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x5, x6):
        v1 = self.conv1(x5)
        v2 = self.conv2(x5)
        v3 = (v1 + x6)
        v4 = (v2 + x6)
        v5 = torch.relu(v3)
        v6 = torch.relu(v4)
        v7 = v5
        v8 = self.conv3(v6)
        v9 = (v8 + x6)
        v10 = torch.relu(v9)
        v11 = self.conv4(x5)
        v12 = self.conv1(x6)
        v13 = (v11 + v12)
        v14 = self.conv3(v13)
        v15 = (v14 * x5)
        return v15




func = Model().to('cuda')



x4 = torch.randn(1, 16, 64, 64)



x5 = torch.randn(1, 16, 64, 64)


test_inputs = [x4, x5]

# JIT_FAIL
'''
direct:
The size of tensor a (58) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 58, 58)), FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 64, 64]); but expected shape should be broadcastable to [1, 16, 58, 58]

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''