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
        self.conv2d = nn.Conv2d(3, 3, 1, 1, dilation=2, padding=4)
        self.conv2d1 = nn.Conv2d(3, 3, 1, 1)
        self.conv2d2 = nn.Conv2d(3, 3, 1, 1, dilation=2)
        self.conv2d3 = nn.Conv2d(3, 3, 1, 1, padding=5)
        self.conv2d4 = nn.Conv2d(3, 3, 1, 1)

    def forward(self, x):
        t1 = self.conv2d(x)
        t2 = self.conv2d1(x)
        t3 = self.conv2d2(x)
        t4 = self.conv2d3(x)
        t5 = self.conv2d4(x)
        t6 = (((t1 * t2) - (t3 * t4)) + t5)
        return t6




func = Model().to('cuda')



x = torch.randn(1, 3, 128, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (72) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 136, 72)), FakeTensor(..., device='cuda:0', size=(1, 3, 128, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([1, 3, 128, 64]); but expected shape should be broadcastable to [1, 3, 136, 72]

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''