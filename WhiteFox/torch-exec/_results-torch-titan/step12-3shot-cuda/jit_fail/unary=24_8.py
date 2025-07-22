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
        self.conv1 = torch.nn.Conv3d(8, 32, 4, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(32, 32, 2, stride=1, padding=1)

    def forward(self, x):
        negative_slope = 1
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = (v2 > 0)
        v4 = (v2 * negative_slope)
        v5 = torch.where(v3, v2, v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(4, 8, 56, 56, 56)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [4, 32, 59, 59, 59]

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(4, 32, 59, 59, 59)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [4, 32, 59, 59, 59]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''