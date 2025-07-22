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
        self.convolution = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
        self.pool = torch.nn.AvgPool3d(3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.convolution(x1)
        t1 = self.pool(v1)
        t2 = (3 + t1)
        t3 = torch.clamp_min(t2, 0)
        t4 = torch.clamp_max(t3, 6)
        t5 = (t1 * t4)
        t6 = (t5 / 6)
        return t6.unsqueeze((- 1))




func = Model().to('cuda')



x1 = torch.randn(1, 3, 30, 104, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 3, 30, 104, 256]

jit:
Failed running call_module L__self___convolution(*(FakeTensor(..., device='cuda:0', size=(1, 3, 30, 104, 256)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 3, 30, 104, 256]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''