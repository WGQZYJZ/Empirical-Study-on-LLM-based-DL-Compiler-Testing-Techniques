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
        self.conv_t = torch.nn.ConvTranspose2d(1, 32, 6, stride=3, padding=2)
        self.conv = torch.nn.Conv2d(32, 17, 6, stride=2, padding=2)

    def forward(self, x):
        v1 = self.conv_t(x)
        v2 = self.conv(v1)
        v3 = x < v1
        v4 = torch.where(v3, v2, x)
        return v4



func = Model().to('cpu')


x = torch.randn(4, 1, 20, 20, device='cuda')

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (20) must match the size of tensor b (59) at non-singleton dimension 3

jit:
Failed running call_function <built-in function lt>(*(FakeTensor(..., size=(4, 1, 20, 20)), FakeTensor(..., size=(4, 32, 59, 59))), **{}):
Attempting to broadcast a dimension of length 59 at -1! Mismatching argument at index 1 had torch.Size([4, 32, 59, 59]); but expected shape should be broadcastable to [4, 1, 20, 20]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''