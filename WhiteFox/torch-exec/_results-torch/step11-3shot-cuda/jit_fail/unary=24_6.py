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
        self.conv1 = torch.nn.Conv2d(8, 8, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = v1 > 0
        v4 = v1 * -0.1
        v5 = torch.where(v3, v1, v4)
        v6 = v2 > 0
        v7 = v2 * -0.1
        v8 = torch.where(v6, v2, v7)
        return v5 + v8



func = Model().to('cuda')


x1 = torch.randn(1, 8, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (34) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32)), FakeTensor(..., device='cuda:0', size=(1, 8, 34, 34))), **{}):
Attempting to broadcast a dimension of length 34 at -1! Mismatching argument at index 1 had torch.Size([1, 8, 34, 34]); but expected shape should be broadcastable to [1, 8, 32, 32]

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''