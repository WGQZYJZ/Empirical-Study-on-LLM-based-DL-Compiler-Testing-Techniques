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
        self.conv1 = torch.nn.Conv2d(16, 4, 25, stride=3, padding=0, dilation=2, groups=1)
        self.conv2 = torch.nn.Conv2d(4, 4, 5, stride=2, padding=5, dilation=2, groups=2)

    def forward(self, x2):
        v1 = self.conv1(x2)
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
        v13 = (v1 * v1)
        v14 = (v3 * v1)
        v15 = (v4 * 0.044715)
        v16 = (v1 + v5)
        v17 = (v6 * 0.7978845608028654)
        v18 = torch.tanh(v17)
        v19 = (v18 + 1)
        v20 = (v10 + v13)
        v21 = (v16 * 0.7978845608028654)
        v22 = torch.tanh(v21)
        v23 = (v22 + 1)
        v24 = (v10 + v14)
        v25 = (v16 * 0.7978845608028654)
        v26 = torch.tanh(v25)
        v27 = (v26 + 1)
        v28 = (v10 + v15)
        v29 = (v11 + v22)
        v30 = (v29 * v29)
        v31 = (v22 + 1)
        v32 = ((v10 + v30) * v31)
        return v28




func = Model().to('cuda')



x2 = torch.randn(1, 100, 200, 5)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 16, 25, 25], expected input[1, 100, 200, 5] to have 16 channels, but got 100 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 100, 200, 5)),), **{}):
Given groups=1, weight of size [4, 16, 25, 25], expected input[1, 100, 200, 5] to have 16 channels, but got 100 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''