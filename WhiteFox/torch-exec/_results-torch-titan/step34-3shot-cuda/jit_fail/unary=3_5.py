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
        self.conv = torch.nn.Conv2d(3, 4, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.7071067811865476)
        v3 = torch.max(x1, v2)
        v4 = self.conv(v3)
        v5 = (v4 * 0.7071067811865476)
        v6 = torch.max(x1, v5)
        v7 = self.conv(v6)
        v8 = (v7 * 0.7071067811865476)
        v9 = torch.max(x1, v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 3, 119, 154)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in method max of type object at 0x7467e52699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 119, 154)), FakeTensor(..., device='cuda:0', size=(1, 4, 119, 154))), **{}):
Attempting to broadcast a dimension of length 4 at -3! Mismatching argument at index 1 had torch.Size([1, 4, 119, 154]); but expected shape should be broadcastable to [1, 3, 119, 154]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''