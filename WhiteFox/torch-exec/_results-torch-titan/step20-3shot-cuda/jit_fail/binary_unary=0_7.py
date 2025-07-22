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
        self.conv = torch.nn.Conv2d(32, 64, 3, stride=2, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = self.conv(v2)
        v4 = torch.relu(v3)
        v5 = self.conv(v4)
        v6 = torch.relu(v5)
        v7 = self.conv(v6)
        v8 = torch.relu(v7)
        v9 = self.conv(v8)
        v10 = torch.relu(v9)
        v11 = self.conv(v10)
        v12 = torch.relu(v11)
        v13 = (v1 + v12)
        v14 = torch.relu(v13)
        v15 = (v14 + x2)
        v16 = torch.relu(v15)
        return v16




func = Model().to('cuda')



x1 = torch.randn(1, 32, 128, 128)



x2 = torch.randn(1, 32, 128, 128)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 32, 3, 3], expected input[1, 64, 64, 64] to have 32 channels, but got 64 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 64, 64, 64)),), **{}):
Given groups=1, weight of size [64, 32, 3, 3], expected input[1, 64, 64, 64] to have 32 channels, but got 64 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''