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
        self.conv1 = torch.nn.Conv2d(8, 16, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 8, 1, stride=1, padding=0)
        self.conv3 = torch.nn.ConvTranspose2d(16, 8, 3, stride=2, padding=1, output_padding=1)
        self.conv4 = torch.nn.ConvTranspose2d(8, 4, 1, stride=1, padding=0)
        self.conv5 = torch.nn.ConvTranspose2d(4, 1, 3, stride=2, padding=1, output_padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = (v2 * 0.5)
        v4 = (v2 * 0.7071067811865476)
        v5 = torch.erf(v4)
        v6 = (v5 + 1)
        v7 = (v3 * v6)
        v8 = self.conv3(v7)
        v9 = self.conv4(v8)
        v10 = self.conv5(v9)
        return v10




func = Model().to('cuda')



x1 = torch.randn(1, 8, 112, 112)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [16, 8, 3, 3], expected input[1, 8, 56, 56] to have 16 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1, 8, 56, 56)),), **{}):
Given transposed=1, weight of size [16, 8, 3, 3], expected input[1, 8, 56, 56] to have 16 channels, but got 8 channels instead

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''