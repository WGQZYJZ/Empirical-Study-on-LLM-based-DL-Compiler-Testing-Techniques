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
        self.conv = torch.nn.Conv2d(32, 32, 1, stride=2, padding=6)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min=0.0)
        v3 = torch.clamp_max(v2, max=1.0)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 32, 100, 10, 100)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 32, 100, 10, 100]

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 32, 100, 10, 100)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 32, 100, 10, 100]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''