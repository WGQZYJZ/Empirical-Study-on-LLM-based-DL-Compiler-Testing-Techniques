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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(4, 6, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = (v1 + v2)
        v4 = self.conv3(v3)
        v5 = (v4 + 3)
        v6 = torch.clamp_min(v5, 0)
        v7 = torch.clamp_max(v6, 6)
        v8 = (v4 * v7)
        v9 = (v8 / 6)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)), FakeTensor(..., device='cuda:0', size=(1, 4, 66, 66))), **{}):
Attempting to broadcast a dimension of length 4 at -3! Mismatching argument at index 1 had torch.Size([1, 4, 66, 66]); but expected shape should be broadcastable to [1, 8, 66, 66]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''