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
        self.conv1 = torch.nn.Conv2d(4, 16, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv1d(16, 16, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv1d(16, 32, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv1d(32, 16, 1, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(16, 8, 1, stride=1, padding=0)
        self.conv6 = torch.nn.Conv1d(8, 2, 1, stride=1, padding=0)
        self.conv7 = torch.nn.Conv2d(8, 4, (3, 3), stride=1, padding=1)
        self.conv8 = torch.nn.Conv1d(4, 8, 3, stride=1, padding=1)

    def forward(self, x):
        v0 = self.conv1(x)
        v1 = self.conv2(v0)
        v2 = self.conv3(v1)
        v3 = self.conv4(v2)
        v4 = self.conv5(v3)
        v5 = self.conv6(v4)
        v6 = self.conv7(v4)
        s = self.conv8(v6)
        v7 = torch.relu(v5)
        v7 = torch.flatten(v7, 1)
        v8 = torch.relu(s)
        v8 = torch.flatten(v8, 1)
        v9 = (v7 + v8)
        return v9




func = Model().to('cuda')



x = torch.randn(1, 4, 256, 256)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 16, 256, 256]

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 16, 256, 256)),), **{}):
Expected 2D (unbatched) or 3D (batched) input to conv1d, but got input of size: [1, 16, 256, 256]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''