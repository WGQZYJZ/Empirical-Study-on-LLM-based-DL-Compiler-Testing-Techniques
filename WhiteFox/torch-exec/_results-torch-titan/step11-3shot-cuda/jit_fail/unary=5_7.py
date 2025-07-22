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
        self.conv_transpose = torch.nn.ConvTranspose2d(4, 16, 2, stride=1, padding=1, groups=4)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 8, 50, 50)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [4, 4, 2, 2], expected input[1, 8, 50, 50] to have 4 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 8, 50, 50)),), **{}):
Given transposed=1, weight of size [4, 4, 2, 2], expected input[1, 8, 50, 50] to have 4 channels, but got 8 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''