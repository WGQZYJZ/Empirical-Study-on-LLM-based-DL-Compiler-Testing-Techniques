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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(2, 3, 2, stride=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(10, 11, 3, stride=1)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.conv_transpose2(v1)
        v3 = torch.tanh(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 2, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [10, 11, 3, 3], expected input[1, 3, 33, 33] to have 10 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv_transpose2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 33, 33)),), **{}):
Given transposed=1, weight of size [10, 11, 3, 3], expected input[1, 3, 33, 33] to have 10 channels, but got 3 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''