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

    def __init__(self, min, max):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 1, 14, stride=1, padding=7)
        self.conv2 = torch.nn.Conv2d(3, 1, 33, stride=2, padding=16)
        self.conv3 = torch.nn.Conv2d(3, 1, 53, stride=1, padding=26)
        self.min = min
        self.max = max

    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = self.conv3(x3)
        r1 = torch.clamp_min(v1, self.min)
        r2 = torch.clamp_min(v2, self.min)
        r3 = torch.clamp_min(v3, self.min)
        r4 = torch.clamp_max(r1, self.max)
        r5 = torch.clamp_max(r2, self.max)
        r6 = torch.clamp_max(r3, self.max)
        v4 = (r4 + r5)
        v5 = (r6 + v4)
        return v5




min = (- 0.33)


max = 0.98


func = Model(min, max).to('cuda')



x1 = torch.randn(1, 3, 32, 256)



x2 = torch.randn(1, 3, 128, 32)



x3 = torch.randn(1, 3, 64, 64)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (257) must match the size of tensor b (16) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 33, 257)), FakeTensor(..., device='cuda:0', size=(1, 1, 64, 16))), **{}):
Attempting to broadcast a dimension of length 16 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 64, 16]); but expected shape should be broadcastable to [1, 1, 33, 257]

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''