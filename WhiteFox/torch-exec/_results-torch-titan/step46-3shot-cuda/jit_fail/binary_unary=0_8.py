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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x1, x2, x3):
        v0 = x1.mean((2, 3))
        v1 = self.conv1(v0)
        v2 = v1.min((2, 3))
        v3 = self.conv2(v2)
        v4 = (v3 * x2)
        v5 = torch.relu(v4)
        v6 = (v2 + v5)
        v7 = torch.relu(v6)
        v8 = v7.amin((2, 3))
        v9 = self.conv3(v8)
        v10 = (v9 + x3)
        v11 = torch.relu(v10)
        v12 = (v10 - v11)
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 16, 64, 64)



x3 = torch.randn(1, 16, 64, 64)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 16]

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 16)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 16]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''