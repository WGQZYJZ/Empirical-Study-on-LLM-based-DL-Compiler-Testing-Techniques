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
        self.conv1 = torch.nn.Conv3d(96, 96, 3, stride=(1, 1, 1), padding=(1, 1, 1))
        self.conv5 = torch.nn.Conv3d(128, 4, 3, stride=(1, 1, 1), padding=(1, 1, 1))
        self.conv6 = torch.nn.Conv2d(3, 64, 3, 1, 1)
        self.conv7 = torch.nn.Conv2d(64, 32, 3, 1, 1)
        self.relu = torch.nn.ReLU()
        self.bn = torch.nn.BatchNorm2d(32)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv6(v1)
        v3 = self.relu(v2)
        v4 = self.conv7(v3)
        v5 = self.bn(v4)
        v6 = self.conv5(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 96, 32, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 96, 32, 32, 32]

jit:
Failed running call_module L__self___conv6(*(FakeTensor(..., device='cuda:0', size=(1, 96, 32, 32, 32)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [1, 96, 32, 32, 32]

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''