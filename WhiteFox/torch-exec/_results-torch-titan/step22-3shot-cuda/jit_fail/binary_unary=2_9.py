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
        self.conv1 = torch.nn.Conv2d(3, 16, 6, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 10, 6, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 - 0.5)
        v3 = F.relu(v2)
        v4 = torch.flatten(v3)
        v5 = self.conv2(v4)
        v6 = (v5 - 0.6)
        v7 = F.relu(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [13456]

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(13456,)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [13456]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''