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
        self.c1 = torch.nn.Conv2d(1, 2, kernel_size=1, stride=1, padding=1)
        self.c2 = torch.nn.Conv2d(1, 1, kernel_size=2, stride=1, padding=1)
        self.c3 = torch.nn.Conv2d(1, 1, kernel_size=3, stride=1, padding=1)
        self.c4 = torch.nn.Conv2d(1, 1, kernel_size=4, stride=1, padding=1)
        self.c5 = torch.nn.Conv2d(1, 1, kernel_size=5, stride=1, padding=1)
        self.a1 = torch.nn.Sigmoid()
        self.b1 = torch.nn.Tanh()
        self.add = torch.add

    def forward(self, x1):
        v1 = self.c1(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1.mul_(v2)
        v4 = self.c2(x1)
        v5 = torch.tanh(v4)
        v6 = v3.mul_(v5)
        v7 = self.c3(x1)
        v8 = torch.sigmoid(v7)
        v9 = v6.mul_(v8)
        v10 = self.c4(x1)
        v11 = torch.tanh(v10)
        v12 = v9.mul_(v11)
        v13 = self.c5(x1)
        v14 = torch.sigmoid(v13)
        v15 = v12.mul_(v14)
        v16 = self.b1(v15)
        v17 = self.a1(v15)
        v18 = v13.mul_(v16).clone()
        v19 = v14.add_(v18).mul_(v17)
        return v19



func = Model().to('cuda')


x1 = torch.randn(1, 1, 1, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 3

jit:
Failed running call_method mul_(*(FakeTensor(..., device='cuda:0', size=(1, 2, 3, 3)), FakeTensor(..., device='cuda:0', size=(1, 1, 2, 2))), **{}):
Attempting to broadcast a dimension of length 2 at -1! Mismatching argument at index 1 had torch.Size([1, 1, 2, 2]); but expected shape should be broadcastable to [1, 2, 3, 3]

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''