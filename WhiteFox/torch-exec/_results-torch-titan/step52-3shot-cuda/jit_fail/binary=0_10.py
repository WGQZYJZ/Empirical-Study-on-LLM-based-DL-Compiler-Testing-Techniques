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
        self.conv = torch.nn.Conv2d(32, 5, 1, stride=1, padding=1)

    def forward(self, x1, other=0, padding1=1, padding2=1, groups=0):
        v1 = self.conv(x1)
        if (other == 0):
            other = torch.randn(v1.shape)
        if (padding1 == 1):
            x1 = F.pad(x1, (padding2, padding2, padding2, padding2), 'constant', 0)
        v2 = (x1 + other)
        if (groups == 0):
            groups = 16
        v3 = F.conv2d(v2, torch.randn(16, 5, 3, 3), stride=1, padding=1, groups=groups, dilation=2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 32, 56, 56)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (5) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 58, 58)), FakeTensor(..., size=(1, 5, 58, 58))), **{}):
Attempting to broadcast a dimension of length 5 at -3! Mismatching argument at index 1 had torch.Size([1, 5, 58, 58]); but expected shape should be broadcastable to [1, 32, 58, 58]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''