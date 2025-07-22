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
        self.conv1 = torch.nn.Conv2d(3, 16, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 8, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.mean(v1, dim=[(- 1), (- 2)])
        v3 = torch.squeeze(v2, dim=(- 1))
        v4 = (v3 - 5.6)
        v5 = F.relu(v4)
        v6 = self.conv2(v5)
        v7 = torch.sum(v6, dim=[(- 1), (- 2)])
        v8 = torch.squeeze(v7, dim=(- 1))
        v9 = torch.mean(v8, dim=[(- 1), (- 2)])
        v10 = (v9 - 7)
        v11 = F.relu(v10)
        return v11




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 16]

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 16)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 16]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''