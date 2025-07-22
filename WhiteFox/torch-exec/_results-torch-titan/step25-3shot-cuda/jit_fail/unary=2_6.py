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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(33, 8, kernel_size=3, padding=1, stride=1)
        self.relu1 = torch.nn.ReLU(inplace=True)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(1, 23, kernel_size=3, padding=1, stride=1)
        self.relu2 = torch.nn.ReLU(inplace=True)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.relu1(v1)
        v3 = self.conv_transpose2(x1)
        v4 = self.relu2(v3)
        v5 = (v1 + v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(3, 33, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 23, 3, 3], expected input[3, 33, 2, 2] to have 1 channels, but got 33 channels instead

jit:
Failed running call_module L__self___conv_transpose2(*(FakeTensor(..., device='cuda:0', size=(3, 33, 2, 2)),), **{}):
Given transposed=1, weight of size [1, 23, 3, 3], expected input[3, 33, 2, 2] to have 1 channels, but got 33 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''