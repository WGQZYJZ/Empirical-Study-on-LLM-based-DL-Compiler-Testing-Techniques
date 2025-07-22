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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 4, 3, bias=False)
        self.relu = torch.nn.ReLU()
        self.conv = torch.nn.Conv2d(12, 3, 1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.relu(v1)
        v3 = (v1 * 0.5)
        v4 = ((v1 * v1) * v1)
        v5 = (v4 * 0.044715)
        v6 = (v1 + v5)
        v7 = (v6 * 0.7978845608028654)
        v8 = torch.tanh(v7)
        v9 = (v8 + 1)
        v10 = (v3 * v9)
        v11 = torch.cat((v2, v10), 1)
        v12 = self.conv(v11)
        return v12




func = Model().to('cuda')



x1 = torch.randn(2, 3, 5, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 12, 1, 1], expected input[2, 8, 7, 7] to have 12 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(2, 8, 7, 7)),), **{}):
Given groups=1, weight of size [3, 12, 1, 1], expected input[2, 8, 7, 7] to have 12 channels, but got 8 channels instead

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''