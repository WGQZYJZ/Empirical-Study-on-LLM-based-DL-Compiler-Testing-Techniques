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
        self.conv = torch.nn.Conv2d(1, 16, 7, stride=2, padding=0)
        self.bn0 = torch.nn.BatchNorm2d(16)
        self.conv01 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=0)
        self.conv02 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv03 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=2)
        self.conv04 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=3)
        self.conv05 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=4)
        self.conv06 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=5)
        self.conv07 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=6)
        self.conv08 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=7)
        self.conv09 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=8)
        self.conv10 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=9)
        self.bn10 = torch.nn.BatchNorm2d(16)
        self.conv11 = torch.nn.Conv2d(16, 32, 3, stride=2, padding=0)
        self.conv12 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=0)
        self.conv13 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv01(v1)
        v3 = self.conv02(v1)
        v4 = self.conv03(v1)
        v5 = self.conv04(v1)
        v6 = self.conv05(v1)
        v7 = self.conv06(v1)
        v8 = self.conv07(v1)
        v9 = self.conv08(v1)
        v10 = self.conv09(v1)
        v11 = self.conv10(v1)
        v12 = v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10 + v11
        v13 = self.conv11(v12)
        v14 = self.conv12(v13)
        v15 = self.conv13(v13)
        v16 = self.bn(v1)
        v17 = v16 + v12 + v14 + v15
        v18 = torch.relu(v17)
        return v18



func = Model().to('cuda')


x1 = torch.randn(1, 1, 50, 97)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (44) must match the size of tensor b (46) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 20, 44)), FakeTensor(..., device='cuda:0', size=(1, 16, 22, 46))), **{}):
Attempting to broadcast a dimension of length 46 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 22, 46]); but expected shape should be broadcastable to [1, 16, 20, 44]

from user code:
   File "<string>", line 46, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''