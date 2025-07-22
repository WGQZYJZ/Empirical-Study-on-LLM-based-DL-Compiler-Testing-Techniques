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

    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv2d(8, 4, 3, stride=1, padding=1)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = torch.mean(x1)
        v2 = v1.expand(x1.size())
        v3 = self.conv(v2)
        v4 = torch.clamp_min((v3 + v2), self.min)
        v5 = torch.clamp_max((v4 + v3), self.max)
        return v5




min = (- 0.8)


max = 0.7


func = Model(min, max).to('cuda')



x1 = torch.randn(1, 8, 100, 100)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (4) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 4, 100, 100)), FakeTensor(..., device='cuda:0', size=(1, 8, 100, 100))), **{}):
Attempting to broadcast a dimension of length 8 at -3! Mismatching argument at index 1 had torch.Size([1, 8, 100, 100]); but expected shape should be broadcastable to [1, 4, 100, 100]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''