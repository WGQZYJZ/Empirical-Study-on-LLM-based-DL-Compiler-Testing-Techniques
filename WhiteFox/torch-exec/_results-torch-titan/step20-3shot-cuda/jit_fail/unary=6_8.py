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
        self.conv = torch.nn.Conv2d(3, 4, 2, stride=1, padding=2, dilation=3)
        self.avgpool = torch.nn.AvgPool2d(6, stride=2, padding=3)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.exp()
        v3 = v2.add(3.0)
        v4 = v3.mul(13)
        v5 = v4.clamp(min=0, max=12)
        v6 = (v1 / v5)
        v7 = v6.max(dim=3)
        v8 = v7[1].unsqueeze(0)
        v9 = v8.min(dim=2)
        v10 = v9[1].unsqueeze(0)
        v11 = v10.mul(21821)
        v12 = (v11.unsqueeze((- 1)) * v11.unsqueeze(0)).sum()
        v13 = v12.sqrt()
        return v13




func = Model().to('cuda')



x1 = torch.randn(3, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (65) must match the size of tensor b (3) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 3, 65, 1), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(1, 1, 1, 3, 65), dtype=torch.int64)), **{}):
Attempting to broadcast a dimension of length 3 at -2! Mismatching argument at index 1 had torch.Size([1, 1, 1, 3, 65]); but expected shape should be broadcastable to [1, 1, 3, 65, 65]

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''