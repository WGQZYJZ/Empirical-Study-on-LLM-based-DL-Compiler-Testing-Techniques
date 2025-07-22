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
        self.conv1 = torch.nn.Conv2d(3, 1, 1, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(1, 5, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(5, 3, 1, stride=2, padding=1)

    def forward(self, x):
        negative_slope = 0.1
        v1 = self.conv1(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        v5 = self.conv2(v4)
        v6 = v5 > 0
        v7 = v5 * negative_slope
        v8 = torch.where(v6, v5, v7)
        v9 = self.conv3(v8)
        v10 = v9 > 0
        v11 = v5 * -0.1
        v12 = torch.where(v10, v9, v11)
        return v12



func = Model().to('cpu')


x1 = torch.randn(2, 3, 220, 220)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (58) must match the size of tensor b (113) at non-singleton dimension 3

jit:
Failed running call_function <built-in method where of type object at 0x70270d596ec0>(*(FakeTensor(..., size=(s0, 3, (((s2 + 1)//4)) + 3, (((s3 + 1)//4)) + 3),
           dtype=torch.bool), FakeTensor(..., size=(s0, 3, (((s2 + 1)//4)) + 3, (((s3 + 1)//4)) + 3)), FakeTensor(..., size=(s0, 5, (((s2 + 1)//2)) + 3, (((s3 + 1)//2)) + 3))), **{}):
Attempting to broadcast a dimension of length (((s3 + 1)//2)) + 3 at -1! Mismatching argument at index 2 had torch.Size([s0, 5, (((s2 + 1)//2)) + 3, (((s3 + 1)//2)) + 3]); but expected shape should be broadcastable to [s0, 3, (((s2 + 1)//4)) + 3, (((s3 + 1)//4)) + 3]

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''