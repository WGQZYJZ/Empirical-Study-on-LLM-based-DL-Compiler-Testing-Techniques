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
        self.conv1 = torch.nn.Conv2d(10, 16, 3, stride=3, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 32, 3, stride=1)
        self.conv3 = torch.nn.Conv2d(32, 64, 3, stride=1, dilation=3)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * v1)
        v4 = (v3 * v1)
        v5 = (v4 * 0.044715)
        v6 = (v1 + v5)
        v7 = (v6 * 0.7978845608028654)
        v8 = torch.tanh(v7)
        v9 = (v8 + 1)
        v10 = (v2 * v9)
        v11 = self.conv2(v10)
        v12 = (v11 * 0.5)
        v13 = (v11 * v11)
        v14 = (v13 * v11)
        v15 = (v14 * 0.044715)
        v16 = (v11 + v15)
        v17 = (v16 * 0.7978845608028654)
        v18 = torch.tanh(v17)
        v19 = (v18 + 1)
        v20 = (v12 * v19)
        v21 = self.conv3(x1)
        v22 = (v21 * 0.5)
        v23 = (v21 * v1)
        v24 = (v23 * v1)
        v25 = (v24 * 0.044715)
        v26 = (v21 + v25)
        v27 = (v26 * 0.7978845608028654)
        v28 = torch.tanh(v17)
        v29 = (v18 + 1)
        v30 = (v2 * v9)
        return v30




func = Model().to('cuda')



x1 = torch.randn(1, 10, 128, 255)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 32, 3, 3], expected input[1, 10, 128, 255] to have 32 channels, but got 10 channels instead

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1, 10, 128, 255)),), **{}):
Given groups=1, weight of size [64, 32, 3, 3], expected input[1, 10, 128, 255] to have 32 channels, but got 10 channels instead

from user code:
   File "<string>", line 44, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''