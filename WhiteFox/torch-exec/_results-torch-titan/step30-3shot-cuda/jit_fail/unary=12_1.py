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
        self.conv_1 = torch.nn.Conv2d(160, 1, 3)
        self.conv_1.weight = torch.nn.Parameter(torch.nn.init.normal_(torch.Tensor(64, 160, 3, 3), 0.01, 0.1))
        self.conv_1.bias = torch.nn.Parameter(torch.nn.init.uniform_(torch.Tensor(64, 160, 3, 3), 0.01, 0.1))
        self.conv_2 = torch.nn.Conv2d(64, 1, 3)
        self.conv_2.weight = torch.nn.Parameter(torch.nn.init.normal_(torch.Tensor(160, 64, 3, 3), 0.01, 0.1))
        self.conv_2.bias = torch.nn.Parameter(torch.nn.init.uniform_(torch.Tensor(160, 64, 3, 3), 0.01, 0.1))

    def forward(self, x1):
        v1 = self.conv_1(x1)
        v2 = F.sigmoid(v1)
        v3 = (v2 * v1)
        v3 = v3.sum(dim=1)
        v4 = self.conv_2(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 64, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 160, 3, 3], expected input[1, 64, 16, 16] to have 160 channels, but got 64 channels instead

jit:
Failed running call_module L__self___conv_1(*(FakeTensor(..., device='cuda:0', size=(1, 64, 16, 16)),), **{}):
Given groups=1, weight of size [64, 160, 3, 3], expected input[1, 64, 16, 16] to have 160 channels, but got 64 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''