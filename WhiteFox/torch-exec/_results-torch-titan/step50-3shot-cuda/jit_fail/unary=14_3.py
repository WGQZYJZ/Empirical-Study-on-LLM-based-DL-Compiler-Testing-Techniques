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
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(5120, 1600, 7, stride=1, padding=3)
        self.relu_1 = torch.nn.ReLU(inplace=False)
        self.conv_transpose_5 = torch.nn.ConvTranspose2d(3300, 300, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose_4(x1)
        v2 = self.relu_1(v1)
        v3 = self.conv_transpose_5(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(4, 5120, 9, 9)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3300, 300, 3, 3], expected input[4, 1600, 9, 9] to have 3300 channels, but got 1600 channels instead

jit:
Failed running call_module L__self___conv_transpose_5(*(FakeTensor(..., device='cuda:0', size=(4, 1600, 9, 9)),), **{}):
Given transposed=1, weight of size [3300, 300, 3, 3], expected input[4, 1600, 9, 9] to have 3300 channels, but got 1600 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''