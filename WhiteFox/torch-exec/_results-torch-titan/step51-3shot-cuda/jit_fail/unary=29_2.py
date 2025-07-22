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

    def __init__(self, min_value=4.99, max_value=4.0):
        super().__init__()
        self.relu6 = torch.nn.ReLU6()
        self.conv2d = torch.nn.Conv2d(3, 3, 1, stride=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(10, 6, 2, stride=2, padding=2)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x4):
        v1 = self.conv2d(x4)
        v2 = self.conv_transpose(v1)
        v3 = torch.clamp_min(v2, self.min_value)
        v4 = torch.clamp_max(v3, self.max_value)
        v5 = self.relu6(v4)
        return v5




func = Model().to('cuda')



x4 = torch.randn(1, 3, 8, 8)


test_inputs = [x4]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [10, 6, 2, 2], expected input[1, 3, 8, 8] to have 10 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 3, 8, 8)),), **{}):
Given transposed=1, weight of size [10, 6, 2, 2], expected input[1, 3, 8, 8] to have 10 channels, but got 3 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''