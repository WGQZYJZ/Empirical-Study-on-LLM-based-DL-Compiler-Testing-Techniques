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
        self.conv_transpose = torch.nn.ConvTranspose1d(512, 256, 1)
        self.conv_transpose1 = torch.nn.ConvTranspose1d(256, 128, 1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(128, 3, 1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.relu(v1)
        v3 = self.conv_transpose1(v2)
        v4 = torch.relu(v3)
        v5 = self.conv_transpose2(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(4, 512, 7)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [128, 3, 1, 1], expected input[1, 4, 128, 7] to have 128 channels, but got 4 channels instead

jit:
Failed running call_module L__self___conv_transpose2(*(FakeTensor(..., device='cuda:0', size=(4, 128, 7)),), **{}):
Given transposed=1, weight of size [128, 3, 1, 1], expected input[1, 4, 128, 7] to have 128 channels, but got 4 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''