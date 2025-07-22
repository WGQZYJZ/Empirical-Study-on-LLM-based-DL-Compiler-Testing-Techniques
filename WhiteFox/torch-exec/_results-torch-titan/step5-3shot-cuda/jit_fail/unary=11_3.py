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
        self.depthwise_conv_transpose = torch.nn.ConvTranspose2d(32, 32, 10, groups=32, stride=2, padding=5)

    def forward(self, x1):
        v1 = self.depthwise_conv_transpose(x1)
        v2 = (v1 + 3)
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = (v4 / 6)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 4, 8, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [32, 1, 10, 10], expected input[1, 4, 8, 8] to have 32 channels, but got 4 channels instead

jit:
Failed running call_module L__self___depthwise_conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 4, 8, 8)),), **{}):
Given transposed=1, weight of size [32, 1, 10, 10], expected input[1, 4, 8, 8] to have 32 channels, but got 4 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''