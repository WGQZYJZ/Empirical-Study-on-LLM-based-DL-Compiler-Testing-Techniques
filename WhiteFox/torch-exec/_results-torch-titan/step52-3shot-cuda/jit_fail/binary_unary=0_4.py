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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2, x3, x4, x5):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1, padding=1)
        v3 = self.conv3(x1, dilation=2)
        v4 = (v1 + x2)
        v5 = torch.nn.functional.relu(v4)
        v6 = (v5 + v3)
        v7 = self.conv2(v6)
        v8 = (v7 + v6)
        v9 = torch.nn.functional.relu(v8)
        v10 = (v9 + v6)
        v11 = torch.flatten(v10, 1)
        v12 = self.conv2(v11)
        v13 = torch.relu(v11)
        return v13




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 16, 64, 64)



x3 = torch.randn(1, 16, 64, 64)



x4 = torch.randn(1, 16, 64, 64)



x5 = torch.randn(1, 16, 64, 64)


test_inputs = [x1, x2, x3, x4, x5]

# JIT_FAIL
'''
direct:
forward() got an unexpected keyword argument 'padding'

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64)),), **{'padding': 1}):
forward() got an unexpected keyword argument 'padding'

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''