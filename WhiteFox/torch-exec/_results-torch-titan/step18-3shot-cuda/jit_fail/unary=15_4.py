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
        self.dense1 = torch.nn.Linear(2, 10)
        self.conv1 = torch.nn.Conv2d(3, 10, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 10, 1, stride=3, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 10, 2, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.dense1(x1)
        v2 = F.relu(v1)
        v3 = (self.conv1(x1) + v2)
        v4 = (self.conv2(x1) + torch.max(v2, v3))
        v5 = torch.max(v2, v3, v4)
        v6 = torch.relu(v5)
        v7 = (self.conv3(x1) + v6)
        v8 = torch.relu(v7)
        v9 = torch.max(v5, v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 2]

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 2)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 2]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''