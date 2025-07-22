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
        self.conv1 = torch.nn.Conv2d(16, 32, 4, stride=1)
        self.conv2 = torch.nn.Conv2d(256, 64, 4, stride=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = torch.max(v6)
        v8 = self.conv2(v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: []

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=()),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: []

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''