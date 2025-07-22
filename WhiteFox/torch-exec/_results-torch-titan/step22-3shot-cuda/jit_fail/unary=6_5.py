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
        self.conv = torch.nn.Conv2d(4, 4, 1, stride=1, padding=1)
        self.depthwise = torch.nn.Conv2d(4, 4, 1, stride=1, padding=1, groups=4)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.depthwise(v1)
        v3 = (3 + v2)
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v6 = (v1 * v5)
        v7 = (v6 / 6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 4, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (34) must match the size of tensor b (36) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 4, 34, 34)), FakeTensor(..., device='cuda:0', size=(1, 4, 36, 36))), **{}):
Attempting to broadcast a dimension of length 36 at -1! Mismatching argument at index 1 had torch.Size([1, 4, 36, 36]); but expected shape should be broadcastable to [1, 4, 34, 34]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''