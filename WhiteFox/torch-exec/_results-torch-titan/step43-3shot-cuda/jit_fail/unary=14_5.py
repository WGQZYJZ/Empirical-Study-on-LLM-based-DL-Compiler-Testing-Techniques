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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(665, 56, 3, stride=2, padding=(0, 1), dilation=(1, 1))
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(665, 315, 2, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = self.conv_transpose_2(v1)
        v3 = torch.sigmoid(v2)
        v4 = (v2 * v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 665, 120, 200)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [665, 315, 2, 2], expected input[1, 56, 241, 399] to have 665 channels, but got 56 channels instead

jit:
Failed running call_module L__self___conv_transpose_2(*(FakeTensor(..., device='cuda:0', size=(1, 56, 241, 399)),), **{}):
Given transposed=1, weight of size [665, 315, 2, 2], expected input[1, 56, 241, 399] to have 665 channels, but got 56 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''