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
        self.conv = torch.nn.Conv2d(3, 14, kernel_size=2, stride=2, padding=1, dilation=1, groups=1, bias=True)
        self.relu = torch.nn.ReLU(inplace=False)
        self.conv1 = torch.nn.Conv2d(14, 12, kernel_size=1, stride=1, padding=0, dilation=1, groups=1, bias=True)
        self.add = torch.add

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.relu(v1)
        v3 = self.conv1(v2)
        v4 = self.add(v1, v3)
        v5 = (v4 - 1.6)
        return v5




func = Model().to('cuda')



x = torch.randn(1, 3, 10, 12)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (14) must match the size of tensor b (12) at non-singleton dimension 1

jit:
Failed running call_function <built-in method add of type object at 0x7ffac94699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 14, 6, 7)), FakeTensor(..., device='cuda:0', size=(1, 12, 6, 7))), **{}):
Attempting to broadcast a dimension of length 12 at -3! Mismatching argument at index 1 had torch.Size([1, 12, 6, 7]); but expected shape should be broadcastable to [1, 14, 6, 7]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''