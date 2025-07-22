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
        self.conv = torch.nn.Conv2d(10, 8, 1, stride=1, padding=0)
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 200, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv_transpose(v1)
        v3 = F.relu(v2)
        v4 = self.conv2(v3)
        v5 = F.softmax(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 10, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 8, 1, 1], expected input[1, 8, 64, 64] to have 3 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)),), **{}):
Given transposed=1, weight of size [3, 8, 1, 1], expected input[1, 8, 64, 64] to have 3 channels, but got 8 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''