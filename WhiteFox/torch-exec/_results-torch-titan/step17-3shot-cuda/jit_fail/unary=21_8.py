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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(77, 109, 1, stride=1)
        self.conv2 = torch.nn.Conv2d(97, 82, 21, stride=18, padding=12, dilation=14)
        self.conv3 = torch.nn.Conv3d(8, 40, 7, stride=3, dilation=10, groups=2)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.relu(v1)
        v3 = self.conv2(v2)
        v4 = self.relu(v3)
        v5 = self.conv3(v4)
        v6 = torch.tanh(v5)
        return v6




func = ModelTanh().to('cuda')



x = torch.randn(6, 8, 56, 56, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [6, 8, 56, 56, 10]

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(6, 8, 56, 56, 10)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [6, 8, 56, 56, 10]

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''