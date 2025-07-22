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
        self.conv_transpose = torch.nn.ConvTranspose3d(64, 8, (2, 2, 2), stride=1, padding=1, bias=True, dilation=(1, 1, 1))
        self.conv_transpose.weight.data = torch.randn([8, 64, 2, 2, 2])

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(6, 64, 1, 3, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [8, 64, 2, 2, 2], expected input[6, 64, 1, 3, 3] to have 8 channels, but got 64 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(6, 64, 1, 3, 3)),), **{}):
Given transposed=1, weight of size [8, 64, 2, 2, 2], expected input[6, 64, 1, 3, 3] to have 8 channels, but got 64 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''