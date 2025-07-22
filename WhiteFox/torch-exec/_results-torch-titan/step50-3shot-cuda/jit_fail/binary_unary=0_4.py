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
        self.conv1 = torch.nn.Conv2d(256, 256, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(2, 3, 5, stride=1, padding=2)
        self.conv3 = torch.nn.Conv2d(3, 256, 7, stride=1, padding=3)

    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = (v1 + v2)
        v4 = self.conv3(v3)
        v5 = torch.relu(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 256, 14, 14)



x2 = torch.randn(1, 2, 64, 64)



x3 = torch.randn(1, 256, 14, 14)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (14) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 256, 14, 14)), FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 64, 64]); but expected shape should be broadcastable to [1, 256, 14, 14]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''