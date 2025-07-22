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
        self.conv1 = torch.nn.Conv2d(64, 64, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)
        self.bn = torch.nn.BatchNorm2d(64)

    def forward(self, x1, x2):
        v1 = (x1 + x2)
        v2 = self.conv1(v1)
        v3 = (v2 + x2)
        v4 = self.conv2(v3)
        v5 = self.bn(v4)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 64, 64, 64)



x2 = torch.randn(1, 64, 16, 16)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (16) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 64, 16, 16))), **{}):
Attempting to broadcast a dimension of length 16 at -1! Mismatching argument at index 1 had torch.Size([1, 64, 16, 16]); but expected shape should be broadcastable to [1, 64, 64, 64]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''