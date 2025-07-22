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
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(16, 50, 1, stride=1, padding=0)
        self.conv_transpose_5 = torch.nn.ConvTranspose2d(51, 3, 3, stride=1, padding=1)

    def forward(self, x1):
        q1 = self.conv_transpose_4(x1)
        q2 = torch.sigmoid(q1)
        q3 = (q1 * q2)
        q4 = self.conv_transpose_5(q3)
        q5 = torch.sigmoid(q4)
        q6 = (q3 * q5)
        return q6




func = Model().to('cuda')



x1 = torch.randn(1, 16, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [51, 3, 3, 3], expected input[1, 50, 32, 32] to have 51 channels, but got 50 channels instead

jit:
Failed running call_module L__self___conv_transpose_5(*(FakeTensor(..., device='cuda:0', size=(1, 50, 32, 32)),), **{}):
Given transposed=1, weight of size [51, 3, 3, 3], expected input[1, 50, 32, 32] to have 51 channels, but got 50 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''