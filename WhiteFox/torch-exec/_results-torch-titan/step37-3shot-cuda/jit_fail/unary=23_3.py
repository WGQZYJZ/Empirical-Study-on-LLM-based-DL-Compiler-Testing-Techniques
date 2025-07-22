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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(3, 8, 8, stride=(4, 1), padding=2)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(1, 4, 2, stride=1, padding=(1, 2))
        self.conv_transpose3 = torch.nn.ConvTranspose2d(16, 16, 2, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = torch.tanh(v1)
        v3 = self.conv_transpose2(v2)
        v4 = self.conv_transpose3(v3)
        v5 = torch.tanh(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 4, 2, 2], expected input[1, 8, 1024, 259] to have 1 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv_transpose2(*(FakeTensor(..., device='cuda:0', size=(1, 8, 1024, 259)),), **{}):
Given transposed=1, weight of size [1, 4, 2, 2], expected input[1, 8, 1024, 259] to have 1 channels, but got 8 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''